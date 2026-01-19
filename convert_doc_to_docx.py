# -*- coding: utf-8 -*-
"""
.doc 파일을 .docx로 변환 후 Markdown으로 변환하는 스크립트
"""

import os
import win32com.client
import time
from pathlib import Path

BASE_DIR = r"c:\1.이규영개인폴더\09.##### SCHOOL #####"
OUTPUT_DIR = os.path.join(BASE_DIR, "converted_md")
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")

def convert_doc_to_docx(doc_path):
    """Word COM을 사용하여 .doc를 .docx로 변환"""
    print(f"📄 Converting .doc to .docx: {doc_path}")
    
    word = None
    doc = None
    
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        word.DisplayAlerts = False
        
        # .doc 파일 열기
        doc = word.Documents.Open(doc_path)
        
        # .docx로 저장 (16 = wdFormatXMLDocument)
        docx_path = doc_path + "x"
        doc.SaveAs2(docx_path, FileFormat=16)
        
        print(f"  ✅ Converted to: {docx_path}")
        return docx_path
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None
    finally:
        if doc:
            doc.Close(SaveChanges=False)
        if word:
            word.Quit()

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("📁 DOC to DOCX Converter")
    print("=" * 60)
    
    # .doc 파일 경로
    doc_file = os.path.join(BASE_DIR, "IEEE_TII_Template", "TII_Articles_Word_template_2025.doc")
    
    if os.path.exists(doc_file):
        docx_path = convert_doc_to_docx(doc_file)
        if docx_path:
            print(f"\n✅ DOC converted to DOCX successfully!")
            print(f"📁 Output: {docx_path}")
    else:
        print(f"⚠️ File not found: {doc_file}")

if __name__ == "__main__":
    main()
