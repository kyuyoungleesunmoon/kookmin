# IEEE DPF 논문 고도화 마스터 플랜 및 완료 보고서 (Master Plan)

**Last Updated:** 2026-01-21
**Target Target:** IEEE Transactions on Industrial Informatics (TII) / IEEE Transactions on Industrial Electronics (TIE)
**Master Document:** `converted_md/04_IEEE_DPF_Paper_Final_Extended.md`

---

## 1. 프로젝트 개요 (Project Overview)
본 문서는 기존 DPF 결함 탐지 논문의 학술적 완성도를 IEEE 저널 투고 수준으로 끌어올리기 위해 수행된 **논문 확장(Expansion), 정제(Refinement), 및 구조화(Restructuring)** 작업의 전 과정을 기록하고, 향후 작업을 위한 가이드라인을 제공합니다.

## 2. 주요 수행 내역 (History of Achievements)

### Phase 1: 기반 구축 및 복원 (Restoration)
- **원본 데이터 복원:** 손실되었던 수치 데이터(Table 1~6)와 핵심 그래프(Fig 2~6)를 원본 논문 기반으로 완벽하게 복구했습니다.
- **이미지 정규화:** 깨지거나 잘못 연결된 이미지를 모두 수정하고, 캡션 형식을 `![Img] \n **Fig. X:**` 스타일로 통일하여 가독성을 높였습니다.

### Phase 2: 콘텐츠 대폭 확장 (Volume Expansion)
- **IEEE 표준 분량 확보:** 4페이지 내외였던 초안을 **10페이지 이상**의 분량으로 대폭 확장했습니다.
- **GLAD 프레임워크 정립:** 단순 방법론 나열이 아닌, **Generative(생성) - Adaptive(적응) - Detection(탐지)**의 3단계 GLAD 프레임워크로 논문을 재구조화했습니다.
- **이론적 깊이 강화:**
    - **Phase 1 (Generative):** Latent Diffusion 및 LoRA의 수학적 원리($\mathcal{L}_{LDM}$, $W=W_0+BA$) 서술 추가.
    - **Phase 2 (Adaptive):** 도메인 적응 이론($\mathcal{H}$-divergence) 및 계층적 전이 학습 매커니즘 상세화.
    - **Phase 3 (Detection):** Uncertainty-aware Detection 및 Sample-weighted Loss 수식화.

### Phase 3: 학술적 어조 정제 (Tone Refinement)
사용자의 엄격한 요구사항에 따라 **"AI Tone"**을 배제하고 학술적 전문성을 강화했습니다.
- **Late Blooming (늦은 개화/발화)** $\rightarrow$ **Delayed Convergence (지연된 수렴)**
- **Robustness (강건함)** $\rightarrow$ **Reliability / Stability (신뢰성 / 안정성)**
- **Key Mechanism (핵심 기제이다)** $\rightarrow$ **Plays a key role (핵심적인 역할을 수행한다)**

### Phase 4: 시각화 고도화 (Visualization Upgrade)
- **Fig. 1 (Flowchart) 재생성:** Python 스크립트(`generate_glad_flowchart.py`)를 통해 논문 내용과 정확히 일치하는 고품질 벡터 다이어그램을 생성했습니다. (Layout Cut-off 문제 해결 완료)
- **F1 Score Chart 생성:** 단순 커브 이미지가 아닌, 실제 데이터를 기반으로 한 분석 차트(`generate_f1_chart.py`)를 새로 생성하여 신뢰도를 높였습니다.

### Phase 5: 참고문헌 표준화 (Reference Standardization)
- **IEEE Citation Style 준수:** 총 32개의 참고문헌을 IEEE 포맷(`[#] A. Author, "Title," *Journal*, ...`)에 맞춰 재작성했습니다.
- **URL 정책 준수:** 일반 논문에는 URL을 삭제하고, GitHub 코드 및 Roboflow 데이터셋에만 `[Online]. Available:`을 명시하여 규정을 준수했습니다.
- **가독성 개선:** 각 참고문헌 항목 사이에 공백(Spacing)을 추가하여 가독성을 확보했습니다.

---

## 3. 사용자 핵심 요구사항 및 대응 (Key Requirements & Solutions)

| 영역 | 요구사항 (Requirements) | 해결 방안 (Solutions) |
| :--- | :--- | :--- |
| **Tone** | "AI 번역투, 늦은 발화, 강건한 등의 표현 지양" | 영어권 학술 용어(Delayed Convergence 등)로 대체 및 문맥 순화 |
| **Figure** | "Fig 1 그림이 안 맞음, 박스 잘림" | Python Matplotlib 스크립트로 Custom Flowchart 제작 및 Canvas 확장 |
| **Content** | "논문이 너무 짧음, 10페이지로 늘려라" | Intro(배경), Method(수식), Exp(분석) 각 섹션을 Deep-dive 형태로 확장 집필 |
| **Ref** | "URL 포함 여부 확인 및 띄어쓰기" | SW/Dataset만 URL 허용 확인, 항목 간 줄바꿈 추가 |
| **Git** | "최종본 Git 업로드" | `main` 브랜치에 코드, 문서, 이미지 전량 Push 완료 |

---

## 4. 최종 산출물 (Final Deliverables)

1.  **최종 논문 (Markdown):** `c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md\04_IEEE_DPF_Paper_Final_Extended.md`
2.  **이미지 에셋:** `c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md\images\` (모든 Figure 포함)
3.  **생성 스크립트:**
    - `generate_glad_flowchart.py`: Fig 1 생성
    - `generate_f1_chart.py`: F1 Score 분석 차트 생성

---

## 5. 향후 계획 (Future Roadmap)

현재 논문은 **IEEE 투고를 위한 내용적 준비(Content Readiness)가 완료**된 상태입니다. 다음 단계로 아래의 작업을 제안합니다.

1.  **Word/LaTeX 변환 (Formatting):**
    - 현재 Markdown 형식을 실제 IEEE Word 템플릿(`.doc`) 또는 LaTeX 템플릿에 옮겨 2단(Two-column) 레이아웃을 잡아야 합니다.
    - Markdown의 수식이 Word 수식 에디터 또는 LaTeX 코드로 정확히 변환되는지 확인이 필요합니다.

2.  **최종 교정 (Proofreading):**
    - 영문 번역이 필요한 경우, 현재 정제된 국문 내용을 바탕으로 전문 번역을 진행해야 합니다. (현재 국문 버전임)

3.  **저널 선정 및 투고:**
    - 타겟 저널(IEEE TII 등)의 가이드라인(Author Guide)을 최종 확인하고 투고 시스템에 파일 업로드를 준비합니다.
