import sys
from pathlib import Path
from markdown_it import MarkdownIt
from pygments.formatters import HtmlFormatter

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <file.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print("Markdown file not found")
        sys.exit(1)

    html_path = md_path.with_suffix(".html")
    
    # Clean up title: remove .md extension and format properly
    doc_title = md_path.stem.replace('_', ' ').replace('-', ' ')

    md = MarkdownIt("gfm-like", {"html": True})

    body = md.render(md_path.read_text(encoding="utf-8"))
    pygments_css = HtmlFormatter(style="friendly").get_style_defs("pre code")

    html = f"""<!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <title>{doc_title}</title>
            <style>
            /* Base Typography */
            body {{
                font-family: 'Segoe UI', 'SF Pro Display', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
                max-width: 850px;
                margin: 0 auto;
                padding: 50px 70px;
                background: #ffffff;
                color: #1a1a1a;
                line-height: 1.65;
                font-size: 14.5px;
            }}
            /* Headings - Alternating Colors */
            h1, h2, h3, h4, h5, h6 {{
                font-weight: 700;
                line-height: 1.25;
                margin-top: 1.8em;
                margin-bottom: 0.7em;
                letter-spacing: -0.03em;
            }}
            h1 {{
                font-size: 2.2em;
                margin-top: 0;
                padding-bottom: 0.35em;
                border-bottom: 4px solid #0066cc;
                color: #0066cc;
                text-transform: capitalize;
            }}
            h2 {{
                font-size: 1.65em;
                padding-bottom: 0.3em;
                padding-left: 12px;
                border-left: 5px solid #0066cc;
                margin-top: 1.8em;
                color: #0a0a0a;
                background: #f8f9fa;
                padding-top: 0.3em;
                padding-right: 12px;
                border-radius: 4px;
            }}
            h3 {{
                font-size: 1.35em;
                color: #0066cc;
                position: relative;
                padding-left: 20px;
            }}
            h3:before {{
                content: "▸";
                position: absolute;
                left: 0;
                color: #0066cc;
                font-weight: bold;
            }}
            h4 {{
                font-size: 1.15em;
                color: #0a0a0a;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                font-size: 0.95em;
            }}
            /* Paragraphs */
            p {{
                margin: 0.9em 0;
                text-align: justify;
                line-height: 1.7;
            }}
            /* Links */
            a {{
                color: #0066cc;
                text-decoration: none;
                border-bottom: 1.5px solid #0066cc60;
                transition: all 0.2s;
                font-weight: 500;
            }}
            a:hover {{
                border-bottom-color: #0066cc;
                background: #f0f7ff;
            }}
            /* Code Blocks */
            pre {{
                background: linear-gradient(135deg, #f8f9fa 0%, #f1f3f5 100%);
                padding: 16px 20px;
                border-radius: 6px;
                overflow-x: auto;
                border-left: 4px solid #0066cc;
                box-shadow: 0 1px 4px rgba(0,0,0,0.06);
                margin: 1.3em 0;
                font-size: 0.85em;
                position: relative;
            }}
            pre:before {{
                content: "";
                position: absolute;
                top: 0;
                right: 0;
                width: 40px;
                height: 40px;
                background: linear-gradient(135deg, transparent 50%, #0066cc15 50%);
                border-radius: 0 6px 0 0;
            }}
            pre code {{
                background: transparent;
                padding: 0;
                border-radius: 0;
                font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                line-height: 1.5;
            }}
            code {{
                background: linear-gradient(135deg, #fff5f5 0%, #ffe8e8 100%);
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                font-size: 0.88em;
                color: #c7254e;
                border: 1px solid #ffd0d0;
                font-weight: 500;
            }}
            /* Blockquotes */
            blockquote {{
                margin: 1.3em 0;
                padding: 0.9em 1.3em;
                border-left: 5px solid #0066cc;
                background: linear-gradient(135deg, #f8f9fa 0%, #f0f4f8 100%);
                font-style: italic;
                color: #3a3a3a;
                border-radius: 0 6px 6px 0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05);
                position: relative;
            }}
            blockquote:before {{
                content: '"';
                position: absolute;
                top: -10px;
                left: 10px;
                font-size: 3em;
                color: #0066cc30;
                font-family: Georgia, serif;
            }}
            blockquote p {{
                margin: 0.4em 0;
            }}
            /* Lists */
            ul, ol {{
                margin: 0.9em 0;
                padding-left: 1.8em;
            }}
            li {{
                margin: 0.4em 0;
                line-height: 1.65;
                position: relative;
            }}
            ul li:before {{
                content: "▸";
                color: #0066cc;
                font-weight: bold;
                position: absolute;
                left: -1.2em;
            }}
            ul {{
                list-style: none;
            }}
            ol {{
                list-style: decimal;
                counter-reset: item;
            }}
            ol li {{
                counter-increment: item;
            }}
            ol li:before {{
                display: none;
            }}
            strong {{
                color: #0a0a0a;
                font-weight: 700;
            }}
            em {{
                color: #2a2a2a;
                font-style: italic;
            }}
            /* Tables */
            table {{
                border-collapse: separate;
                border-spacing: 0;
                width: 100%;
                margin: 1.5em 0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                border-radius: 6px;
                overflow: hidden;
                font-size: 0.92em;
            }}
            th {{
                background: linear-gradient(135deg, #0066cc 0%, #0052a3 100%);
                color: white;
                padding: 11px 14px;
                text-align: left;
                font-weight: 600;
                letter-spacing: 0.03em;
                font-size: 0.9em;
                text-transform: uppercase;
            }}
            td {{
                border-bottom: 1px solid #e8e8e8;
                border-right: 1px solid #f0f0f0;
                padding: 10px 14px;
                background: white;
            }}
            td:last-child {{
                border-right: none;
            }}
            tr:nth-child(even) td {{
                background: #f8f9fa;
            }}
            tr:hover td {{
                background: #f0f7ff;
            }}
            tr:last-child td {{
                border-bottom: none;
            }}
            /* Horizontal Rule */
            hr {{
                border: none;
                height: 2px;
                background: linear-gradient(to right, transparent, #0066cc, transparent);
                margin: 2.5em 0;
                opacity: 0.3;
            }}
            /* Images */
            img {{
                max-width: 100%;
                height: auto;
                border-radius: 6px;
                box-shadow: 0 3px 12px rgba(0,0,0,0.12);
                margin: 1.3em 0;
                border: 1px solid #e8e8e8;
            }}
            /* Syntax Highlighting */
            {pygments_css}
            /* Print Styles */
            @media print {{
                body {{
                    padding: 30px;
                    font-size: 11pt;
                    line-height: 1.55;
                    max-width: 100%;
                }}
                
                h1 {{
                    font-size: 1.9em;
                    page-break-after: avoid;
                    color: #0066cc !important;
                }}
                
                h2 {{
                    font-size: 1.5em;
                    page-break-after: avoid;
                    page-break-inside: avoid;
                }}
                
                h3 {{
                    font-size: 1.25em;
                    page-break-after: avoid;
                }}
                
                h4 {{
                    font-size: 1.05em;
                    page-break-after: avoid;
                }}
                
                h1, h2, h3, h4, h5, h6 {{
                    page-break-inside: avoid;
                }}
                
                pre, blockquote, table {{
                    page-break-inside: avoid;
                }}
                
                img {{
                    page-break-inside: avoid;
                    page-break-after: avoid;
                }}
                
                a {{
                    color: #0066cc;
                    text-decoration: none;
                    border-bottom: none;
                }}
                
                a[href^="http"]:after {{
                    content: " (" attr(href) ")";
                    font-size: 0.75em;
                    color: #666;
                }}
                
                pre {{
                    box-shadow: none;
                    border: 1px solid #ccc;
                    overflow: visible !important;
                    overflow-x: visible !important;
                    overflow-y: visible !important;
                    white-space: pre-wrap !important;
                    word-break: break-word !important;
                    overflow-wrap: anywhere;
                }}
                
                pre:before {{
                    display: none;
                }}
                
                pre code {{
                    white-space: pre-wrap !important;
                    word-break: break-word !important;
                    overflow-wrap: anywhere;
                }}
                
                table {{
                    box-shadow: none;
                    font-size: 0.9em;
                }}
                
                blockquote:before {{
                    display: none;
                }}
                
                ul li:before, ol li:before {{
                    color: #333;
                }}
                
                @page {{
                    margin: 1.8cm;
                }}
            }}
            </style>
            </head>
            <body>
            {body}
            </body>
            </html>
            """

    html_path.write_text(html, encoding="utf-8")
    print(f"HTML generated: {html_path}")
    print("Open in browser → Ctrl+P → Save as PDF")

if __name__ == "__main__":
    main()
