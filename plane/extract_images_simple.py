import zipfile
import os

# 설정
docx_path = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\논문작성\이규영 국민대 DPF 논문.docx"
output_dir = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md\images_recovered"

# 출력 디렉토리 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        # word/media/ 폴더 내 파일 찾기
        media_files = [f for f in zip_ref.namelist() if f.startswith('word/media/')]
        
        print(f"총 {len(media_files)}개의 이미지 파일을 발견했습니다.")
        
        for file in media_files:
            # 파일명만 추출 (경로 제외)
            filename = os.path.basename(file)
            if not filename:
                continue
            
            # 대상 경로
            target_path = os.path.join(output_dir, filename)
            
            # 파일 추출 및 쓰기
            with zip_ref.open(file) as source, open(target_path, "wb") as target:
                target.write(source.read())
            
            print(f"복구됨: {filename}")

    print("\n모든 이미지 추출이 완료되었습니다.")
    print(f"저장 경로: {output_dir}")

except FileNotFoundError:
    print(f"오류: 파일을 찾을 수 없습니다 - {docx_path}")
except zipfile.BadZipFile:
    print(f"오류: 유효한 docx(zip) 파일이 아닙니다 - {docx_path}")
except Exception as e:
    print(f"알 수 없는 오류 발생: {e}")
