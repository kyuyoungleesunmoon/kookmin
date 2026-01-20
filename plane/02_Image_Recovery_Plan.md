# 이미지 복구 및 논문 정제 재실행 계획 (Image Recovery Plan)

**일자:** 2026-01-20  
**작성자:** Antigravity  
**목표:** 실수로 삭제된 논문 이미지를 원본 Word 파일에서 복구하고, 정제된 논문 파일(`IEEE_DPF_Paper_Refined.md`)과 올바르게 연결한다.

---

## 1. 상황 분석
- **문제:** 사용자가 이미지 파일 삭제를 보고함. 현재 `converted_md/images` 폴더에는 파일이 존재하나, 링크 불일치 또는 실제 파일 손상 가능성 대비 필요.
- **소스:** `c:\1.이규영개인폴더\09.##### SCHOOL #####\논문작성\이규영 국민대 DPF 논문.docx`
- **타겟:** `c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md\images_recovered\` (임시 폴더 사용 안전 확보)

## 2. 복구 전략
이미지 파일명(`img_0.png` 등)과 실제 이미지 간의 매핑을 보장하기 위해, 단순 압축 해제가 아닌 **문서 내 등장 순서**에 따른 추출을 수행한다.

### 단계 1: 이미지 추출 스크립트 실행
- **도구:** Python (`python-docx`, `docx` 라이브러리 활용)
- **로직:**
  1. Word 문서를 파싱하여 본문 내 이미지(`inline_shapes`, `blips`)를 순서대로 탐색.
  2. 이미지를 `extracted_image_1.png`, `extracted_image_2.png` 와 같이 순차적 이름으로 저장.
  3. `images_recovered` 폴더에 저장.

### 단계 2: 논문 파일 링크 수정
- **대상:** `IEEE_DPF_Paper_Refined.md`
- **작업:**
  - 기존 이미지 링크(예: `images/이규영_국민대_DPF_논문_img_0.png`)를 새로 추출된 파일명(예: `images/extracted_image_1.png`)으로 일괄 변경.
  - Figure 번호와 이미지 순서가 일치하는지 확인.

### 단계 3: 파일 정리 및 확인
- 복구된 이미지를 `images` 폴더로 이동(또는 경로 변경).
- 사용자가 결과물 확인 후 `Refined.md`를 최종 확정.

## 3. 실행 계획
1. `recover_images.py` 스크립트 작성 및 실행.
2. 추출 결과 확인.
3. `IEEE_DPF_Paper_Refined.md` 내 이미지 경로 업데이트.
4. 사용자에게 완료 보고 및 검토 요청.
