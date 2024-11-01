from scanner.pdf_scanner import scan_pdf
from scanner.docx_scanner import scan_docx
from scanner.link_analyzer import check_url_malicious

def scan_file(file_path):
    links = []
    if file_path.endswith(".pdf"):
        links = scan_pdf(file_path)
    elif file_path.endswith(".docx"):
        links = scan_docx(file_path)
    else:
        print("Unsupported file type.")
    
    if links:
        print("\nLink Analysis Report:")
        for link in links:
            result = check_url_malicious(link)
            print(f"- {link}: {result}")

if __name__ == "__main__":
    # Example file path; replace this with the path to your document
    file_path = "sample.pdf"  # Or "sample.docx"
    scan_file(file_path)
