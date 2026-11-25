"""Opening packet: a short, styled first-screen PDF (ReportLab).

The opening packet is what goes out with the first reply, before formal diligence. It asks what the deal is and
for a short list of documents, explains the process, and contains no placeholders, answer boxes or blank lines.

Content comes from a JSON spec that Claude writes per deal (see SKILL.md, "Opening packet"), with items taken from
the library (intake questions and screen-stage requests) and rewritten in plain language. Usage:

    python3 scripts/dd.py opening --spec spec.json --out Opening_Packet.pdf

Spec keys: title, subtitle, amount, prepared_for, prepared_by, date, theme ("navy"|"forest"|"slate"|"burgundy"),
intro [paras], steps [{name, desc}], questions {title, intro, groups:[{title, items:[{q, why, ref}]}]},
documents {title, intro, groups:[{title, items:[{doc, detail, why, ref, essential}]}]},
callout {title, items:[{title, text}]}, how_to_send [paras], closing [paras], confidentiality.
"""
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame, KeepTogether, NextPageTemplate,
                                PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle)

THEMES = {
    "navy": ("#14304f", "#c8a24a", "#eef2f7", "#5c6b7a"),
    "forest": ("#1d4636", "#c9a227", "#eef4f0", "#5a6b62"),
    "slate": ("#2b3440", "#d08a3c", "#f0f2f4", "#5e6873"),
    "burgundy": ("#5a1e2b", "#c9a227", "#f6eff1", "#6d5a5f"),
}
W, H = letter


def _styles(dark, accent, light, mute):
    base = dict(fontName="Helvetica", textColor=colors.HexColor("#1d232a"))
    return {
        "body": ParagraphStyle("body", fontSize=10, leading=14.5, **base),
        "lead": ParagraphStyle("lead", fontSize=11.5, leading=16.5, **base),
        "small": ParagraphStyle("small", fontName="Helvetica", fontSize=8.3, leading=11, textColor=mute),
        "why": ParagraphStyle("why", fontName="Helvetica-Oblique", fontSize=8.6, leading=11.5, textColor=mute),
        "q": ParagraphStyle("q", fontName="Helvetica-Bold", fontSize=10.2, leading=14,
                            textColor=colors.HexColor("#1d232a")),
        "doc": ParagraphStyle("doc", fontName="Helvetica-Bold", fontSize=10.2, leading=13.5,
                              textColor=colors.HexColor("#1d232a")),
        "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=20, leading=25, textColor=dark,
                             spaceAfter=6),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=dark,
                             spaceBefore=10, spaceAfter=6),
        "kicker": ParagraphStyle("kicker", fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=accent),
        "stepname": ParagraphStyle("stepname", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=dark,
                                   alignment=TA_CENTER),
        "stepdesc": ParagraphStyle("stepdesc", fontName="Helvetica", fontSize=8.2, leading=10.8, textColor=mute,
                                   alignment=TA_CENTER),
        "calloutT": ParagraphStyle("calloutT", fontName="Helvetica-Bold", fontSize=10, leading=13,
                                   textColor=colors.white),
        "calloutB": ParagraphStyle("calloutB", fontName="Helvetica", fontSize=9.4, leading=13,
                                   textColor=colors.white),
        "tag": ParagraphStyle("tag", fontName="Helvetica-Bold", fontSize=7, leading=9, textColor=colors.white,
                              alignment=TA_CENTER),
    }


class Badge(Flowable):
    """Filled circle with a number."""

    def __init__(self, n, color, size=0.3 * inch):
        super().__init__()
        self.n, self.color, self.size = n, color, size
        self.width = self.height = size

    def draw(self):
        c = self.canv
        c.setFillColor(self.color)
        c.circle(self.size / 2, self.size / 2, self.size / 2, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 9.5 if self.n < 10 else 8.5)
        c.drawCentredString(self.size / 2, self.size / 2 - 3.3, str(self.n))


class Timeline(Flowable):
    def __init__(self, steps, dark, accent, light, mute, st, width):
        super().__init__()
        self.steps, self.dark, self.accent, self.light, self.mute, self.st = steps, dark, accent, light, mute, st
        self.width, self.height = width, 1.55 * inch

    def draw(self):
        c, n = self.canv, len(self.steps)
        colw = self.width / n
        y = self.height - 0.25 * inch
        c.setStrokeColor(self.accent)
        c.setLineWidth(2)
        c.line(colw / 2, y, self.width - colw / 2, y)
        for i, s in enumerate(self.steps):
            x = colw * i + colw / 2
            c.setFillColor(self.dark if i == 0 else colors.white)
            c.setStrokeColor(self.dark)
            c.setLineWidth(2)
            c.circle(x, y, 0.17 * inch, stroke=1, fill=1)
            c.setFillColor(colors.white if i == 0 else self.dark)
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(x, y - 3.5, str(i + 1))
            for txt, style, top in ((s["name"], self.st["stepname"], 0.5), (s.get("desc", ""), self.st["stepdesc"], 0.78)):
                p = Paragraph(escape(txt), style)
                w, h = p.wrap(colw - 10, 1 * inch)
                p.drawOn(c, colw * i + 5, y - top * inch - h + 12)


def build(spec, out):
    dark, accent, light, mute = [colors.HexColor(x) for x in THEMES.get(spec.get("theme", "navy"), THEMES["navy"])]
    st = _styles(dark, accent, light, mute)
    title = spec.get("title", "Opening Due Diligence Packet")
    footer_left = spec.get("prepared_by", "")
    footer_mid = spec.get("subtitle", "")

    def cover(c, d):
        c.saveState()
        c.setFillColor(dark)
        c.rect(0, 0, W, H, fill=1, stroke=0)
        c.setFillColor(accent)
        c.rect(0.9 * inch, H - 1.25 * inch, 0.9 * inch, 4, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#ffffff"))
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(0.9 * inch, H - 1.05 * inch, (spec.get("kicker") or "CONFIDENTIAL").upper())
        c.setFont("Helvetica-Bold", 34)
        y = H - 3.1 * inch
        for line in _wrap(title, 22):
            c.drawString(0.9 * inch, y, line)
            y -= 40
        c.setFont("Helvetica", 15)
        c.setFillColor(colors.HexColor("#dfe6ee"))
        for line in _wrap(spec.get("subtitle", ""), 52):
            c.drawString(0.9 * inch, y - 6, line)
            y -= 21
        if spec.get("amount"):
            c.setFillColor(accent)
            c.roundRect(0.9 * inch, y - 0.95 * inch, 2.6 * inch, 0.62 * inch, 6, fill=1, stroke=0)
            c.setFillColor(dark)
            c.setFont("Helvetica-Bold", 22)
            c.drawString(1.08 * inch, y - 0.73 * inch, spec["amount"])
        c.setStrokeColor(colors.HexColor("#ffffff"))
        c.setLineWidth(0.4)
        c.line(0.9 * inch, 1.65 * inch, W - 0.9 * inch, 1.65 * inch)
        c.setFillColor(colors.HexColor("#dfe6ee"))
        rows = [("PREPARED FOR", spec.get("prepared_for", "")), ("PREPARED BY", spec.get("prepared_by", "")),
                ("DATE", spec.get("date", ""))]
        x = 0.9 * inch
        for k, v in rows:
            if not v:
                continue
            c.setFont("Helvetica-Bold", 7.5)
            c.setFillColor(accent)
            c.drawString(x, 1.35 * inch, k)
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.white)
            for j, line in enumerate(_wrap(v, 30)[:2]):
                c.drawString(x, 1.15 * inch - j * 13, line)
            x += 2.3 * inch
        c.restoreState()

    def body(c, d):
        c.saveState()
        c.setFillColor(dark)
        c.rect(0, H - 0.42 * inch, W, 0.42 * inch, fill=1, stroke=0)
        c.setFillColor(accent)
        c.rect(0, H - 0.46 * inch, W, 0.04 * inch, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(0.75 * inch, H - 0.27 * inch, title.upper())
        c.setFont("Helvetica", 8.5)
        c.drawRightString(W - 0.75 * inch, H - 0.27 * inch, footer_mid)
        c.setFillColor(mute)
        c.setFont("Helvetica", 7.8)
        c.drawString(0.75 * inch, 0.45 * inch, "Confidential" + (f"  |  {footer_left}" if footer_left else ""))
        c.drawRightString(W - 0.75 * inch, 0.45 * inch, f"{d.page}")
        c.restoreState()

    doc = BaseDocTemplate(str(out), pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                          topMargin=0.85 * inch, bottomMargin=0.75 * inch, title=title,
                          author=spec.get("prepared_by", ""), subject=spec.get("subtitle", ""))
    fr = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate("cover", [fr], onPage=cover), PageTemplate("body", [fr], onPage=body)])
    s = [NextPageTemplate("body"), PageBreak()]

    # Welcome
    s += [Paragraph("WELCOME", st["kicker"]), Paragraph(escape(spec.get("welcome_title", "Thanks for reaching out")),
                                                        st["h1"])]
    for i, para in enumerate(spec.get("intro", [])):
        s += [Paragraph(escape(para), st["lead"] if i == 0 else st["body"]), Spacer(1, 7)]
    if spec.get("steps"):
        s += [Spacer(1, 8), Paragraph("HOW THE PROCESS WORKS", st["kicker"]), Spacer(1, 10),
              Timeline(spec["steps"], dark, accent, light, mute, st, doc.width)]
    if spec.get("contents"):
        s += [Spacer(1, 8), Paragraph("IN THIS PACKET", st["kicker"]), Spacer(1, 6)]
        rows = [[Paragraph(f"<b>{escape(a)}</b>", st["body"]), Paragraph(escape(b), st["body"])]
                for a, b in spec["contents"]]
        t = Table(rows, colWidths=[1.9 * inch, doc.width - 1.9 * inch])
        t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#d5dbe1")),
                               ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 6),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
        s.append(t)

    def section_head(kicker, title_, intro):
        out_ = [PageBreak(), Paragraph(escape(kicker).upper(), st["kicker"]), Paragraph(escape(title_), st["h1"])]
        if intro:
            out_ += [Paragraph(escape(intro), st["body"]), Spacer(1, 6)]
        return out_

    # Questions
    q = spec.get("questions")
    if q:
        s += section_head(q.get("kicker", "Part A"), q["title"], q.get("intro"))
        n = 0
        for g in q["groups"]:
            head_ = Paragraph(escape(g["title"]), st["h2"])
            for j, it in enumerate(g["items"]):
                n += 1
                inner = [Paragraph(escape(it["q"]), st["q"])]
                if it.get("why"):
                    inner += [Spacer(1, 2), Paragraph("Why we ask: " + escape(it["why"]), st["why"])]
                t = Table([[Badge(n, dark), inner]], colWidths=[0.45 * inch, doc.width - 0.45 * inch])
                t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (0, 0), 0),
                                       ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 4),
                                       ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#e1e5ea"))]))
                s.append(KeepTogether([head_, t] if j == 0 else [t]))

    # Documents
    dd = spec.get("documents")
    if dd:
        s += section_head(dd.get("kicker", "Part B"), dd["title"], dd.get("intro"))
        legend = Table([[Paragraph("ESSENTIAL", st["tag"]), Paragraph("Needed before we can move forward.", st["small"]),
                         Paragraph("REQUESTED", st["tag"]), Paragraph("Send if you have it; tell us if you don't.",
                                                                      st["small"])]],
                       colWidths=[0.85 * inch, 2.4 * inch, 0.85 * inch, 2.8 * inch])
        legend.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), dark), ("BACKGROUND", (2, 0), (2, 0), mute),
                                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (1, 0), (1, 0), 6),
                                    ("LEFTPADDING", (3, 0), (3, 0), 6)]))
        s += [legend, Spacer(1, 4)]
        for g in dd["groups"]:
            head_ = Paragraph(escape(g["title"]), st["h2"])
            for j, it in enumerate(g["items"]):
                ess = it.get("essential", False)
                head = Table([[Paragraph(escape(it["doc"]), st["doc"]),
                               Paragraph("ESSENTIAL" if ess else "REQUESTED", st["tag"])]],
                             colWidths=[doc.width - 1.15 * inch, 0.8 * inch])
                head.setStyle(TableStyle([("BACKGROUND", (1, 0), (1, 0), dark if ess else mute),
                                          ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (0, 0), 0),
                                          ("TOPPADDING", (1, 0), (1, 0), 2), ("BOTTOMPADDING", (1, 0), (1, 0), 2)]))
                inner = [head]
                if it.get("detail"):
                    inner += [Spacer(1, 3), Paragraph(escape(it["detail"]), st["body"])]
                if it.get("why"):
                    inner += [Spacer(1, 3), Paragraph("Why we ask: " + escape(it["why"]), st["why"])]
                card = Table([[inner]], colWidths=[doc.width - 0.05 * inch])
                card.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), light),
                                          ("LINEBEFORE", (0, 0), (0, -1), 3.5, accent if ess else mute),
                                          ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                                          ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
                s += [KeepTogether([head_, card] if j == 0 else [card]), Spacer(1, 7)]

    # Callout
    co = spec.get("callout")
    if co:
        rows = [[Paragraph(escape(co["title"]).upper(), ParagraphStyle("ct", parent=st["kicker"],
                                                                        textColor=accent))]]
        for it in co["items"]:
            rows.append([[Paragraph(escape(it["title"]), st["calloutT"]), Spacer(1, 2),
                          Paragraph(escape(it["text"]), st["calloutB"])]])
        t = Table(rows, colWidths=[doc.width])
        t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), dark), ("LEFTPADDING", (0, 0), (-1, -1), 16),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 16), ("TOPPADDING", (0, 0), (-1, -1), 7),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (0, 0), 14),
                               ("BOTTOMPADDING", (0, -1), (-1, -1), 14)]))
        s += [PageBreak(), KeepTogether(t)]

    # How to send / closing
    if spec.get("how_to_send"):
        s += [Spacer(1, 16), Paragraph("HOW TO SEND", st["kicker"]),
              Paragraph(escape(spec.get("how_title", "Sending your answers and documents")), st["h2"])]
        for para in spec["how_to_send"]:
            if para.startswith("- "):
                s.append(Paragraph("&bull;&nbsp;&nbsp;" + escape(para[2:]),
                                   ParagraphStyle("bl", parent=st["body"], leftIndent=14, firstLineIndent=-9,
                                                  spaceAfter=3)))
            else:
                s += [Paragraph(escape(para), st["body"]), Spacer(1, 5)]
    if spec.get("closing"):
        s += [Spacer(1, 14), Paragraph("WHAT HAPPENS NEXT", st["kicker"]),
              Paragraph(escape(spec.get("closing_title", "After you send this")), st["h2"])]
        for para in spec["closing"]:
            s += [Paragraph(escape(para), st["body"]), Spacer(1, 5)]
    if spec.get("confidentiality"):
        box = Table([[Paragraph(escape(spec["confidentiality"]), st["small"])]], colWidths=[doc.width])
        box.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#c9d0d7")),
                                 ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                                 ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
        s += [Spacer(1, 18), KeepTogether(box)]
    doc.build(s)


def _wrap(text, n):
    words, lines, cur = (text or "").split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines
