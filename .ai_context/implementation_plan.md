# 논문 이미지(img_4) 폰트 크기 최적화

## 배경
`이규영_국민대_DPF_논문_img_4.png`는 Word 문서에서 추출된 원본 이미지로, 기존 Python 스크립트에서 생성된 것이 아닙니다. 이미지는 **2-panel 구성**입니다:
- **왼쪽:** DPF Multiclass Training Performance (mAP50 vs Epoch 곡선)
- **오른쪽:** Final Performance Metrics (Precision, Recall, mAP50, mAP50-95 바 차트)

현재 폰트가 작아서 논문에 첨부 시 가독성이 떨어지므로, 폰트 크기를 키우면서 텍스트가 이미지 영역을 침범하지 않도록 레이아웃을 조정합니다.

## Proposed Changes

### 이미지 재생성 스크립트

#### [NEW] [regenerate_img4.py](file:///c:/1.이규영개인폴더/09.##### SCHOOL #####/plane/regenerate_img4.py)

원본 이미지를 분석하여 동일한 2-panel 그래프를 재생성합니다:

**폰트 크기 설정 (논문용 대형 폰트):**
| 요소 | 기존 (추정) | 변경 |
|---|---|---|
| Title | ~10pt | **20pt (Bold)** |
| Axis Labels | ~8pt | **16pt** |
| Tick Labels | ~7pt | **14pt** |
| Annotations | ~8pt | **15pt** |
| Legend | ~8pt | **14pt** |
| Bar Values | ~8pt | **15pt (Bold)** |

**레이아웃 대응 조치 (텍스트 침범 방지):**
- `figsize=(16, 7)` → 충분한 캔버스 확보
- `subplot` 간격 `wspace=0.35` 이상 확보
- `bbox_inches='tight'` + `pad_inches` 설정
- 어노테이션 위치 재계산 (폰트 키워도 겹치지 않게)
- `tight_layout()` + `subplots_adjust()` 조합

**데이터 (원본 이미지 기반):**
- 왼쪽 패널: Epoch 0~50, mAP50 0→62.3%, Starting Point(1.2%), Final Point(62.3%)
- 오른쪽 패널: Precision=0.819, Recall=0.542, mAP50=0.623, mAP50-95=0.320

**출력 파일:**
- `이규영_국민대_DPF_논문_img_4.png` (원본 덮어쓰기)

## Verification Plan

### 자동 검증
1. 스크립트 실행: `python regenerate_img4.py`
2. 출력 이미지 존재 확인

### 시각적 검증
- 생성된 이미지를 `view_file`로 확인하여 폰트 크기, 레이아웃, 텍스트 침범 여부 확인
