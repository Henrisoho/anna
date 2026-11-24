#!/usr/bin/env python3
"""due-diligence: build request packets, track evidence, and score a deal.

Standard library only. If `openpyxl` is installed, packets also get an Excel tracker.

Commands
  types                                   list deal types and subtypes
  intake   --type T[,T2]                  print intake questions for a deal type
  packet   --type T[,T2] [--subtype a,b] [--conditions c,d] [--parts 4] --deal NAME [--sponsor NAME] [--out DIR]
                                          build the request packet, reviewer checklist and tracker
  update   --tracker FILE --id ID --status S [--evidence TEXT] [--note TEXT] [--by NAME]
                                          record a review result for one item
  bulk     --tracker FILE --json FILE     apply many updates: [{"id":..,"status":..,"evidence":..,"note":..}]
  status   --tracker FILE                 progress summary and what is blocking approval
  report   --tracker FILE [--out FILE]    write the diligence report and the decision
  validate                                check every library file against the schema

Decision rules (report)
  DECLINE    any kill test triggered, or any gating request failed
  NOT READY  any gating or core request not yet verified, any kill test unchecked,
             or any red flag present and not mitigated
  APPROVE TO IC  every gating and core request verified (core may be waived with a written note),
             every kill test clear, no open red flags. Supporting gaps are listed, not blocking.
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
LIB = HERE / "library"
REF = HERE / "references"

STAGES = ["screen", "term-sheet", "confirmatory", "third-party", "closing", "monitoring"]
STAGE_TITLES = {
    "screen": "Stage 1. Screen: send with your first reply",
    "term-sheet": "Stage 2. Before a term sheet or LOI",
    "confirmatory": "Stage 3. Confirmatory diligence",
    "third-party": "Stage 4. Third-party reports",
    "closing": "Stage 5. Closing deliverables",
    "monitoring": "Stage 6. Post-close reporting and monitoring",
}
PRIORITIES = ["gating", "core", "supporting"]
# --parts N splits the sponsor-facing list into N sendable parts (stage groupings).
PART_GROUPS = {
    2: [("Screen and term sheet", ["screen", "term-sheet"]),
        ("Confirmatory diligence, third-party reports, closing and monitoring",
         ["confirmatory", "third-party", "closing", "monitoring"])],
    3: [("Screen and term sheet", ["screen", "term-sheet"]),
        ("Confirmatory diligence and third-party reports", ["confirmatory", "third-party"]),
        ("Closing and post-close monitoring", ["closing", "monitoring"])],
    4: [("Screen", ["screen"]), ("Pre-term-sheet diligence and management questionnaire", ["term-sheet"]),
        ("Confirmatory diligence and third-party reports", ["confirmatory", "third-party"]),
        ("Closing deliverables and post-close reporting", ["closing", "monitoring"])],
    6: [(STAGE, [STAGE]) for STAGE in STAGES],
}
WORKSTREAMS = [
    "Sponsor & Background", "KYC/AML & Sanctions", "Corporate & Legal", "Financial", "Tax",
    "Commercial & Market", "Operational", "Technical", "Collateral & Title", "Regulatory & Compliance",
    "Environmental & ESG", "Insurance", "IT & Cyber", "HR & Management", "Structure & Terms",
    "Valuation & Model", "Fund Operations",
]
STATUS = {
    "request": ["requested", "received", "verified", "failed", "waived", "n/a"],
    "kill_test": ["unchecked", "clear", "triggered"],
    "red_flag": ["unchecked", "clear", "present", "mitigated"],
    "hard_question": ["unasked", "good", "weak", "evaded"],
}
NEEDS_NOTE = {"waived", "mitigated", "failed", "triggered", "present", "evaded", "n/a"}


# ---------------------------------------------------------------- library
def load(type_id):
    p = LIB / f"{type_id}.json"
    if not p.exists():
        sys.exit(f"Unknown deal type '{type_id}'. Run: dd.py types")
    return json.loads(p.read_text())


def all_types():
    return sorted(p.stem for p in LIB.glob("*.json") if p.stem != "universal")


def applies(item, subtypes):
    a = item.get("applies_to") or ["all"]
    return "all" in a or not subtypes or any(s in a for s in subtypes)


def assemble(types, subtypes, conditions=None):
    """Each library filters only by its own subtype ids. Universal 'subtypes' are deal conditions
    (operating-company, levered-vehicle, ...) passed via --conditions. A library with none of its
    subtypes selected includes every item."""
    libs = [load("universal")] + [load(t) for t in types]
    out = {k: [] for k in ["requests", "kill_tests", "red_flags", "metrics", "third_party_reports",
                           "hard_questions", "failure_cases", "intake_questions"]}
    known = {s["id"] for lib in libs for s in lib.get("subtypes", [])}
    unknown = [s for s in list(subtypes) + list(conditions or []) if s not in known]
    if unknown:
        sys.exit(f"Unknown subtype/condition {unknown}. Run: dd.py types")
    seen = set()
    for lib in libs:
        own = {s["id"] for s in lib.get("subtypes", [])}
        chosen = (conditions or []) if lib["type"] == "universal" else [s for s in subtypes if s in own]
        for k in out:
            for it in lib.get(k, []):
                iid = it.get("id") or f"{lib['type']}:{it.get('case', '')}"
                if iid in seen or not applies(it, chosen):
                    continue
                seen.add(iid)
                out[k].append({**it, "_type": lib["type"], "_type_name": lib.get("name", lib["type"])})
    out["requests"].sort(key=lambda r: (STAGES.index(r.get("stage", "confirmatory")),
                                        r["_type"] != "universal", r.get("order", 999), r["id"]))
    return libs, out


# ---------------------------------------------------------------- commands
def cmd_types(a):
    for t in ["universal"] + all_types():
        lib = load(t)
        print(f"{t:24s} {lib.get('name', '')}  ({len(lib.get('requests', []))} requests)")
        if t == "universal":
            print("    conditions (pass with --conditions):")
        for s in lib.get("subtypes", []):
            print(f"    - {s['id']:28s} {s.get('name', '')}")


def cmd_intake(a):
    types = [t for t in a.type.split(",") if t] if a.type else []
    for t in ["universal"] + types:
        lib = load(t)
        print(f"\n## {lib.get('name', t)}")
        for q in lib.get("intake_questions", []):
            print(f"- [{q['id']}] {q['question']}" + (f"  (why: {q['why']})" if q.get("why") else ""))


def md_escape(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ")


def cmd_packet(a):
    types = [t for t in a.type.split(",") if t]
    subtypes = [s for s in (a.subtype or "").split(",") if s]
    conditions = [s for s in (a.conditions or "").split(",") if s]
    libs, d = assemble(types, subtypes, conditions)
    exclude = {x for x in (a.exclude or "").split(",") if x}
    if exclude:
        known = {i["id"] for k in ("requests", "kill_tests", "red_flags", "hard_questions") for i in d[k]}
        if exclude - known:
            sys.exit(f"--exclude ids not in this packet: {sorted(exclude - known)}")
        for k in ("requests", "kill_tests", "red_flags", "hard_questions"):
            d[k] = [i for i in d[k] if i["id"] not in exclude]
    slug = "".join(c if c.isalnum() else "-" for c in a.deal.lower()).strip("-")
    out = Path(a.out or f"dd-{slug}")
    out.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    names = ", ".join(l.get("name", l["type"]) for l in libs[1:])
    sponsor = a.sponsor or "the sponsor"

    # Sponsor-facing request list
    L = [f"# Due Diligence Request List: {a.deal}", "",
         f"Deal type: {names}" + (f" ({', '.join(subtypes)})" if subtypes else ""),
         f"Prepared for: {sponsor}  |  Date: {today}", "",
         "## How to respond", "",
         "1. Work through the stages in order. We review Stage 1 before we request Stage 2.",
         "2. Upload each document to the data room in a folder named with its request number (e.g. `U-SPO-010`).",
         "3. Items marked **GATING** must be satisfied for the deal to proceed. Items marked **CORE** are required.",
         "   **SUPPORTING** items are requested; tell us if one does not exist rather than leaving it blank.",
         "4. Where we ask for third-party documents (bank statements, confirmations, reports), we will also verify",
         "   them directly with the issuer. Please sign the authorizations in Stage 1 so we can.",
         "5. If something does not apply, write \"N/A\" with one line explaining why.", ""]
    n = 0
    for st in STAGES:
        items = [r for r in d["requests"] if r.get("stage") == st]
        if not items:
            continue
        L += [f"## {STAGE_TITLES[st]}", "", "| # | Ref | Priority | Workstream | Request | What we need to see |",
              "|---|---|---|---|---|---|"]
        for r in items:
            n += 1
            L.append(f"| {n} | {r['id']} | {r['priority'].upper()} | {md_escape(r['workstream'])} | "
                     f"{md_escape(r['request'])} | {md_escape(r.get('format'))} |")
        L.append("")
    if d["hard_questions"]:
        L += ["## Management questionnaire", "",
              "Please answer each question in writing. We will discuss the answers on a call.", ""]
        for i, q in enumerate(d["hard_questions"], 1):
            L.append(f"{i}. {q['question']}  `{q['id']}`")
        L.append("")
    if a.md:
        (out / "01_request_list.md").write_text("\n".join(L))
        if a.parts:
            write_parts(out, a, d, names, subtypes, sponsor, today)

    # Internal reviewer checklist with pass criteria
    R = [f"# Reviewer checklist (internal): {a.deal}", "",
         "Not for the sponsor. Pass criteria, verification steps, kill tests and red flags.", ""]
    for lib in libs[1:]:
        if lib.get("one_check"):
            R += [f"> **THE ONE CHECK ({lib.get('name')}):** {lib['one_check']}", ""]
    R += ["## Kill tests (any one triggered = decline)", ""]
    R += [f"- [ ] `{k['id']}` {k['test']} (bible {k.get('ref', '')})" for k in d["kill_tests"]] + [""]
    R += ["## Requests: pass criteria and independent verification", ""]
    for st in STAGES:
        items = [r for r in d["requests"] if r.get("stage") == st]
        if not items:
            continue
        R += [f"### {STAGE_TITLES[st]}", ""]
        for r in items:
            R += [f"**`{r['id']}` [{r['priority'].upper()}] {r['request']}**" + ("  *WEAK threshold*" if r.get("weak") else ""),
                  f"- Why: {r.get('why', '')}", f"- Pass: {r.get('pass', '')}", f"- Fail: {r.get('fail', '')}",
                  f"- Verify independently: {r.get('verify', '')}", f"- Bible: {r.get('ref', '')}", ""]
    R += ["## Red flags to test", ""]
    R += [f"- [ ] `{f['id']}` {f['flag']}  CHECK: {f.get('check', '')} (bible {f.get('ref', '')})" for f in d["red_flags"]] + [""]
    R += ["## Benchmarks", "", "| Metric | Acceptable | Source | Weak |", "|---|---|---|---|"]
    R += [f"| {md_escape(m['metric'])} | {md_escape(m.get('acceptable'))} | {md_escape(m.get('source'))} | "
          f"{'WEAK' if m.get('weak') else ''} |" for m in d["metrics"]] + [""]
    R += ["## Third-party reports to commission", ""]
    R += [f"- `{t['id']}` {t['report']}: {t.get('provider', '')}. Required: {t.get('required_when', '')}" for t in d["third_party_reports"]] + [""]
    R += ["## Hard questions and what a good answer looks like", ""]
    R += [f"- `{q['id']}` {q['question']}\n  - Good answer: {q.get('good_answer', '')}" for q in d["hard_questions"]] + [""]
    R += ["## Failure cases this packet is built to catch", ""]
    R += [f"- **{c.get('case')} ({c.get('year', '')})**: {c.get('what_happened', '')} CHECK: {c.get('check', '')}" for c in d["failure_cases"]]
    chapters = sorted({c for l in libs for c in l.get("chapters", [])})
    R += ["", "## Read before reviewing", ""] + [f"- references/{c}" for c in chapters]
    if a.md:
        (out / "02_reviewer_checklist.md").write_text("\n".join(R))
    pdfs = write_pdfs(out, a, libs, d, names, subtypes, sponsor, today, chapters)

    # Tracker
    items = []
    for kind, key, default in [("request", "requests", "requested"), ("kill_test", "kill_tests", "unchecked"),
                               ("red_flag", "red_flags", "unchecked"), ("hard_question", "hard_questions", "unasked")]:
        for it in d[key]:
            items.append({**{k: v for k, v in it.items() if not k.startswith("_")}, "deal_type": it["_type"],
                          "kind": kind, "status": default, "evidence": "", "note": "", "by": "", "date": ""})
    tracker = {"deal": a.deal, "sponsor": a.sponsor or "", "types": types, "subtypes": subtypes,
               "conditions": conditions, "excluded": sorted(exclude),
               "created": today, "metrics": d["metrics"], "third_party_reports": d["third_party_reports"],
               "chapters": chapters, "items": items}
    tp = out / "tracker.json"
    tp.write_text(json.dumps(tracker, indent=1))
    xl = write_xlsx(out / "03_Request_Tracker.xlsx", a.deal, d)
    print(f"Packet written to {out}/  ({n} requests, {len(d['hard_questions'])} questions, "
          f"{len(d['kill_tests'])} kill tests, {len(d['red_flags'])} red flags)")
    for f, what in pdfs:
        print(f"  {f:44s} {what}")
    if a.md:
        print("  01_request_list.md / 02_reviewer_checklist.md  Markdown copies")
    print(f"  tracker.json                                 review state; update with: dd.py update --tracker {tp} --id ID --status S")
    if xl:
        print(f"  03_Request_Tracker.xlsx                      spreadsheet tracker (share with sponsor or keep internal)")


def write_parts(out, a, d, names, subtypes, sponsor, today):
    if a.parts not in PART_GROUPS:
        sys.exit(f"--parts must be one of {sorted(PART_GROUPS)}")
    groups = PART_GROUPS[a.parts]
    num = {r["id"]: i for i, r in enumerate(d["requests"], 1)}
    q_part = next((i for i, (_, sts) in enumerate(groups) if "term-sheet" in sts), 0)
    for i, (title, sts) in enumerate(groups):
        items = [r for r in d["requests"] if r.get("stage") in sts]
        g = sum(r["priority"] == "gating" for r in items)
        P = [f"# Due Diligence Request Packet, Part {i + 1} of {len(groups)}: {title}", "",
             f"Deal: {a.deal}  |  Deal type: {names}" + (f" ({', '.join(subtypes)})" if subtypes else ""),
             f"Prepared for: {sponsor}  |  Date: {today}", "",
             f"{len(items)} requests ({g} gating). "
             + ("Part 1 goes out with our first reply. " if i == 0 else
                f"We send Part {i + 1} once Part {i} has been reviewed and cleared. ")
             + "Gating items must be satisfied for the deal to proceed; core items are required; supporting items "
               "are requested (tell us if one does not exist). Upload each document to the data room in a folder "
               "named with its request number. Write \"N/A\" with a one-line reason for anything that does not "
               "apply. We verify bank statements, confirmations and third-party documents directly with the issuer.", ""]
        for st in sts:
            rs = [r for r in items if r.get("stage") == st]
            if not rs:
                continue
            P += [f"## {STAGE_TITLES[st]}", "", "| # | Ref | Priority | Workstream | Request | What we need to see |",
                  "|---|---|---|---|---|---|"]
            P += [f"| {num[r['id']]} | {r['id']} | {r['priority'].upper()} | {md_escape(r['workstream'])} | "
                  f"{md_escape(r['request'])} | {md_escape(r.get('format'))} |" for r in rs] + [""]
        if i == q_part and d["hard_questions"]:
            P += ["## Management questionnaire", "",
                  "Answer each question in writing before the management call.", ""]
            P += [f"{k}. {q['question']}  `{q['id']}`" for k, q in enumerate(d["hard_questions"], 1)] + [""]
        (out / f"01_part{i + 1}_{'-'.join(sts)}.md").write_text("\n".join(P))
        print(f"  01_part{i + 1}_{'-'.join(sts)}.md  {len(items)} requests ({g} gating)")


def write_pdfs(out, a, libs, d, names, subtypes, sponsor, today, chapters):
    try:
        import pdf as P
    except ImportError:
        print("reportlab is not installed (pip install reportlab): writing Markdown instead of PDF", file=sys.stderr)
        a.md = True
        return []
    firm = a.firm or "[Firm name]"
    subnames = {s["id"]: s.get("name", s["id"]) for l in libs[1:] for s in l.get("subtypes", [])}
    deal_type = "; ".join(
        l.get("name", l["type"]) + (" (" + ", ".join(subnames[s] for s in subtypes
                                                    if s in {x["id"] for x in l.get("subtypes", [])}) + ")"
                                    if any(s in {x["id"] for x in l.get("subtypes", [])} for s in subtypes) else "")
        for l in libs[1:])
    groups = PART_GROUPS.get(a.parts or 1, [("Full request list", STAGES)]) if (a.parts or 1) != 1 else \
        [("Full request list", STAGES)]
    if a.parts and a.parts not in PART_GROUPS:
        sys.exit(f"--parts must be one of {sorted(PART_GROUPS)}")
    # number requests in the order they appear in the PDFs (part > stage > workstream)
    num, k = {}, 0
    for _, sts in groups:
        for st in sts:
            rows = [r for r in d["requests"] if r.get("stage") == st]
            for ws in dict.fromkeys(r["workstream"] for r in rows):
                for r in rows:
                    if r["workstream"] == ws:
                        k += 1
                        num[r["id"]] = k
    q_part = next((i for i, (_, sts) in enumerate(groups) if "term-sheet" in sts), 0)
    files, summary = [], []
    for i, (title, sts) in enumerate(groups):
        rs = [r for r in d["requests"] if r.get("stage") in sts]
        summary.append((title, len(rs), sum(r["priority"] == "gating" for r in rs)))
        label = f"Part {i + 1} of {len(groups)}: {title}" if len(groups) > 1 else "Complete request list"
        fn = (f"Part{i + 1}_{title.split(' and ')[0].replace(' ', '-').replace(',', '')}.pdf" if len(groups) > 1
              else "Request_List.pdf")
        fn = f"01_{fn}"
        P.request_pdf(out / fn, firm=firm, deal=a.deal, sponsor=sponsor, deal_type=deal_type, part_label=label,
                      part_title=title, part_no=i + 1, n_parts=len(groups), requests=rs, num=num,
                      questions=d["hard_questions"] if i == q_part else [],
                      stage_titles=[(st, STAGE_TITLES[st].split(". ", 1)[-1]) for st in sts], contact=a.contact,
                      data_room=a.data_room, today=today, include_certification=(i == 0))
        files.append((fn, f"send to sponsor: {len(rs)} requests" + (", questionnaire" if i == q_part else "")
                      + (", certification" if i == 0 else "")))
    notes = []
    if a.notes:
        notes = [ln.rstrip() for ln in Path(a.notes).read_text().splitlines() if ln.strip()]
    P.letter_pdf(out / "00_Cover_Letter.pdf", firm=firm, deal=a.deal, sponsor=sponsor, deal_type=deal_type,
                 today=today, parts=summary, notes=notes, contact=a.contact, data_room=a.data_room)
    files.insert(0, ("00_Cover_Letter.pdf", "send to sponsor with Part 1"))
    P.checklist_pdf(out / "02_Reviewer_Checklist_INTERNAL.pdf", firm=firm, deal=a.deal, deal_type=deal_type, today=today,
                    one_checks=[(l.get("name"), l["one_check"]) for l in libs[1:] if l.get("one_check")],
                    kill_tests=d["kill_tests"], requests=d["requests"], red_flags=d["red_flags"],
                    metrics=d["metrics"], third_parties=d["third_party_reports"], questions=d["hard_questions"],
                    failure_cases=d["failure_cases"], chapters=chapters,
                    stage_titles=[(st, STAGE_TITLES[st].split(". ", 1)[-1]) for st in STAGES])
    files.append(("02_Reviewer_Checklist_INTERNAL.pdf", "internal only: pass criteria, kill tests, red flags"))
    return files


def write_xlsx(path, deal, d):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Alignment, Font, PatternFill
        from openpyxl.worksheet.datavalidation import DataValidation
    except ImportError:
        return False
    wb = Workbook()
    ws = wb.active
    ws.title = "Requests"
    hdr = ["#", "Ref", "Stage", "Priority", "Workstream", "Request", "Format", "Status", "Date received",
           "Data room location", "Sponsor comment", "Reviewer note"]
    ws.append(hdr)
    for i, r in enumerate(d["requests"], 1):
        ws.append([i, r["id"], r.get("stage"), r["priority"].upper(), r["workstream"], r["request"],
                   r.get("format", ""), "Requested", "", "", "", ""])
    dv = DataValidation(type="list", formula1='"Requested,Received,Verified,Failed,Waived,N/A"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"H2:H{len(d['requests']) + 1}")
    widths = [5, 13, 13, 11, 22, 60, 40, 12, 14, 22, 30, 30]
    for col, w in zip("ABCDEFGHIJKL", widths):
        ws.column_dimensions[col].width = w
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1A3A5A")
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    q = wb.create_sheet("Questions")
    q.append(["#", "Ref", "Question", "Sponsor answer"])
    for i, h in enumerate(d["hard_questions"], 1):
        q.append([i, h["id"], h["question"], ""])
    q.column_dimensions["C"].width = 80
    q.column_dimensions["D"].width = 60
    wb.save(path)
    return True


def tracker_load(p):
    return json.loads(Path(p).read_text())


def apply_update(t, iid, status, evidence="", note="", by=""):
    it = next((i for i in t["items"] if i["id"] == iid), None)
    if not it:
        raise SystemExit(f"No item {iid} in tracker")
    allowed = STATUS[it["kind"]]
    if status not in allowed:
        raise SystemExit(f"{iid} is a {it['kind']}; status must be one of {allowed}")
    if status in NEEDS_NOTE and not (note or it.get("note")):
        raise SystemExit(f"Status '{status}' needs --note explaining why (for the record)")
    if status == "verified" and not (evidence or it.get("evidence")):
        raise SystemExit("Status 'verified' needs --evidence (document, source, who confirmed it)")
    it["status"] = status
    if evidence:
        it["evidence"] = evidence
    if note:
        it["note"] = note
    it["by"] = by or it.get("by", "")
    it["date"] = dt.date.today().isoformat()


def cmd_update(a):
    t = tracker_load(a.tracker)
    apply_update(t, a.id, a.status, a.evidence or "", a.note or "", a.by or "")
    Path(a.tracker).write_text(json.dumps(t, indent=1))
    print(f"{a.id} -> {a.status}")


def cmd_bulk(a):
    t = tracker_load(a.tracker)
    ups = json.loads(Path(a.json).read_text())
    for u in ups:
        apply_update(t, u["id"], u["status"], u.get("evidence", ""), u.get("note", ""), u.get("by", ""))
    Path(a.tracker).write_text(json.dumps(t, indent=1))
    print(f"applied {len(ups)} updates")


def decide(t):
    req = [i for i in t["items"] if i["kind"] == "request"]
    kills = [i for i in t["items"] if i["kind"] == "kill_test"]
    flags = [i for i in t["items"] if i["kind"] == "red_flag"]
    reasons = {"decline": [], "blocking": []}
    reasons["decline"] += [f"Kill test triggered: {k['id']} {k['test']}" for k in kills if k["status"] == "triggered"]
    reasons["decline"] += [f"Gating request failed: {r['id']} {r['request']}" for r in req
                           if r["priority"] == "gating" and r["status"] == "failed"]
    for r in req:
        if r["priority"] in ("gating", "core") and r["status"] not in ("verified", "n/a") and not (
                r["priority"] == "core" and r["status"] == "waived"):
            reasons["blocking"].append(f"{r['priority'].upper()} not verified ({r['status']}): {r['id']} {r['request']}")
    reasons["blocking"] += [f"Kill test unchecked: {k['id']} {k['test']}" for k in kills if k["status"] == "unchecked"]
    reasons["blocking"] += [f"Red flag open: {f['id']} {f['flag']}" for f in flags if f["status"] == "present"]
    if reasons["decline"]:
        return "DECLINE", reasons
    if reasons["blocking"]:
        return "NOT READY", reasons
    return "APPROVE TO IC", reasons


def counts(items, kind):
    out = {}
    for i in items:
        if i["kind"] == kind:
            k = (i.get("priority", "-"), i["status"])
            out[k] = out.get(k, 0) + 1
    return out


def cmd_status(a):
    t = tracker_load(a.tracker)
    decision, why = decide(t)
    req = [i for i in t["items"] if i["kind"] == "request"]
    print(f"{t['deal']}  [{', '.join(t['types'])}]  decision now: {decision}")
    for p in PRIORITIES:
        rs = [r for r in req if r["priority"] == p]
        by = {}
        for r in rs:
            by[r["status"]] = by.get(r["status"], 0) + 1
        print(f"  {p:10s} {len(rs):4d}  " + "  ".join(f"{k}:{v}" for k, v in sorted(by.items())))
    for kind in ("kill_test", "red_flag", "hard_question"):
        by = {}
        for i in t["items"]:
            if i["kind"] == kind:
                by[i["status"]] = by.get(i["status"], 0) + 1
        print(f"  {kind:10s}       " + "  ".join(f"{k}:{v}" for k, v in sorted(by.items())))
    for r in (why["decline"] + why["blocking"])[: a.limit]:
        print("   - " + r)
    extra = len(why["decline"] + why["blocking"]) - a.limit
    if extra > 0:
        print(f"   ... and {extra} more")


def cmd_report(a):
    t = tracker_load(a.tracker)
    decision, why = decide(t)
    items = t["items"]
    req = [i for i in items if i["kind"] == "request"]
    today = dt.date.today().isoformat()
    L = [f"# Diligence Report: {t['deal']}", "",
         f"Sponsor: {t.get('sponsor') or '-'}  |  Deal type: {', '.join(t['types'])}"
         + (f" ({', '.join(t['subtypes'])})" if t["subtypes"] else "") + f"  |  Report date: {today}", "",
         f"## Decision: {decision}", ""]
    if decision == "DECLINE":
        L += ["The deal fails at least one kill test or gating request:", ""] + [f"- {r}" for r in why["decline"]] + [""]
    elif decision == "NOT READY":
        L += [f"{len(why['blocking'])} items block approval. Every gating and core item must be verified, every kill test "
              "cleared, and every red flag closed.", ""]
    else:
        L += ["Every gating and core request is verified (or core waived with a written exception), every kill test is "
              "clear, and no red flag is open. Recommend presenting to the investment committee.", ""]

    def section(title, rows, fields):
        nonlocal L
        L += [f"## {title}", ""]
        if not rows:
            L += ["None.", ""]
            return
        L += ["| " + " | ".join(h for h, _ in fields) + " |", "|" + "---|" * len(fields)]
        for r in rows:
            L.append("| " + " | ".join(md_escape(f(r)) for _, f in fields) + " |")
        L.append("")

    ref = ("Ref", lambda r: r["id"])
    section("Red flags found and their status",
            [i for i in items if i["kind"] == "red_flag" and i["status"] in ("present", "mitigated")],
            [ref, ("Red flag", lambda r: r["flag"]), ("Status", lambda r: r["status"]), ("Note", lambda r: r["note"])])
    section("Kill tests", [i for i in items if i["kind"] == "kill_test"],
            [ref, ("Test", lambda r: r["test"]), ("Result", lambda r: r["status"]), ("Note", lambda r: r["note"])])
    section("What was verified independently, and how",
            [r for r in req if r["status"] == "verified"],
            [ref, ("Item", lambda r: r["request"]), ("Evidence", lambda r: r["evidence"]), ("By", lambda r: r["by"]),
             ("Weak threshold", lambda r: "WEAK" if r.get("weak") else "")])
    section("What could NOT be verified",
            [r for r in req if r["status"] in ("requested", "received", "failed")],
            [ref, ("Priority", lambda r: r["priority"].upper()), ("Item", lambda r: r["request"]),
             ("Status", lambda r: r["status"]), ("Note", lambda r: r["note"])])
    section("Exceptions and waivers (need IC sign-off)",
            [r for r in req if r["status"] in ("waived", "n/a")],
            [ref, ("Priority", lambda r: r["priority"].upper()), ("Item", lambda r: r["request"]),
             ("Status", lambda r: r["status"]), ("Reason", lambda r: r["note"])])
    section("Hard questions: answers", [i for i in items if i["kind"] == "hard_question" and i["status"] != "unasked"],
            [ref, ("Question", lambda r: r["question"]), ("Answer quality", lambda r: r["status"]),
             ("Note", lambda r: r["note"])])
    weak = [r for r in req if r.get("weak") and r["status"] == "verified"]
    L += ["## Thresholds that rest on weak sourcing", "",
          f"{len(weak)} verified items were tested against a WEAK benchmark. Confirm those benchmarks with a primary "
          "source or practitioner before they anchor the decision." if weak else "None.", ""]
    L += ["## Progress by workstream", "", "| Workstream | Verified | Open | Failed | Waived/NA |", "|---|---|---|---|---|"]
    for ws in sorted({r["workstream"] for r in req}):
        rs = [r for r in req if r["workstream"] == ws]
        L.append(f"| {ws} | {sum(r['status'] == 'verified' for r in rs)} | "
                 f"{sum(r['status'] in ('requested', 'received') for r in rs)} | {sum(r['status'] == 'failed' for r in rs)} | "
                 f"{sum(r['status'] in ('waived', 'n/a') for r in rs)} |")
    L += ["", "## Sections the reviewer still writes", "",
          "Fill these from the references (A.2 Diligence report template):", "",
          "- Deal summary and structure", "- The numbers: model, base and downside, sensitivities, return attribution",
          "- Third-party reports obtained; sponsor background-check summary", "- Open concerns and unresolved questions",
          "- Recommendation and conditions precedent", ""]
    out = Path(a.out) if a.out else Path(a.tracker).with_name("diligence_report.md")
    out.write_text("\n".join(L))
    print(f"{decision}  -> {out}")


def cmd_validate(a):
    ok = True
    ids = {}
    for p in sorted(LIB.glob("*.json")):
        try:
            lib = json.loads(p.read_text())
        except Exception as e:
            print(f"FAIL {p.name}: invalid JSON: {e}")
            ok = False
            continue
        errs = []
        if lib.get("type") != p.stem:
            errs.append(f"type '{lib.get('type')}' != filename")
        subs = {s["id"] for s in lib.get("subtypes", [])}
        for r in lib.get("requests", []):
            for f in ("id", "stage", "priority", "workstream", "request", "pass"):
                if not r.get(f):
                    errs.append(f"{r.get('id', '?')}: missing {f}")
            if r.get("stage") not in STAGES:
                errs.append(f"{r.get('id')}: bad stage {r.get('stage')}")
            if r.get("priority") not in PRIORITIES:
                errs.append(f"{r.get('id')}: bad priority {r.get('priority')}")
            if r.get("workstream") not in WORKSTREAMS:
                errs.append(f"{r.get('id')}: bad workstream {r.get('workstream')}")
        for k in ("requests", "kill_tests", "red_flags", "metrics", "third_party_reports", "hard_questions",
                  "intake_questions"):
            for it in lib.get(k, []):
                i = it.get("id")
                if not i:
                    errs.append(f"{k}: item without id")
                    continue
                if i in ids:
                    errs.append(f"duplicate id {i} (also in {ids[i]})")
                ids[i] = p.name
                bad = [s for s in it.get("applies_to", ["all"]) if s != "all" and s not in subs]
                if bad:
                    errs.append(f"{i}: applies_to unknown subtype {bad}")
        for c in lib.get("chapters", []):
            if not (REF / c).exists():
                errs.append(f"chapter file missing: {c}")
        n = {k: len(lib.get(k, [])) for k in ("requests", "kill_tests", "red_flags", "metrics", "hard_questions", "failure_cases")}
        print(f"{'OK  ' if not errs else 'FAIL'} {p.name:32s} " + " ".join(f"{k}={v}" for k, v in n.items()))
        for e in errs[:15]:
            print("     " + e)
        if len(errs) > 15:
            print(f"     ... {len(errs) - 15} more")
        ok &= not errs
    sys.exit(0 if ok else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("types")
    s = sp.add_parser("intake"); s.add_argument("--type", default="")
    s = sp.add_parser("packet"); s.add_argument("--type", required=True); s.add_argument("--subtype")
    s.add_argument("--conditions", help="universal deal conditions, e.g. operating-company,levered-vehicle")
    s.add_argument("--deal", required=True); s.add_argument("--sponsor"); s.add_argument("--out")
    s.add_argument("--firm", help="your firm name for letterhead and headers")
    s.add_argument("--contact", help="contact line for the letter and request list, e.g. 'Jane Doe, jane@firm.com'")
    s.add_argument("--data-room", dest="data_room", help="data room name or link")
    s.add_argument("--notes", help="text file of deal-specific notes for the cover letter ('- ' lines become bullets)")
    s.add_argument("--md", action="store_true", help="also write Markdown copies")
    s.add_argument("--exclude", help="comma-separated item ids that do not apply to this deal (recorded in tracker)")
    s.add_argument("--parts", type=int, help="also split the sponsor list into 2, 3, 4 or 6 sendable parts")
    s = sp.add_parser("update"); s.add_argument("--tracker", required=True); s.add_argument("--id", required=True)
    s.add_argument("--status", required=True); s.add_argument("--evidence"); s.add_argument("--note"); s.add_argument("--by")
    s = sp.add_parser("bulk"); s.add_argument("--tracker", required=True); s.add_argument("--json", required=True)
    s = sp.add_parser("status"); s.add_argument("--tracker", required=True); s.add_argument("--limit", type=int, default=25)
    s = sp.add_parser("report"); s.add_argument("--tracker", required=True); s.add_argument("--out")
    sp.add_parser("validate")
    a = ap.parse_args()
    globals()[f"cmd_{a.cmd}"](a)


if __name__ == "__main__":
    main()
