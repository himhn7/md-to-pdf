import sys
import webbrowser
from pathlib import Path
from markdown_it import MarkdownIt
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

SCRIPT_DIR = Path(__file__).parent
STYLE_CSS = SCRIPT_DIR / "style.css"
OUTPUT_DIR = SCRIPT_DIR / "output"


def highlight_code(code, lang, _attrs):
    """Syntax-highlight a fenced code block using Pygments."""
    try:
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
        else:
            lexer = guess_lexer(code)
    except ClassNotFound:
        return ""  # fall back to default rendering

    formatter = HtmlFormatter(nowrap=True)
    return f'<pre><code class="highlight">{highlight(code, lexer, formatter)}</code></pre>'


def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <file.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"Markdown file not found: {md_path}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(exist_ok=True)
    html_path = OUTPUT_DIR / md_path.with_suffix(".html").name

    doc_title = md_path.stem.replace('_', ' ').replace('-', ' ')

    md = MarkdownIt("gfm-like", {"html": True, "highlight": highlight_code})

    body = md.render(md_path.read_text(encoding="utf-8"))

    pygments_css = HtmlFormatter(style="friendly").get_style_defs(".highlight")
    base_css = STYLE_CSS.read_text(encoding="utf-8")

    html = f"""<!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <title>{doc_title}</title>
            <style>
            {base_css}
            /* Syntax Highlighting */
            {pygments_css}
            </style>
            </head>
            <body>
            {body}
            </body>
            </html>
            """

    html_path.write_text(html, encoding="utf-8")
    print(f"HTML generated: {html_path}")

    webbrowser.open(html_path.resolve().as_uri())


if __name__ == "__main__":
    main()
