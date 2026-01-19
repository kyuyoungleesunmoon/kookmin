from docx import Document
import zipfile
import os
import shutil
import re

print('='*60)
print('호환성 모드 업그레이드 (Word 2003 → Word 2016)')
print('='*60)

input_path = r'IEEE_DPF_Paper_Corrected.docx'
output_path = r'IEEE_DPF_Paper_Modern.docx'
temp_dir = r'temp_docx_upgrade'

# 1. 임시 폴더 생성
print(f'\n1. 문서 압축 해제...')
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
os.makedirs(temp_dir)

with zipfile.ZipFile(input_path, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)
print(f'   ✓ 완료')

# 2. settings.xml 수정
print(f'\n2. 호환성 모드 업데이트...')
settings_path = os.path.join(temp_dir, 'word', 'settings.xml')

with open(settings_path, 'r', encoding='utf-8') as f:
    settings_content = f.read()

# compatibilityMode 값을 15로 변경 (Word 2013/2016/2019/365)
original_mode = re.search(r'<w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="(\d+)"/>', settings_content)

if original_mode:
    old_val = original_mode.group(1)
    print(f'   이전 값: {old_val} (Word 2003)')
    
    # 값을 15로 변경
    settings_content = settings_content.replace(
        f'w:val="{old_val}"',
        'w:val="15"',
        1  # 첫 번째만 변경
    )
    print(f'   새 값: 15 (Word 2016+)')
else:
    print(f'   compatibilityMode를 찾을 수 없음')

with open(settings_path, 'w', encoding='utf-8') as f:
    f.write(settings_content)
print(f'   ✓ settings.xml 업데이트 완료')

# 3. 다시 압축
print(f'\n3. 문서 재압축...')

with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, temp_dir)
            zipf.write(file_path, arcname)

print(f'   ✓ 완료')

# 4. 임시 폴더 삭제
shutil.rmtree(temp_dir)

# 5. 검증
print(f'\n4. 검증...')
with zipfile.ZipFile(output_path, 'r') as zip_ref:
    new_settings = zip_ref.read('word/settings.xml').decode('utf-8')
    if 'w:val="15"' in new_settings:
        print(f'   ✓ 호환성 모드 업데이트 확인됨')
    else:
        print(f'   ⚠️ 업데이트 확인 필요')

print(f'\n' + '='*60)
print(f'✅ 완료!')
print(f'='*60)

print(f'\n새 파일: {output_path}')
print(f'\n이 파일을 열면 수식 메뉴가 활성화됩니다!')
print(f'\n참고: 원본 파일은 그대로 유지됩니다.')
