
import fitz # PyMuPDF
import os

pdf_path = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\001_imgprocessing\X선_최종보고서.pdf"
output_path = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\plane\extracted_pdf_content.txt"

def extract_pdf_content():
    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found at {pdf_path}")
        return

    try:
        doc = fitz.open(pdf_path)
        full_text = []
        
        for page_num, page in enumerate(doc):
            text = page.get_text()
            full_text.append(f"--- Page {page_num + 1} ---\n{text}\n")
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(full_text))
            
        print(f"Successfully extracted content to {output_path}")
        print(f"Total pages: {len(doc)}")
        
    except Exception as e:
        print(f"Extraction failed: {e}")

if __name__ == "__main__":
    extract_pdf_content()
