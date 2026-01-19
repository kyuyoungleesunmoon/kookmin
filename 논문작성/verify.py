# -*- coding: utf-8 -*-
from docx import Document
import re

doc = Document(r'c:\1.이규영개인폴더\09.##### SCHOOL #####\논문작성\IEEE_DPF_Paper_Final_v5.docx')

print('=' * 60)
print('최종 검증')
print('=' * 60)

code_issues = []
for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    if not text or len(text) > 150:
        continue
    
    patterns = [
        r'^[a-z_]+\s*=\s*[\d\.\{\[\'\"]',
        r'^[a-z_]+:\s*[\d\.]+',
        r'^model\s*=',
    ]
    
    for p in patterns:
        if re.match(p, text):
            code_issues.append((i, text[:60]))
            break

if code_issues:
    print(f'잔존 코드: {len(code_issues)}건')
    for idx, text in code_issues[:10]:
        print(f'  [{idx}] {text}')
else:
    print('코드 패턴: 0건')

print()
print('=' * 60)
