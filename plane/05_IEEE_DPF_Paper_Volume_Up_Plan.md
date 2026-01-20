# IEEE TII 논문 분량 2배 확장을 위한 심층 증량 계획 (Volume-Up Plan)

**작성일:** 2026-01-20  
**목표:** IEEE 2-Column Format 기준 8~10페이지 분량 확보 (현재 약 4~5페이지 예상)  
**핵심 전략:** 단순 텍스트 늘리기가 아닌, **"이론적 깊이(Depth)"**와 **"분석의 치밀함(Rigor)"**을 보강하여 자연스러운 증량 유도.

---

## 1. 섹션별 상세 확장 전략

### **I. Introduction (예상 증량: +0.5 페이지)**
*   **현재:** 문제 제기 → 통계 제시 → 솔루션 요약.
*   **확장:**
    *   **Industry 5.0 배경 강화:** 단순 인용을 넘어, 인간 중심 제조(Human-Centric)와 지속 가능성(Sustainability) 관점에서 결함 검출의 필요성을 2문단 이상 서술.
    *   **기존 연구의 한계점 세분화:** 
        1.  Data Scarcity (데이터 부족)
        2.  Domain Shift (도메인 불일치)
        3.  Scale Imbalance (미세 객체) 
        각 항목을 별도 문단으로 나누어 구체적 사례와 함께 비판.

### **II. Related Work (예상 증량: +1.0 페이지)**
*   **현재:** 일반 객체 탐지 / Few-shot 트렌드 (간략).
*   **확장:** 카테고리를 세분화하여 문헌 리뷰를 대폭 강화.
    *   **A. Deep Learning in Manufacturing:** CNN부터 Transformer 기반 방법론까지의 진화 과정 서술.
    *   **B. Transfer Learning & Domain Adaptation:** "Fine-tuning" vs "Domain Adaptation" vs "Domain Generalization"의 차이를 이론적으로 설명하고 본 연구의 위치(Domain Bridging)를 명확히 함.
    *   **C. Small Object Detection:** Feature Pyramid Network (FPN), Attention Mechanism 등 미세 객체 탐지 기법들에 대한 리뷰 추가.

### **III. Methodology (예상 증량: +1.5 페이지)**
*   **현재:** 문제 정의 / 3단계 프로토콜 / Late Blooming 정의.
*   **확장:** **"수식(Mathematics)"**과 **"아키텍처(Architecture)"**를 대폭 보강.
    *   **A. Theoretical Formulation:** 
        *   Ben-David의 Domain Adaptation 이론($\mathcal{H}\Delta\mathcal{H}$-distance)을 인용하여, 'Bridge Domain'이 상한(Upper Bound)을 낮추는 원리를 수식으로 증명 ($d_{\mathcal{H}}(S, T) \le d_{\mathcal{H}}(S, B) + d_{\mathcal{H}}(B, T)$).
    *   **B. Network Architecture (YOLO11 Analysis):**
        *   C2PSA(Cross-Stage Partial Self-Attention) 모듈의 내부 구조(Query, Key, Value 연산)를 수식과 함께 상세히 설명. 
        *   이 모듈이 왜 DPF의 '작은 결함'에 효과적인지 Receptive Field 관점에서 논증.
    *   **C. OneCycle Scheduling:** 
        *   단순 적용 사실만 언급하는 것이 아니라, Learning Rate의 변화 곡선 수식과 운동량(Momentum)의 관계를 설명하며 Late Blooming을 유도하는 메커니즘 서술.

### **IV. Experimental Results (예상 증량: +1.5 페이지)**
*   **현재:** 정량적 비교 / Late Blooming / Ablation Study.
*   **확장:** **"정성적 분석(Qualitative Analysis)"**과 **"실패 분석(Failure Analysis)"** 추가.
    *   **A. Detailed Comparative Analysis:**
        *   각 모델(Faster R-CNN, RT-DETR 등)의 성능 차이에 대한 구조적 원인 분석 텍스트 추가.
    *   **B. Failure Analysis (오답 노트):**
        *   FP(False Positive)와 FN(False Negative) 사례를 구체적으로 묘사 (e.g., "기판의 불규칙한 패턴을 Crack으로 오인").
        *   이를 해결하기 위한 방안(Active Learning 등)을 논의하며 분량 확보.
    *   **C. Computational Complexity:**
        *   파라미터 수(Params), 연산량(GFLOPs), 추론 시간(Latency)을 비교하는 별도 파트 신설. Edge Device 탑재 가능성 논증.

### **V. Discussion (예상 증량: +0.5 페이지)**
*   **현재:** Industry 5.0 / 한계점.
*   **확장:** **"Threats to Validity"** 및 **"Practical Implications"** 추가.
    *   **Validity:** 데이터셋 편향 가능성, 외부 타당성(Generalizability)에 대한 학술적 방어.
    *   **Implication:** 공장 관리자가 이 시스템을 도입했을 때 얻을 수 있는 ROI(투자 대비 효과)를 정성적으로 서술.

---

## 2. 작업 순서
1.  **[Methodology]** Domain Adaptation 이론 수식 및 C2PSA 아키텍처 상세 기술.
2.  **[Related Work]** 최신 논문(2023-2025) 10편 이상 추가 리스팅 및 요약 통합.
3.  **[Results]** Failure Analysis 및 복잡도 분석 섹션 신설.
4.  **[Intro/Discussion]** 배경 설명 및 고찰 문단 확장 (Paragraph Splitting).

이 계획대로 진행 시, 논문의 논리적 밀도가 높아짐과 동시에 분량이 자연스럽게 2배 이상(IEEE 포맷 기준 8p+) 확보될 것입니다.
