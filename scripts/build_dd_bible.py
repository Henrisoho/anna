#!/usr/bin/env python3
"""Assemble The Bible on Due Diligence v2 from research/due-diligence/v2/*.md.

Splits every part file on top-level '# ' chapter headings, orders chapters
(front matter, 0..18 with 6A after 6, then appendices), appends a consolidated
source list (every URL cited, de-duplicated) and writes:
  research/due-diligence/bible_v2.md
  research/due-diligence/bible_v2.html  (pandoc, with TOC)
  research/due-diligence/bible_v2.pdf   (Chromium print via Playwright, if available)
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "research" / "due-diligence"
PARTS = sorted((ROOT / "v2").glob("*.md"))


def chapter_key(title: str):
    m = re.match(r"#\s+(?:Chapter\s+)?(\d+)([A-Z]?)\b", title)
    if m:
        return (1, int(m.group(1)), m.group(2))
    m = re.match(r"#\s+Appendix\s+([A-Z])", title, re.I)
    if m:
        return (2, ord(m.group(1).upper()), "")
    return (0, 0, "")  # front matter


chapters = []  # (key, order, text)
front = []
for i, part in enumerate(PARTS):
    text = part.read_text().replace("<!-- APPENDICES -->", "")
    blocks = re.split(r"(?m)^(?=# )", text)
    for j, b in enumerate(blocks):
        if not b.strip():
            continue
        first = b.lstrip().splitlines()[0]
        key = chapter_key(first) if first.startswith("# ") else (0, 0, "")
        if key[0] == 0:
            front.append((i, j, b.strip()))
        else:
            chapters.append((key, (i, j), b.strip()))

chapters.sort(key=lambda c: (c[0], c[1]))
body = "\n\n".join([f[2] for f in sorted(front)] + [c[2] for c in chapters])

# Consolidated sources: every URL cited anywhere, in order of first appearance.
urls = []
seen = set()
for u in re.findall(r"https?://[^\s)\]>\"'`]+", body):
    u = u.rstrip(".,;:")
    if u not in seen:
        seen.add(u)
        urls.append(u)
sources = "# Appendix C Sources\n\nEvery URL cited in this volume, in order of first citation.\n\n" + "\n".join(
    f"{n}. <{u}>" for n, u in enumerate(urls, 1)
)

header = """---
title: "The Bible on Due Diligence"
subtitle: "How to build, check, and attack a private market deal at the depth of an institutional data room. Version 2.0"
---

"""
md = header + body + "\n\n" + sources + "\n"
out_md = ROOT / "bible_v2.md"
out_md.write_text(md)
print(f"wrote {out_md} ({len(md.split()):,} words, {len(chapters)} chapters, {len(urls)} sources)")

css = ROOT / "v2_style.css"
css.write_text("""
body{font-family:Georgia,serif;max-width:52em;margin:2em auto;line-height:1.45;font-size:10.5pt;color:#111}
h1{page-break-before:always;border-bottom:2px solid #333;padding-bottom:.2em}
h1.title{page-break-before:avoid;font-size:2.4em}
h2{margin-top:1.4em;color:#1a3a5a}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.92em}
th,td{border:1px solid #bbb;padding:4px 6px;vertical-align:top}
th{background:#eef2f6}
code{font-size:.9em}
a{color:#1a4f8a;word-break:break-all}
nav#TOC{page-break-after:always}
blockquote{border-left:4px solid #1a3a5a;margin-left:0;padding-left:1em;background:#f5f7fa}
""")
out_html = ROOT / "bible_v2.html"
subprocess.run(["pandoc", str(out_md), "-s", "--toc", "--toc-depth=2", "-c", css.name,
                "--embed-resources", "--metadata", "lang=en", "-o", str(out_html)],
               check=True, cwd=ROOT)
print(f"wrote {out_html}")

pdf = ROOT / "bible_v2.pdf"
js = f"""
const {{chromium}} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const pg = await b.newPage();
  await pg.goto({str(out_html.as_uri())!r});
  await pg.pdf({{path: {str(pdf)!r}, format: 'Letter', printBackground: true,
    margin: {{top: '0.7in', bottom: '0.7in', left: '0.7in', right: '0.7in'}},
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center">The Bible on Due Diligence v2.0 · <span class="pageNumber"></span></div>'}});
  await b.close();
}})();
"""
r = subprocess.run(["node", "-e", js])
print(f"wrote {pdf}" if r.returncode == 0 else "PDF step failed", file=sys.stderr if r.returncode else sys.stdout)
