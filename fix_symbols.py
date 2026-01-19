# -*- coding: utf-8 -*-
"""
IEEE 논문에서 AI 톤으로 의심받는 기호(✓, ✗)를 서술형으로 변환
"""
import zipfile
import os
import shutil

def fix_document():
    src = r'논문작성\IEEE_DPF_Paper_Final_v4.docx'
    dst = r'논문작성\IEEE_DPF_Paper_Final_Fixed.docx'
    
    temp_dir = r'논문작성\temp_docx_fix'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    # 압축 해제
    with zipfile.ZipFile(src, 'r') as z:
        z.extractall(temp_dir)
    
    # document.xml 읽기
    doc_path = os.path.join(temp_dir, 'word', 'document.xml')
    with open(doc_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 변환 전 기호 수
    check_chars = ['✓', '✔', '✗', '✘']
    before_count = sum(content.count(c) for c in check_chars)
    print(f'변환 전 기호 수: {before_count}')
    
    # 기호 변환 (순서 중요)
    replacements = [
        # 표 평가 항목 (공백 포함)
        ('✓✓✓ 초과 달성', '목표 초과 달성'),
        ('✓✓✓ 기준 충족', '기준 충족(우수)'),
        ('✓✓✓ 매우 빠름', '매우 빠름'),
        ('✓✓✓ 우수', '매우 우수'),
        ('✓✓ 기준 충족', '기준 충족'),
        ('✓✓ 우수', '우수'),
        ('✓✓ 합리적', '합리적'),
        # 남은 기호들
        ('✓✓✓', ''),
        ('✓✓', ''),
        ('✓', ''),
        ('✗', ''),
        ('✔', ''),
        ('✘', ''),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    # 변환 후 기호 수
    after_count = sum(content.count(c) for c in check_chars)
    print(f'변환 후 기호 수: {after_count}')
    
    # 저장
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # 새 docx로 압축
    if os.path.exists(dst):
        os.remove(dst)
    
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arcname)
    
    # 정리
    shutil.rmtree(temp_dir)
    
    if after_count == 0:
        print('\n✅ 성공! 모든 기호가 서술형으로 변환되었습니다.')
    else:
        print(f'\n⚠️ {after_count}개의 기호가 남아있습니다.')
    
    print(f'\n결과 파일: {os.path.abspath(dst)}')

if __name__ == '__main__':
    os.chdir(r'C:\국민대프로젝트')
    fix_document()
