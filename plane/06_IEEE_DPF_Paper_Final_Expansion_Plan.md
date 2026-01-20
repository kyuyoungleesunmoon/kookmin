# IEEE DPF 논문 최종 확장 계획 (Version: Final Volume-Up)

**작성일:** 2026-01-20  
**목표:** `IEEE_DPF_Paper_Refined.md` (약 190줄) 대비 2배 이상의 분량 및 학술적 깊이 확보.  
**기본 전략:** **"Refined 버전의 깔끔한 뼈대"**를 유지하되, 각 문단 사이사이에 **"심층 분석(Deep Dive)"** 내용을 이식하여 밀도를 높임.

---

## 1. 섹션별 확장 상세 (Expansion Details)

| 섹션 | 기존 내용 (Refined.md) | **추가/보강될 내용 (Source: Draft + Deepening)** | 예상 분량 증가 |
|:---:|:---|:---|:---:|
| **Abstract** | 91.7% 달성 요약 | Late Blooming, Industry 5.0 키워드 강화, 수치적 기여도 구체화 | +5줄 |
| **I. Introduction** | 배경/목적 (간략) | **1) Industry 5.0 & Sustainability:** 단순 설명에서 2문단으로 확장.<br>**2) Data Statistics (Fig 1):** 결함 크기 분포(98% < 1%) 통계 데이터 삽입으로 '난이도' 강조. | +0.5 페이지 |
| **II. Related Work** | 딥러닝/전이학습/YOLO (단순 나열) | **1) 최신 연구(2024-2025) 표:** SOTA 모델들과의 특징 비교표 추가.<br>**2) 이론적 차별점:** Fine-tuning vs Domain Adaptation의 수식적 차이 서술. | +1.0 페이지 |
| **III. Methodology** | 3단계 절차/알고리즘 | **1) Domain Adaptation Theory:** Ben-David 정리를 인용한 'Bridge'의 수학적 증명 ($\epsilon_T(h)$).<br>**2) Architecture (C2PSA):** YOLO11 핵심 모듈의 수식(Attention) 및 구조도 설명.<br>**3) Late Blooming Mechanism:** LR 스케줄링 곡선 수식 추가. | +1.5 페이지 |
| **IV. Experiments** | 데이터셋/구현환경 | **1) Complexity Analysis:** 파라미터(M), 연산량(GFLOPs) 비교 테이블 신설.<br>**2) Implementation Detail:** Augmentation (Mosaic, Mixup) 전략의 상세 근거 서술. | +0.5 페이지 |
| **V. Results** | 성능/비교/학습과정 | **1) Qualitative Analysis (오답노트):** FP/FN 사례 분석 (이미지 크롭 예시 서술).<br>**2) Late Blooming Deep Dive:** Epoch 50 전후의 Feature Map 변화 추론 서술. | +1.5 페이지 |
| **VI. Discussion** | 경제성 분석 (짧음) | **1) ROI Analysis:** 투자 대비 효과를 구체적 금액($) 시나리오로 확장.<br>**2) Edge Computing Feasibility:** 38 FPS의 현장 적용성 논증.<br>**3) Threats to Validity:** 연구의 한계점과 방어 논리(Generalizability). | +1.0 페이지 |
| **VII. Conclusion** | 요약 | 향후 연구 방향(Active Learning) 구체화 | +5줄 |

---

## 2. 확장 작업 프로세스 (Work Process)

1.  **Skeleton Loading:** `Refined.md` 내용을 복사하여 기본 뼈대로 잡음.
2.  **Theory Injection:** Methodology 섹션에 `Ben-David Theory` 및 `C2PSA Attention` 수식/설명 삽입.
3.  **Data Fact Check:** 실제 데이터 분석 결과(Small Object 통계)를 Introduction에 근거로 배치.
4.  **Deep Writing:** Results 및 Discussion 섹션에 'Why'에 대한 설명을 문단 단위로 추가 (단순 결과 나열 지양).
5.  **Final Polish:** 문단 간 연결어(Transition Words)를 다듬어 글의 호흡을 길게 가져감.

## 3. 예상 결과물 형태
*   **파일명:** `IEEE_DPF_Paper_Final_Extended.md`
*   **특징:**
    *   기존 Refined 버전의 깔끔한 논리 흐름 유지.
    *   수식(Equation) 5개 이상 포함 (학술적 권위).
    *   테이블 4개, 그림 7개 이상 인용 (시각적 풍부함).
    *   분량: A4 용지 기준 약 10~12페이지 (Word 변환 시).

이 계획에 동의하시면 바로 확장 집필을 시작하겠습니다.
