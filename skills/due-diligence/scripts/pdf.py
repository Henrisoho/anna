"""PDF rendering for due-diligence packets (ReportLab).

Produces documents in the form an institutional fund or lender sends: a cover letter on letterhead, a request list
per part (cover page, instructions, request tables grouped by workstream with a response column, management
questionnaire with answer space, certification page), and an internal reviewer checklist.

Install: pip install reportlab
"""
import datetime as dt
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Frame, KeepTogether, NextPageTemplate, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

NAVY = colors.HexColor("#14304f")
RULE = colors.HexColor("#9aa7b5")
SHADE = colors.HexColor("#e9eef3")
GROUP = colors.HexColor("#d4dde7")
GATING = colors.HexColor("#8b1a1a")
CORE = colors.HexColor("#14304f")
SUPP = colors.HexColor("#5f6b78")
PRIO_COLOR = {"gating": GATING, "core": CORE, "supporting": SUPP}

_ss = getSampleStyleSheet()
S = {
    "body": ParagraphStyle("body", parent=_ss["Normal"], fontName="Helvetica", fontSize=9.5, leading=13),
    "small": ParagraphStyle("small", parent=_ss["Normal"], fontName="Helvetica", fontSize=7.8, leading=9.6),
    "smallb": ParagraphStyle("smallb", parent=_ss["Normal"], fontName="Helvetica-Bold", fontSize=7.8, leading=9.6),
    "cell": ParagraphStyle("cell", parent=_ss["Normal"], fontName="Helvetica", fontSize=8, leading=10),
    "cellb": ParagraphStyle("cellb", parent=_ss["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=10),
    "hdr": ParagraphStyle("hdr", parent=_ss["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=10,
                          textColor=colors.white),
    "h1": ParagraphStyle("h1", parent=_ss["Heading1"], fontName="Helvetica-Bold", fontSize=15, leading=19,
                         textColor=NAVY, spaceBefore=4, spaceAfter=8),
    "h2": ParagraphStyle("h2", parent=_ss["Heading2"], fontName="Helvetica-Bold", fontSize=11.5, leading=15,
                         textColor=NAVY, spaceBefore=10, spaceAfter=6),
    "h3": ParagraphStyle("h3", parent=_ss["Heading3"], fontName="Helvetica-Bold", fontSize=9.5, leading=12,
                         textColor=NAVY, spaceBefore=8, spaceAfter=3),
    "firm": ParagraphStyle("firm", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=NAVY),
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=24, leading=29, textColor=NAVY),
    "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=13, leading=17, textColor=NAVY),
    "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=10, leading=15),
    "notice": ParagraphStyle("notice", fontName="Helvetica", fontSize=7.8, leading=10, textColor=SUPP),
    "banner": ParagraphStyle("banner", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=colors.white,
                             alignment=TA_CENTER),
}

CONFIDENTIALITY = (
    "CONFIDENTIAL. This request list and any information provided in response are confidential and are furnished "
    "solely to evaluate the proposed transaction. A request is not an offer, commitment or agreement to invest or "
    "lend; any investment is subject to completion of diligence, investment committee approval and definitive "
    "documentation. Documents provided may be verified directly with their issuers.")


def p(text, style="cell"):
    return Paragraph(escape(str(text or "")), S[style] if isinstance(style, str) else style)


class Doc(BaseDocTemplate):
    def __init__(self, path, firm, left_hdr, right_hdr, footer, internal=False):
        super().__init__(str(path), pagesize=letter, leftMargin=0.7 * inch, rightMargin=0.7 * inch,
                         topMargin=0.85 * inch, bottomMargin=0.75 * inch, title=footer, author=firm)
        self.firm, self.left_hdr, self.right_hdr, self.footer, self.internal = firm, left_hdr, right_hdr, footer, internal
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="f")
        self.addPageTemplates([PageTemplate("cover", [fr], onPage=self._cover),
                               PageTemplate("body", [fr], onPage=self._body)])

    def _cover(self, c, d):
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, letter[1] - 0.28 * inch, letter[0], 0.28 * inch, fill=1, stroke=0)
        if self.internal:
            c.setFillColor(GATING)
            c.rect(0, 0, letter[0], 0.3 * inch, fill=1, stroke=0)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(letter[0] / 2, 0.11 * inch, "INTERNAL: DO NOT DISTRIBUTE TO THE SPONSOR")
        c.restoreState()

    def _body(self, c, d):
        c.saveState()
        w, h = letter
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.line(self.leftMargin, h - 0.6 * inch, w - self.rightMargin, h - 0.6 * inch)
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(NAVY)
        c.drawString(self.leftMargin, h - 0.52 * inch, self.left_hdr)
        c.setFont("Helvetica", 8)
        c.setFillColor(GATING if self.internal else SUPP)
        c.drawRightString(w - self.rightMargin, h - 0.52 * inch, self.right_hdr)
        c.line(self.leftMargin, 0.55 * inch, w - self.rightMargin, 0.55 * inch)
        c.setFillColor(SUPP)
        c.drawString(self.leftMargin, 0.4 * inch, self.footer)
        c.drawRightString(w - self.rightMargin, 0.4 * inch, f"Page {d.page}")
        c.restoreState()


def _kv_table(rows):
    t = Table([[p(k, "smallb"), p(v, "meta")] for k, v in rows], colWidths=[1.6 * inch, 4.9 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                           ("LINEBELOW", (0, 0), (-1, -1), 0.3, RULE)]))
    return t


def _cover(story, firm, title, subtitle, rows, internal=False):
    story += [Spacer(1, 0.6 * inch), p(firm, "firm"), Spacer(1, 1.3 * inch), p(title, "title"), Spacer(1, 6),
              p(subtitle, "subtitle"), Spacer(1, 0.45 * inch), _kv_table(rows), Spacer(1, 1.5 * inch)]
    if not internal:
        story.append(p(CONFIDENTIALITY, "notice"))
    story += [NextPageTemplate("body"), PageBreak()]


def _prio(r):
    return Paragraph(f'<font size="7" color="{PRIO_COLOR[r["priority"]].hexval()}"><b>{r["priority"].upper()}</b></font>',
                     S["cell"])


def _request_table(rows, num):
    """Rows grouped by workstream; columns: No., Ref, Priority, Request, Evidence required, Response."""
    widths = [0.36, 0.9, 0.82, 2.4, 1.62, 1.0]
    data = [[p(h, "hdr") for h in ["No.", "Ref", "Priority", "Request", "Evidence required", "Sponsor response / location"]]]
    style = [("BACKGROUND", (0, 0), (-1, 0), NAVY), ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("GRID", (0, 0), (-1, -1), 0.3, RULE), ("TOPPADDING", (0, 0), (-1, -1), 3),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 4),
             ("RIGHTPADDING", (0, 0), (-1, -1), 4)]
    order = []
    for r in rows:
        if r["workstream"] not in order:
            order.append(r["workstream"])
    for ws in order:
        data.append([p(ws.upper(), "cellb"), "", "", "", "", ""])
        i = len(data) - 1
        style += [("SPAN", (0, i), (-1, i)), ("BACKGROUND", (0, i), (-1, i), GROUP)]
        for r in [x for x in rows if x["workstream"] == ws]:
            data.append([p(num[r["id"]]), p(r["id"]), _prio(r), p(r["request"]), p(r.get("format")), ""])
    t = Table(data, colWidths=[w * inch for w in widths], repeatRows=1)
    t.setStyle(TableStyle(style))
    return t


def request_pdf(path, *, firm, deal, sponsor, deal_type, part_label, part_title, part_no, n_parts, requests, num,
                questions, stage_titles, contact, data_room, today, include_certification):
    footer = f"{deal}  |  Due Diligence Request List" + (f"  |  Part {part_no} of {n_parts}" if n_parts > 1 else "")
    doc = Doc(path, firm, firm, "Confidential", footer)
    story = []
    g = sum(r["priority"] == "gating" for r in requests)
    _cover(story, firm, "Due Diligence Request List", part_label, [
        ("Transaction", deal), ("Prepared for", sponsor), ("Deal type", deal_type),
        ("This part", f"{part_title}: {len(requests)} requests ({g} gating)" + (
            f", plus a {len(questions)}-question management questionnaire" if questions else "")),
        ("Date issued", today), ("Contact", contact or "[Name, email, phone]")])

    story.append(p("Instructions", "h1"))
    steps = [
        "Respond to every request. Where a request does not apply, write \"N/A\" in the response column with a "
        "one-line explanation. Where a document does not exist, say so; do not leave the item blank.",
        "Upload each document to the data room" + (f" ({data_room})" if data_room else "") +
        " in the workstream folder, with the request reference at the start of the file name "
        "(for example \"U-LEG-001 Certificate of formation.pdf\").",
        "Provide documents in their original form: issuer PDFs for bank statements, audits, confirmations, licenses "
        "and third-party reports; native Excel with formulas intact for models and schedules.",
        "We verify key documents directly with their issuers (banks, auditors, administrators, regulators, "
        "counterparties). Please return the signed authorizations with this part so we can.",
        "Upload a new version rather than replacing a document, with \"v2\" in the file name.",
        "Questions about any request should be sent to the contact above, quoting the request reference.",
    ]
    if n_parts > 1:
        steps.insert(0, f"This is Part {part_no} of {n_parts}. "
                        + ("We will issue the next part after this part has been reviewed and cleared."
                           if part_no < n_parts else "It is the final part."))
    story += [p(f"{i}.  {s}", "body") for i, s in enumerate(steps, 1)]
    story += [Spacer(1, 10), p("Priority of requests", "h2")]
    leg = Table([[_prio({"priority": "gating"}), p("Must be provided and verified for the transaction to proceed. "
                                                    "Cannot be waived.", "body")],
                 [_prio({"priority": "core"}), p("Required. Any exception must be agreed in writing.", "body")],
                 [_prio({"priority": "supporting"}), p("Requested. Tell us if it does not exist.", "body")]],
                colWidths=[1.0 * inch, 5.6 * inch])
    leg.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    story += [leg, PageBreak()]

    for st, title in stage_titles:
        rows = [r for r in requests if r.get("stage") == st]
        if not rows:
            continue
        story += [CondPageBreak(1.5 * inch), p(title, "h1"),
                  p(f"{len(rows)} requests, {sum(r['priority'] == 'gating' for r in rows)} gating.", "small"),
                  Spacer(1, 6), _request_table(rows, num), Spacer(1, 10)]

    if questions:
        story += [PageBreak(), p("Management Questionnaire", "h1"),
                  p("Please answer each question in writing, in a separate document referencing the question number, "
                    "before the management meeting. Attach support where a question asks for numbers.", "body"),
                  Spacer(1, 8)]
        for i, q in enumerate(questions, 1):
            box = Table([[""]], colWidths=[6.9 * inch], rowHeights=[0.55 * inch])
            box.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.4, RULE)]))
            story.append(KeepTogether([Paragraph(f"<b>{i}.</b>&nbsp; {escape(q['question'])} "
                                                 f"<font color='#5f6b78' size='7'>[{q['id']}]</font>", S["body"]),
                                       Spacer(1, 3), box, Spacer(1, 8)]))

    if include_certification:
        story += [PageBreak(), p("Certification and Authorization", "h1"),
                  p(f"The undersigned, on behalf of {sponsor} and each entity identified in its responses, certifies "
                    "that (1) the documents and information provided in response to this request list are true, "
                    "correct and complete in all material respects and are copies of the originals; (2) it will "
                    "promptly notify the recipient of any change that makes a response inaccurate or incomplete; and "
                    "(3) it authorizes the recipient and its agents to contact the issuers of any document provided "
                    "(including banks, auditors, administrators, custodians, regulators, landlords, customers and "
                    "counterparties) to verify it, and to obtain background, litigation, regulatory, sanctions and "
                    "credit reports on the entities and individuals named, subject to any separate individual "
                    "consents required by law.", "body"), Spacer(1, 30)]
        sig = Table([["", "", ""], [p("Signature", "small"), "", p("Date", "small")], ["", "", ""],
                     [p("Name and title", "small"), "", p("Entity", "small")]],
                    colWidths=[3.4 * inch, 0.4 * inch, 2.8 * inch], rowHeights=[0.45 * inch, 0.25 * inch,
                                                                                0.45 * inch, 0.25 * inch])
        sig.setStyle(TableStyle([("LINEBELOW", (0, 0), (0, 0), 0.6, colors.black),
                                 ("LINEBELOW", (2, 0), (2, 0), 0.6, colors.black),
                                 ("LINEBELOW", (0, 2), (0, 2), 0.6, colors.black),
                                 ("LINEBELOW", (2, 2), (2, 2), 0.6, colors.black)]))
        story.append(sig)
    doc.build(story)


def letter_pdf(path, *, firm, deal, sponsor, deal_type, today, parts, notes, contact, data_room):
    doc = Doc(path, firm, firm, "Confidential", f"{deal}  |  Cover letter")
    st = [p(firm, "firm"), Spacer(1, 4)]
    rule = Table([[""]], colWidths=[7.1 * inch], rowHeights=[2])
    rule.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), 1.2, NAVY)]))
    st += [rule, Spacer(1, 18), p(today, "body"), Spacer(1, 12), p(sponsor, "body"), Spacer(1, 14),
           Paragraph(f"<b>Re: {escape(deal)}: due diligence request list</b>", S["body"]), Spacer(1, 12),
           p("Dear [Name],", "body"), Spacer(1, 8),
           p(f"Thank you for the information provided to date. We have classified the transaction as {deal_type} "
             f"and enclose {'Part 1 of ' + str(len(parts)) + ' of ' if len(parts) > 1 else ''}our due diligence "
             "request list. Our process runs in the stages below; we issue each part once the previous part has been "
             "reviewed and cleared.", "body"), Spacer(1, 8)]
    rows = [[p("Part", "hdr"), p("Scope", "hdr"), p("Requests", "hdr"), p("Gating", "hdr")]]
    rows += [[p(str(i)), p(t), p(str(n)), p(str(g))] for i, (t, n, g) in enumerate(parts, 1)]
    t = Table(rows, colWidths=[0.5 * inch, 4.7 * inch, 0.9 * inch, 0.8 * inch])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("GRID", (0, 0), (-1, -1), 0.3, RULE),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    st += [t, Spacer(1, 10)]
    for para in notes:
        if para.startswith("- "):
            st.append(Paragraph("&bull;&nbsp; " + escape(para[2:]), ParagraphStyle("b", parent=S["body"],
                                                                                   leftIndent=12)))
        else:
            st += [Spacer(1, 4), p(para, "body")]
    st += [Spacer(1, 8),
           p("Items marked GATING must be satisfied for the transaction to proceed. We verify bank statements, "
             "confirmations, licenses and third-party reports directly with their issuers; this is standard for every "
             "transaction we review. The certification and authorization form is at the end of Part 1." +
             (f" Please upload documents to {data_room}." if data_room else ""), "body"), Spacer(1, 8),
           p("We are happy to walk through any of the requests on a call.", "body"), Spacer(1, 16),
           p("Sincerely,", "body"), Spacer(1, 30), p(contact or "[Name]", "body"), p(firm, "body")]
    doc.build([NextPageTemplate("body")] + st)


def checklist_pdf(path, *, firm, deal, deal_type, today, one_checks, kill_tests, requests, red_flags, metrics,
                  third_parties, questions, failure_cases, chapters, stage_titles):
    doc = Doc(path, firm, firm, "INTERNAL - DO NOT DISTRIBUTE", f"{deal}  |  Reviewer checklist", internal=True)
    story = []
    _cover(story, firm, "Reviewer Checklist", "Pass criteria, verification steps, kill tests and red flags", [
        ("Transaction", deal), ("Deal type", deal_type), ("Requests", str(len(requests))),
        ("Kill tests", str(len(kill_tests))), ("Red flags", str(len(red_flags))), ("Date", today)], internal=True)
    for name, oc in one_checks:
        story += [p(f"The one check: {name}", "h2"), p(oc, "body")]
    story += [p("Kill tests (any one triggered = decline)", "h1")]
    t = Table([[p(h, "hdr") for h in ["", "Ref", "Test", "Bible"]]] +
              [[Paragraph("[&nbsp;&nbsp;&nbsp;]", S["cell"]), p(k["id"]), p(k["test"]), p(k.get("ref"))] for k in kill_tests],
              colWidths=[0.35 * inch, 0.8 * inch, 5.3 * inch, 0.65 * inch], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), GATING), ("GRID", (0, 0), (-1, -1), 0.3, RULE),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story += [t, PageBreak(), p("Requests: pass criteria and independent verification", "h1")]
    for st, title in stage_titles:
        rows = [r for r in requests if r.get("stage") == st]
        if not rows:
            continue
        story.append(p(title, "h2"))
        for r in rows:
            data = [[Paragraph(f"<b>{r['id']}</b>&nbsp;&nbsp;", S["cell"]), _prio(r),
                     Paragraph(f"<b>{escape(r['request'])}</b>" + (" <i>(WEAK threshold)</i>" if r.get("weak") else ""),
                               S["cell"])]]
            for k, lab in (("why", "Why"), ("pass", "Pass"), ("fail", "Fail"), ("verify", "Verify"), ("ref", "Bible")):
                data.append(["", p(lab, "cellb"), p(r.get(k))])
            t = Table(data, colWidths=[0.85 * inch, 0.75 * inch, 5.5 * inch])
            t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (-1, 0), SHADE),
                                   ("BOX", (0, 0), (-1, -1), 0.3, RULE), ("TOPPADDING", (0, 0), (-1, -1), 2),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
            story += [KeepTogether(t), Spacer(1, 4)]
    story += [PageBreak(), p("Red flags", "h1")]
    t = Table([[p(h, "hdr") for h in ["", "Ref", "Red flag", "Check"]]] +
              [[Paragraph("[&nbsp;&nbsp;&nbsp;]", S["cell"]), p(f["id"]), p(f["flag"]), p(f.get("check"))] for f in red_flags],
              colWidths=[0.35 * inch, 0.8 * inch, 2.9 * inch, 3.05 * inch], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("GRID", (0, 0), (-1, -1), 0.3, RULE),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story += [t, PageBreak(), p("Benchmarks", "h1")]
    t = Table([[p(h, "hdr") for h in ["Metric", "Acceptable", "Source", ""]]] +
              [[p(m["metric"]), p(m.get("acceptable")), p(m.get("source")), p("WEAK" if m.get("weak") else "")]
               for m in metrics], colWidths=[1.8 * inch, 2.4 * inch, 2.4 * inch, 0.5 * inch], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("GRID", (0, 0), (-1, -1), 0.3, RULE),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story += [t, p("Third-party reports to commission", "h1")]
    t = Table([[p(h, "hdr") for h in ["Ref", "Report", "Provider", "Required"]]] +
              [[p(x["id"]), p(x["report"]), p(x.get("provider")), p(x.get("required_when"))] for x in third_parties],
              colWidths=[0.8 * inch, 2.0 * inch, 2.4 * inch, 1.9 * inch], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("GRID", (0, 0), (-1, -1), 0.3, RULE),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story += [t, PageBreak(), p("Hard questions: what a good answer looks like", "h1")]
    for q in questions:
        story += [KeepTogether([Paragraph(f"<b>{q['id']}</b>&nbsp; {escape(q['question'])}", S["body"]),
                                Paragraph(f"<font color='#14304f'>Good answer:</font> {escape(q.get('good_answer', ''))}",
                                          ParagraphStyle("ga", parent=S["cell"], leftIndent=14)), Spacer(1, 6)])]
    story += [PageBreak(), p("Failure cases this packet is built to catch", "h1")]
    for c in failure_cases:
        story += [KeepTogether([Paragraph(f"<b>{escape(str(c.get('case')))} ({escape(str(c.get('year', '')))})</b>",
                                          S["body"]), p(c.get("what_happened")),
                                Paragraph(f"<b>Check:</b> {escape(str(c.get('check', '')))}", S["cell"]),
                                Spacer(1, 6)])]
    story += [p("Read before reviewing", "h2")] + [p(f"references/{c}", "body") for c in chapters]
    doc.build(story)
