import docx
from .utils import find_links


def scan_docx(file_path):
    doc = docx.Document(file_path)
    text = " ".join([paragraph.text for paragraph in doc.paragraphs])
    links = find_links(text)

    print(f"\nDOCX Analysis Report for {file_path}")
    print("Extracted Links:")
    if links:
        for link in links:
            print(f"- {link}")
    else:
        print("No links found.")
    return links
