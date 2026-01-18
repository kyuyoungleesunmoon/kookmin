import win32com.client
import os

def read_structure():
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    try:
        source_path = os.path.abspath(r'C:\국민대프로젝트\IEEE_DPF_논문_최종본.docx')
        doc = word.Documents.Open(source_path)
        
        print(f"Total Paragraphs: {doc.Paragraphs.Count}")
        for i in range(1, min(31, doc.Paragraphs.Count + 1)):
            para = doc.Paragraphs(i)
            txt = para.Range.Text.strip()
            style = para.Style
            print(f"[{i}] Style: {style} | Text: {txt[:50]}...")
            
        doc.Close(False)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        word.Quit()

if __name__ == "__main__":
    read_structure()
