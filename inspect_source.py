import win32com.client
import os

def inspect_doc():
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    
    try:
        source_path = os.path.abspath(r'C:\국민대프로젝트\IEEE_DPF_논문_최종본.docx')
        doc = word.Documents.Open(source_path)
        
        print(f"File: {source_path}")
        print(f"Tables: {doc.Tables.Count}")
        for i in range(1, doc.Tables.Count + 1):
            try:
                # Get first cell text as a hint
                txt = doc.Tables(i).Cell(1, 1).Range.Text.strip()
                print(f"  Table {i}: {txt[:50]}...")
            except:
                print(f"  Table {i}: <Error reading cell>")

        print(f"InlineShapes (Images): {doc.InlineShapes.Count}")
        print(f"Shapes (Images): {doc.Shapes.Count}")
        
        doc.Close(False)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        word.Quit()

if __name__ == "__main__":
    inspect_doc()
