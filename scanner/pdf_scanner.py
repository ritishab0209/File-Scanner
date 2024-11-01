import fitz  # PyMuPDF
from .utils import find_links

def scan_pdf(file_path):
    with fitz.open(file_path) as pdf:
        text = ""
        for page in pdf:
            text += page.get_text()
        links = find_links(text)
        
        print(f"\nPDF Analysis Report for {file_path}")
        print("Extracted Links:")
        if links:
            for link in links:
                print(f"- {link}")
        else:
            print("No links found.")
    return links
