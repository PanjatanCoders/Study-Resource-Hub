from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "linux-commands-study-material.md"
HTML_OUT = ROOT / "linux-commands-study-material.html"


def flush_paragraph(paragraph_lines: list[str], out: list[str]) -> None:
    if not paragraph_lines:
        return
    text = " ".join(line.strip() for line in paragraph_lines).strip()
    if text:
        out.append(f"<p>{escape(text)}</p>")
    paragraph_lines.clear()


def flush_list(list_items: list[str], out: list[str]) -> None:
    if not list_items:
        return
    out.append("<ul>")
    for item in list_items:
        out.append(f"<li>{escape(item)}</li>")
    out.append("</ul>")
    list_items.clear()


def flush_table(table_rows: list[list[str]], out: list[str]) -> None:
    if not table_rows:
        return
    out.append('<table class="revision-table">')
    header = table_rows[0]
    out.append("<thead><tr>" + "".join(f"<th>{escape(cell)}</th>" for cell in header) + "</tr></thead>")
    body_rows = table_rows[1:]
    if body_rows:
        out.append("<tbody>")
        for row in body_rows:
            out.append("<tr>" + "".join(f"<td>{escape(cell)}</td>" for cell in row) + "</tr>")
        out.append("</tbody>")
    out.append("</table>")
    table_rows.clear()


def markdown_to_html(markdown: str) -> str:
    out: list[str] = []
    paragraph_lines: list[str] = []
    list_items: list[str] = []
    table_rows: list[list[str]] = []
    in_code = False
    code_lines: list[str] = []

    lines = markdown.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph(paragraph_lines, out)
            flush_list(list_items, out)
            flush_table(table_rows, out)
            if not in_code:
                in_code = True
                code_lines = []
            else:
                out.append("<pre><code>")
                out.append(escape("\n".join(code_lines)))
                out.append("</code></pre>")
                in_code = False
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not stripped:
            flush_paragraph(paragraph_lines, out)
            flush_list(list_items, out)
            flush_table(table_rows, out)
            i += 1
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph(paragraph_lines, out)
            flush_list(list_items, out)
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if set(cells) <= {"---", ""}:
                i += 1
                continue
            table_rows.append(cells)
            i += 1
            continue

        if stripped.startswith("- "):
            flush_paragraph(paragraph_lines, out)
            flush_table(table_rows, out)
            list_items.append(stripped[2:].strip())
            i += 1
            continue

        if stripped.startswith("# "):
            flush_paragraph(paragraph_lines, out)
            flush_list(list_items, out)
            flush_table(table_rows, out)
            out.append(f"<h1>{escape(stripped[2:].strip())}</h1>")
            i += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph(paragraph_lines, out)
            flush_list(list_items, out)
            flush_table(table_rows, out)
            out.append(f"<h2>{escape(stripped[3:].strip())}</h2>")
            i += 1
            continue

        paragraph_lines.append(line)
        i += 1

    flush_paragraph(paragraph_lines, out)
    flush_list(list_items, out)
    flush_table(table_rows, out)

    body = "\n".join(out)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Linux Commands Study Material</title>
  <style>
    :root {{
      --ink: #18212f;
      --muted: #5a6778;
      --accent: #0f6cbd;
      --paper: #ffffff;
      --panel: #f3f7fb;
      --line: #d5deea;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      margin: 0;
      font-family: "Segoe UI", Tahoma, sans-serif;
      color: var(--ink);
      background: var(--paper);
      line-height: 1.55;
      font-size: 11pt;
    }}
    main {{
      max-width: 900px;
      margin: 0 auto;
      padding: 36px 42px 54px;
    }}
    h1 {{
      font-size: 24pt;
      margin: 0 0 12px;
      color: var(--accent);
      border-bottom: 3px solid var(--accent);
      padding-bottom: 10px;
    }}
    h2 {{
      font-size: 15pt;
      margin: 24px 0 10px;
      color: var(--ink);
      background: linear-gradient(90deg, rgba(15,108,189,0.12), rgba(15,108,189,0));
      padding: 8px 10px;
      border-left: 4px solid var(--accent);
      page-break-after: avoid;
    }}
    p {{
      margin: 8px 0;
    }}
    ul {{
      margin: 8px 0 12px 20px;
      padding: 0;
    }}
    li {{
      margin: 4px 0;
    }}
    pre {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px 14px;
      overflow: hidden;
      white-space: pre-wrap;
      word-break: break-word;
      font-size: 10pt;
    }}
    code {{
      font-family: Consolas, "Courier New", monospace;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 18px;
      font-size: 10.5pt;
    }}
    th, td {{
      border: 1px solid var(--line);
      padding: 8px 10px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background: var(--panel);
    }}
    @page {{
      size: A4;
      margin: 16mm;
    }}
  </style>
</head>
<body>
  <main>
{body}
  </main>
</body>
</html>
"""


def main() -> None:
    markdown = SOURCE.read_text(encoding="utf-8")
    html = markdown_to_html(markdown)
    HTML_OUT.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
