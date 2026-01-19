from docx import Document
import zipfile
import os
import re

print('='*60)
print('Word 수식 메뉴 비활성화 원인 분석')
print('='*60)

file_path = r'IEEE_DPF_Paper_Corrected.docx'

# 1. 파일 존재 확인
print(f'\n1. 파일 확인')
print(f'   파일: {file_path}')
print(f'   존재: {os.path.exists(file_path)}')
print(f'   크기: {os.path.getsize(file_path):,} bytes')

# 2. DOCX 내부 구조 확인
print(f'\n2. 문서 내부 구조 확인')

with zipfile.ZipFile(file_path, 'r') as zip_ref:
    file_list = zip_ref.namelist()
    
    # 핵심 파일 확인
    core_files = ['word/document.xml', 'word/styles.xml', '[Content_Types].xml']
    for cf in core_files:
        exists = cf in file_list
        print(f'   {cf}: {"✓" if exists else "✗"}')
    
    # settings.xml 확인 (호환 모드 정보)
    if 'word/settings.xml' in file_list:
        settings_content = zip_ref.read('word/settings.xml').decode('utf-8')
        
        # 호환 모드 확인
        print(f'\n3. 호환성 모드 확인')
        
        if 'compatibilityMode' in settings_content:
            # compatibilityMode 값 추출
            compat_section = settings_content[settings_content.find('compatibilityMode'):settings_content.find('compatibilityMode')+100]
            match = re.search(r'w:val="(\d+)"', compat_section)
            
            if match:
                compat_mode = int(match.group(1))
                print(f'   compatibilityMode 값: {compat_mode}')
                
                mode_names = {
                    11: 'Word 2003',
                    12: 'Word 2007',
                    14: 'Word 2010',
                    15: 'Word 2013/2016/2019/365'
                }
                mode_name = mode_names.get(compat_mode, f'알 수 없음')
                print(f'   해당 버전: {mode_name}')
                
                if compat_mode < 14:
                    print(f'\n   ⚠️ 문제 발견!')
                    print(f'   호환 모드가 Word 2007 이전으로 설정되어 있습니다.')
                    print(f'   이 경우 수식 메뉴가 비활성화됩니다.')
                    print(f'\n   해결 방법:')
                    print(f'   1. 파일 > 정보 > 변환 클릭')
                    print(f'   2. 또는 다른 이름으로 저장 > .docx 형식 선택')
                elif compat_mode == 14:
                    print(f'\n   ⚠️ Word 2010 호환 모드')
                    print(f'   일부 수식 기능이 제한될 수 있습니다.')
                else:
                    print(f'   ✓ 호환 모드 정상')
            else:
                print(f'   값을 찾을 수 없음')
        else:
            print(f'   compatibilityMode 설정 없음 (기본값 사용)')
        
        # 문서 보호 확인
        print(f'\n4. 문서 보호 확인')
        if 'documentProtection' in settings_content:
            print(f'   ⚠️ 문서 보호가 활성화되어 있습니다!')
            print(f'   수식 입력이 제한될 수 있습니다.')
        else:
            print(f'   ✓ 문서 보호 없음')
        
        # 읽기 전용 확인
        if 'readOnlyRecommended' in settings_content:
            print(f'   ⚠️ 읽기 전용 권장 설정됨')

# 4. Content_Types 확인
print(f'\n5. 수식 관련 Content Type 확인')
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    content_types = zip_ref.read('[Content_Types].xml').decode('utf-8')
    
    if 'math' in content_types.lower():
        print(f'   ✓ 수식 Content Type 존재')
    else:
        print(f'   수식 Content Type 없음 (아직 수식이 없는 문서)')

# 5. 원본 템플릿 비교
print(f'\n6. 원본 템플릿 호환성 모드 확인')
template_path = r'C:\1.이규영개인폴더\09.##### SCHOOL #####\IEEE_TII_Template\TII_Articles_Word_template_2025.docx'

if os.path.exists(template_path):
    with zipfile.ZipFile(template_path, 'r') as zip_ref:
        if 'word/settings.xml' in zip_ref.namelist():
            template_settings = zip_ref.read('word/settings.xml').decode('utf-8')
            
            if 'compatibilityMode' in template_settings:
                compat_section = template_settings[template_settings.find('compatibilityMode'):template_settings.find('compatibilityMode')+100]
                match = re.search(r'w:val="(\d+)"', compat_section)
                if match:
                    print(f'   템플릿 compatibilityMode: {match.group(1)}')

print(f'\n' + '='*60)
print('결론 및 해결 방법')
print('='*60)

print('''
Word에서 수식 메뉴가 비활성화되는 주요 원인:

1. 호환 모드 문제 (가장 흔함)
   - 문서가 .doc 형식이거나 이전 버전 호환 모드일 때
   - 해결: 파일 > 정보 > "변환" 버튼 클릭

2. 문서 보호
   - 편집 제한이 걸려 있을 때
   - 해결: 검토 > 편집 제한 > 보호 중지

3. 제한된 편집 모드
   - 특정 영역만 편집 가능할 때
   - 해결: 검토 > 편집 제한 해제

4. 추가 기능 충돌
   - 일부 추가 기능이 수식 기능과 충돌
   - 해결: 파일 > 옵션 > 추가 기능 > COM 추가 기능 비활성화
''')
