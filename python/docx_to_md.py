import sys
import os
from markitdown import MarkItDown

def convert_docx_to_md(input_path, output_path=None):
    if not input_path.endswith('.docx'):
        raise ValueError("Input file must be a .docx file.")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    # Convert to Markdown
    md = MarkItDown(enable_plugins=False)
    result = md.convert(input_path)
    print(result.text_content)

    # Determine output path
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.md'

    # Write Markdown to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result.markdown)

    print(f"✅ Markdown file created at: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python docx_to_md.py <input_file.docx> [output_file.md]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_docx_to_md(input_file, output_file)
