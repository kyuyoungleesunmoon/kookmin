import win32com.client as win32
from win32com.client import constants
import os

# Word Application 생성
word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = False

try:
    # 템플릿 열기
    template_path = r'C:\국민대프로젝트\TII_Articles_Word_template_2025.doc'
    doc = word.Documents.Open(template_path)
    
    # 새 파일로 저장 (.docx 형식)
    new_path = r'C:\국민대프로젝트\IEEE_DPF_Paper_Final.docx'
    doc.SaveAs2(new_path, FileFormat=16)  # 16 = wdFormatXMLDocument (.docx)
    
    doc.Close()
    print('Template saved as .docx successfully!')
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
finally:
    word.Quit()
