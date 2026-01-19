from docx import Document
import re

def analyze_structure(file_path):
    print(f"Analyzing: {file_path}")
    try:
        doc = Document(file_path)
        
        current_section = "Start"
        section_counts = {"Start": 0}
        
        for p in doc.paragraphs:
            text = p.text.strip()
            if not text:
                continue
                
            # Check for Roman Numeral Headings
            match = re.match(r'^(I|II|III|IV|V|VI|VII|VIII|IX|X)\.?\s', text)
            if match:
                current_section = text[:20]  # Capture start of heading
                section_counts[current_section] = 0
                # print(f"\n[SECTION FOUND] {text}")
            else:
                section_counts[current_section] += 1
                     
        print("\nSummary of Content per Section:")
        for sec, count in section_counts.items():
            print(f"  {sec}: {count} paragraphs")
            
    except Exception as e:
        print(f"Error: {e}")

print("--- Checking Other Candidates ---")
analyze_structure(r"C:\국민대프로젝트\논문작성\IEEE_DPF_Paper_한글최종본.docx")
analyze_structure(r"C:\국민대프로젝트\논문작성\IEEE_DPF_Paper_TII_Compliant.docx")
