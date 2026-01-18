# 국민대 프로젝트 - IEEE DPF 논문 자동화

이 저장소는 IEEE 논문 형식 변환 및 자동화를 위한 스크립트와 결과물을 포함합니다.

## 주요 기능
- **포맷 변환**: `finalize_paper_v6.py`를 통해 원본 DOCX 파일을 IEEE 템플릿에 맞게 자동 변환
- **다이어그램 생성**: `create_architecture_diagram.py` (영문/한글) 로 아키텍처 흐름도 생성
- **이미지 자동 삽입**: 실험 결과 이미지 자동 추출 및 배치

## 실행 방법
```bash
python finalize_paper_v6.py
```

## 파일 구조
- `IEEE_DPF_Paper_Korean_Final_Rev4.docx`: 최종 완성된 논문 파일
- `finalize_paper_v6.py`: 최종 변환 스크립트
- `create_korean_diagram.py`: 한글 아키텍처 다이어그램 생성 코드
