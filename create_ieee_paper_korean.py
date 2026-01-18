import win32com.client
from win32com.client import constants
import os
import time

# Word Application 생성
word = win32com.client.Dispatch('Word.Application')
word.Visible = True  # 진행 상황 확인용

try:
    # 템플릿 열기
    template_path = r'C:\국민대프로젝트\TII_Articles_Word_template_2025.doc'
    source_path = r'C:\국민대프로젝트\이규영 국민대 DPF 논문.docx'
    output_path = r'C:\국민대프로젝트\IEEE_DPF_Paper_Korean_Final.docx'
    
    # 원본 논문 열기 (이미지와 표 복사용)
    source_doc = word.Documents.Open(source_path)
    
    # 템플릿 기반으로 새 문서 생성
    template_doc = word.Documents.Open(template_path)
    
    # 템플릿 내용 전체 삭제
    template_doc.Content.Delete()
    
    # =====================================================
    # IEEE 형식으로 논문 작성 (한글)
    # =====================================================
    
    rng = template_doc.Content
    
    # ----- 제목 -----
    rng.InsertAfter("소량 데이터 환경에서의 DPF 결함 검출을 위한 도메인 브리지 전이학습: YOLO11 기반 2단계 프레임워크\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 24
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1  # Center
    rng.Paragraphs.Last.SpaceAfter = 12
    
    # ----- 저자 -----
    rng.InsertAfter("\n이규영\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 11
    rng.Paragraphs.Last.Range.Font.Bold = False
    rng.Paragraphs.Last.Alignment = 1
    
    # ----- 소속 -----
    rng.InsertAfter("국민대학교 자동차공학과, 서울, 대한민국\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 9
    rng.Paragraphs.Last.Range.Font.Italic = True
    rng.Paragraphs.Last.Alignment = 1
    rng.Paragraphs.Last.SpaceAfter = 18
    
    # ----- 초록 -----
    abstract_text = """
Abstract—본 논문은 제조업의 데이터 부족 환경에서 디젤 미립자 필터(DPF) 결함 검출을 위한 새로운 2단계 도메인 브리지 전이학습 프레임워크를 제안한다. 기존의 직접 전이학습 방식과 달리, 본 연구는 ImageNet 사전학습과 타겟 DPF 검사 사이에 중간 도메인(X-ray 영상)을 도입하여 효과적인 특징 공간 브리지 경로를 형성한다. 단 339장의 학습 이미지만으로 YOLO11s를 사용하여 91.7% mAP50을 달성했으며, 이는 베이스라인 대비 34.8%p, 단일 단계 전이학습 대비 19.4%p의 개선이다. 실험 분석 결과, 현대 어텐션 기반 아키텍처에서 '늦은 개화(late blooming)' 현상이 발견되었으며, 51-100 에포크 구간에서 14.8%p의 성능 향상이 발생하여 50 에포크에서의 조기 종료 관행에 의문을 제기한다. YOLO11의 C2PSA 어텐션 메커니즘은 동일한 학습 프로토콜 하에서 YOLOv8 대비 47.2%의 상대적 성능 향상을 보였다. 본 프레임워크는 제조업 AI 배포를 위한 실용적 가이드라인을 제공한다.

"""
    rng.InsertAfter(abstract_text)
    
    # Index Terms
    rng.InsertAfter("Index Terms—딥러닝, 결함 검출, 디젤 미립자 필터, 도메인 적응, 제조 품질 관리, 객체 탐지, 전이학습, YOLO.\n\n")
    
    # ===== I. 서론 =====
    rng.InsertAfter("I. 서론\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1
    
    intro_text = """
제조업 품질 관리는 지속적인 도전에 직면해 있다: 제한된 학습 데이터로 신뢰할 수 있는 자동화 결함 검출을 달성하는 것이다. 전통적인 머신러닝 접근법은 수용 가능한 성능을 달성하기 위해 수천 개의 라벨링된 샘플을 필요로 하며, 이는 중소기업에게 상당한 진입 장벽을 형성한다. 이러한 데이터 부족 문제는 디젤 미립자 필터(DPF) 품질 관리와 같은 특수 부품 검사에서 특히 심각하며, 결함 샘플은 본질적으로 희소하고 수집 비용이 높다.

DPF는 디젤 차량의 핵심 배출 제어 부품으로, 그 품질은 환경 규제 준수와 차량 성능에 직접적인 영향을 미친다. 현재의 검사 방법은 숙련된 기술자의 수동 육안 검사에 크게 의존하며, 이 과정은 시간 소모적이고, 주관적이며, 인간 오류에 취약하다. 주요 결함 유형인 균열과 용융 손상은 불량품이 최종 사용자에게 도달하는 것을 방지하기 위해 신중한 식별이 필요하다.

전이학습은 컴퓨터 비전 응용 분야에서 데이터 부족 문제에 대한 유망한 해결책으로 부상했다. ImageNet과 같은 대규모 데이터셋에서 사전 학습된 모델을 활용하여, 연구자들은 제한된 데이터로 다양한 도메인에서 상당한 개선을 달성했다. 그러나 전이학습의 효과는 소스와 타겟 도메인 간의 유사성에 크게 의존하며, 이는 산업 검사 작업에서 체계적으로 탐구되지 않았다.

본 논문에서는 이러한 한계를 해결하는 2단계 도메인 브리지 전이학습 프레임워크를 제안한다. ImageNet에서 DPF 검사로 직접 전이하는 대신, 소스와 타겟 도메인 모두와 구조적 유사성을 공유하는 중간 도메인(X-ray 결함 검출)을 도입한다. 이 브리지 접근법은 보다 점진적인 특징 공간 전환을 생성하여, 최소한의 데이터로 더 효과적인 지식 전이를 가능하게 한다.

본 연구의 주요 기여는 다음과 같다:
• 단 339장의 학습 이미지로 91.7% mAP50을 달성하는 새로운 도메인 브리지 전이학습 프레임워크 제안 (베이스라인 대비 34.8%p, 직접 전이학습 대비 19.4%p 향상)
• 어텐션 기반 아키텍처에서 '늦은 개화' 현상 발견 및 문서화 (에포크 50 이후 14.8%p 성능 향상 발생)
• 동일 프로토콜 하 YOLO11과 YOLOv8의 포괄적 비교 (YOLO11의 C2PSA 어텐션 메커니즘으로 47.2% 상대 향상)
• 데이터 제한 환경에서의 제조업 AI 배포를 위한 실용적 가이드라인 제공

"""
    rng.InsertAfter(intro_text)
    
    # ===== II. 관련 연구 =====
    rng.InsertAfter("II. 관련 연구\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1
    
    rng.InsertAfter("A. 제조 검사에서의 딥러닝\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    related_text1 = """
딥러닝은 다양한 제조 부문에서 자동화 시각 검사에 혁명을 일으켰다. 합성곱 신경망(CNN)은 결함 검출 작업에서 뛰어난 성공을 보여주었으며, 종종 수작업 특징 기반의 전통적인 머신 비전 접근법을 능가한다. 특히 YOLO 계열의 객체 탐지 아키텍처는 실시간 추론 능력과 경쟁력 있는 정확도로 인해 인기를 얻었다.

최근 YOLO 아키텍처의 발전은 정교한 어텐션 메커니즘을 도입했다. YOLOv8은 효율적인 특징 추출을 위한 C2f 모듈을 사용하며, YOLO11은 공간 어텐션, 채널 어텐션, 컨텍스트 집계의 세 가지 병렬 어텐션 경로를 통합한 C2PSA(Cross Stage Partial with Spatial Attention) 모듈을 도입한다.

"""
    rng.InsertAfter(related_text1)
    
    rng.InsertAfter("B. 전이학습 전략\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    related_text2 = """
전이학습은 제한된 데이터로 딥러닝 모델을 학습시키는 데 사실상의 표준 접근법이 되었다. 근본적인 원칙은 대규모 데이터셋에서 학습된 특징 표현을 활용하여 타겟 작업에 적응시키는 것이다. Pan과 Yang은 이론적 기반을 확립했으며, 후속 연구들은 다른 레이어와 도메인 간 특징의 전이성을 탐구했다.

도메인 유사성은 전이 효과에 중요한 역할을 한다. Yosinski 등은 CNN 초기 레이어의 특징이 대체로 일반적이고 전이 가능한 반면, 깊은 레이어는 점점 작업 특화됨을 보여주었다. 산업 검사의 경우, 이는 시각적으로 유사한 작업에 대한 중간 도메인 사전학습이 전이 효과를 향상시킬 수 있음을 시사한다.

"""
    rng.InsertAfter(related_text2)
    
    rng.InsertAfter("C. 데이터 증강 및 소량 데이터 학습\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    related_text3 = """
데이터 증강 기법은 변환을 통해 효과적인 학습 세트 크기를 확장한다. 산업 검사의 경우, 관련 증강에는 기하학적 변환(회전, 스케일링, 플리핑), 광학적 변형(밝기, 대비), 그리고 여러 이미지를 합성 학습 샘플로 결합하는 모자이크 증강과 같은 고급 기법이 포함된다.

"""
    rng.InsertAfter(related_text3)
    
    # ===== III. 제안 방법 =====
    rng.InsertAfter("III. 제안 방법\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1
    
    rng.InsertAfter("A. 도메인 브리지 전이학습 프레임워크\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    method_text1 = """
제안하는 프레임워크는 두 개의 순차적 전이 단계로 구성되며, 중간 도메인이 범용 ImageNet 특징과 특화된 DPF 결함 검출 작업 사이의 브리지 역할을 한다.

Stage 1 (도메인 브리지): ImageNet 사전학습된 YOLO11s 모델을 균열 및 기공 주석이 있는 310장의 X-ray 결함 검출 데이터셋으로 미세 조정한다. X-ray 영상은 DPF 검사와 핵심 특성을 공유한다: 그레이스케일 이미지, 내부 구조 시각화, 유사한 결함 형태(선형 균열, 불규칙한 공동), 결함과 배경 간 낮은 대비. 이 중간 학습은 자연 이미지 패턴에서 산업 결함 패턴으로 특징 추출기를 적응시킨다.

Stage 2 (타겟 적응): X-ray 사전학습된 모델을 DPF 데이터셋(339장, 2개 클래스: Crack과 Melting)으로 추가 미세 조정한다. 이 단계는 학습된 결함 특징을 DPF 구조 손상의 특정 특성에 맞게 정제한다.

"""
    rng.InsertAfter(method_text1)
    
    rng.InsertAfter("B. YOLO11 아키텍처 분석\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    method_text2 = """
YOLO11s는 YOLOv8의 C2f 모듈에 비해 상당한 아키텍처 발전을 나타내는 C2PSA 모듈을 도입한다. C2PSA 아키텍처는 세 가지 병렬 처리 경로로 구성된다:

1) 공간 어텐션 경로: 결함을 포함할 가능성이 높은 영역을 강조하는 공간 어텐션 맵을 생성하여 '어디를' 볼지에 집중한다. 이는 작은 공간 범위를 차지하는 미세 균열 검출에 특히 효과적이다.

2) 채널 어텐션 경로: 채널별 중요도 가중치를 학습하여 '어떤' 특징이 가장 구별력 있는지 결정한다. 이는 모델이 균열 대 용융 결함 패턴에 특화된 특징을 강조할 수 있게 한다.

3) 컨텍스트 집계 경로: 큰 수용 영역에 걸쳐 정보를 풀링하여 전역 컨텍스트를 포착하고, 실제 결함과 규칙적인 필터 구조 패턴을 구별하는 데 도움이 된다.

이 세 경로의 출력은 학습 가능한 융합 레이어를 통해 결합되어, 입력 특성에 따라 각 어텐션 메커니즘의 기여를 적응적으로 가중한다.

"""
    rng.InsertAfter(method_text2)
    
    rng.InsertAfter("C. 학습 설정\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    method_text3 = """
모든 실험은 공정한 비교를 보장하기 위해 일관된 하이퍼파라미터를 사용한다:

• 옵티마이저: AdamW, weight decay 0.0005
• 학습률: 초기 0.01, 코사인 어닐링으로 0.0001까지
• 배치 크기: 16
• 입력 해상도: 640×640 픽셀
• 데이터 증강: Mosaic(확률 0.5), 회전(±15°), 스케일(0.5-1.5), 수평/수직 플리핑
• 학습 에포크: Stage 1은 50, Stage 2는 100
• 랜덤 시드: 42 (재현성을 위해 고정)

손실 함수는 세 가지 구성 요소를 결합한다: 바운딩 박스 회귀를 위한 Complete IoU(CIoU) 손실, 분류를 위한 이진 교차 엔트로피(BCE) 손실, 경계 정제를 위한 분포 초점 손실(DFL). 손실 가중치는 λ_box=7.5, λ_cls=0.5, λ_dfl=1.5로 설정된다.

"""
    rng.InsertAfter(method_text3)
    
    # ===== IV. 실험 설정 =====
    rng.InsertAfter("IV. 실험 설정\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1
    
    rng.InsertAfter("A. 데이터셋\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    setup_text1 = """
1) DPF 결함 데이터셋: 주요 데이터셋은 자동차 부품 제조업체에서 수집한 디젤 미립자 필터의 X-ray 이미지를 포함한다. 데이터셋은 339장의 학습 이미지와 66장의 검증 이미지로 구성되며, 두 가지 결함 클래스가 있다: Crack(선형 구조 손상)과 Melting(열 변형). 주석은 바운딩 박스 좌표와 함께 YOLO 형식으로 제공된다.

2) X-ray 결함 데이터셋 (브리지 도메인): 균열 및 기공 결함에 대한 주석이 있는 310장의 이미지를 포함하는 Roboflow Universe의 공개 X-ray 결함 검출 데이터셋을 활용한다. 이 데이터셋은 2단계 전이학습 접근법의 중간 도메인 역할을 한다.

"""
    rng.InsertAfter(setup_text1)
    
    rng.InsertAfter("B. 평가 지표\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    setup_text2 = """
표준 객체 탐지 지표를 사용하여 모델 성능을 평가한다:

• mAP50: IoU 임계값 0.5에서의 평균 정밀도
• mAP50-95: IoU 임계값 0.5에서 0.95까지(0.05 간격)의 평균 AP
• Precision: 참 양성을 모든 예측 양성으로 나눈 값
• Recall: 참 양성을 모든 실제 양성으로 나눈 값
• F1-Score: 정밀도와 재현율의 조화 평균

mAP50은 객체 탐지의 표준 평가 프로토콜을 나타내고 중간 수준의 위치 정밀도가 허용되는 일반적인 산업 검사 요구사항과 일치하므로 주요 비교 지표로 사용된다.

"""
    rng.InsertAfter(setup_text2)
    
    rng.InsertAfter("C. 실험 프로토콜\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    setup_text3 = """
재현성과 공정한 비교를 보장하기 위해 다음 프로토콜을 구현한다:

1) 랜덤 시드 제어: 모든 난수 생성기(Python, NumPy, PyTorch)는 값 42로 시드된다. CUDA 결정적 모드가 활성화된다.

2) 동일한 학습 조건: YOLO11s와 YOLOv8s 모델 모두 동일한 전처리, 증강, 학습 스케줄을 거친다.

3) 하드웨어 환경: 모든 실험은 AMD Ryzen 9 5900X CPU, 32GB RAM, CUDA 11.8이 설치된 NVIDIA RTX 3080 GPU가 장착된 시스템에서 수행된다.

4) 검증 프로토콜: 모델 체크포인트는 매 에포크마다 저장되며, 'best' 모델은 가장 높은 검증 mAP50을 기준으로 선택된다.

"""
    rng.InsertAfter(setup_text3)
    
    # ===== V. 실험 결과 =====
    rng.InsertAfter("V. 실험 결과\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1
    
    rng.InsertAfter("A. 전체 성능 비교\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    results_text1 = """
표 I은 2단계 도메인 브리지 전이학습 완료 후 YOLO11s와 YOLOv8s 간의 최종 성능 비교를 제시한다. YOLO11s는 91.7% mAP50을 달성하여 YOLOv8s(62.3%) 대비 29.4%p의 절대 향상을 나타낸다. 이는 15.3% 적은 파라미터(9.4M vs 11.1M)를 사용하면서 47.2%의 상대적 성능 향상에 해당한다.

"""
    rng.InsertAfter(results_text1)
    
    # 표 I 삽입 위치 표시
    rng.InsertAfter("\n[표 I: YOLO11 vs YOLOv8 최종 성능 비교]\n\n")
    
    rng.InsertAfter("B. 전이학습 효과 검증\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    results_text2 = """
표 II는 대안적 전략과 비교하여 2단계 도메인 브리지 전이학습 접근법의 효과를 보여준다. 무작위 초기화로부터의 학습은 56.9% mAP50만 달성하여 데이터 부족 문제를 부각시킨다. ImageNet으로부터의 직접 전이는 성능을 72.3%로 개선하여 15.4%p 향상을 제공한다. 중간 단계로 X-ray 사전학습을 도입하는 도메인 브리지 접근법은 91.7%를 달성하여 직접 전이 대비 추가 19.4%p 개선을 보인다.

"""
    rng.InsertAfter(results_text2)
    
    rng.InsertAfter("\n[표 II: 전이학습 전략 비교]\n\n")
    
    rng.InsertAfter("C. 늦은 개화 현상 분석\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    results_text3 = """
본 연구의 핵심 발견은 YOLO11의 학습 동역학에서 관찰되는 '늦은 개화' 현상이다. 표 III은 학습 에포크에 따른 성능 진행을 보여준다. 많은 연구에서 일반적인 종료 지점인 에포크 50에서 YOLO11s는 76.9% mAP50을 달성한다. 그러나 에포크 100까지 학습을 진행하면 상당한 추가 개선이 드러나며, 최종 성능은 91.7%에 도달한다. 이 14.8%p 향상은 학습 후반부에 최종 성능의 19.2%가 발생함을 나타낸다.

학습 과정은 네 가지 구별되는 단계로 나눌 수 있다:

Phase 1 (에포크 1-25): 37.2%에서 69.1%로 빠른 개선을 보이는 전이 적응 기간 (+31.9%p).

Phase 2 (에포크 26-50): 69.1%에서 76.9%로 안정적 개선을 보이는 점진적 정제 단계 (+7.8%p).

Phase 3 (에포크 51-75): 76.9%에서 89.5%로의 가속화된 개선 단계 ('개화') (+12.6%p). 이 단계는 Phase 2 대비 1.6배 빠른 개선 속도를 보인다.

Phase 4 (에포크 76-100): 89.5%에서 91.7%로의 미세 조정을 통한 최종 수렴 (+2.2%p).

"""
    rng.InsertAfter(results_text3)
    
    rng.InsertAfter("\n[표 III: 에포크별 성능 진행]\n\n")
    rng.InsertAfter("\n[그림 1: 학습 곡선 - 늦은 개화 현상]\n\n")
    
    rng.InsertAfter("D. 클래스별 성능 분석\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    results_text4 = """
표 IV는 클래스별 성능 지표를 제시한다. YOLO11s는 Crack 클래스에서 특히 높은 정밀도를 달성한다(100.0% vs 68.5%), 이는 균열 결함에 대한 위양성 예측이 없음을 나타낸다. 두 클래스 모두 균형 잡힌 개선을 보이며, 각 클래스에서 약 29%p의 AP 향상을 보인다.

"""
    rng.InsertAfter(results_text4)
    
    rng.InsertAfter("\n[표 IV: 클래스별 성능 비교]\n\n")
    rng.InsertAfter("\n[그림 2: 혼동 행렬]\n\n")
    rng.InsertAfter("\n[그림 3: Precision-Recall 곡선]\n\n")
    
    rng.InsertAfter("E. 통계적 유의성\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    results_text5 = """
연구 결과의 통계적 유의성을 검증하기 위해 클래스별 AP 값에 대한 대응 t-검정을 수행했다. YOLO11s와 YOLOv8s 간의 비교는 t-통계량=29.4, p-value<0.001을 산출하여 매우 유의미한 차이(99.9% 신뢰 수준)를 나타낸다. Cohen's d=4.32는 매우 큰 효과 크기를 나타낸다. 동일 시드로 세 번의 독립적 실행에 대한 재현성 테스트는 변동 계수(CV) 0.05%를 산출하여 거의 완벽한 재현성을 확인한다.

"""
    rng.InsertAfter(results_text5)
    
    rng.InsertAfter("\n[그림 4: 검증 배치 예측 결과]\n\n")
    rng.InsertAfter("\n[그림 5: F1 점수 곡선]\n\n")
    
    # ===== VI. 토론 =====
    rng.InsertAfter("VI. 토론\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1
    
    rng.InsertAfter("A. 주요 발견의 해석\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    disc_text1 = """
도메인 브리지 전이학습의 우수성은 특징 공간 전환의 관점에서 설명될 수 있다. ImageNet에서 DPF로 직접 전이할 때, 모델은 자연 RGB 이미지에서 산업용 그레이스케일 X-ray 영상까지 큰 도메인 갭을 연결해야 한다. 중간 X-ray 결함 도메인을 도입함으로써, 특징 공간을 통한 보다 점진적인 전환 경로를 생성한다. X-ray 도메인은 ImageNet(일반적인 시각 패턴)과 DPF 검사(결함 특화 특징, 그레이스케일 영상, 내부 구조 시각화) 모두와 특성을 공유한다.

YOLO11의 늦은 개화 현상은 C2PSA 어텐션 메커니즘의 복잡성에 기인할 수 있다. 세 가지 병렬 어텐션 경로(공간, 채널, 컨텍스트)는 최적의 시너지를 달성하기 위해 확장된 학습이 필요하다. 초기 학습(Phase 1-2) 동안, 각 경로는 다소 독립적으로 최적화된다. Phase 3에서만 융합 레이어가 최적의 조합을 발견하여 가속화된 성능 향상으로 이어진다.

"""
    rng.InsertAfter(disc_text1)
    
    rng.InsertAfter("B. 제조업을 위한 실용적 함의\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    disc_text2 = """
본 연구 결과는 제조업 AI 배포에 대한 두 가지 일반적인 가정에 의문을 제기한다:

1) 데이터 요구사항: 효과적인 AI가 수천 개의 학습 샘플을 필요로 한다는 통념은 339장의 이미지로 91.7% mAP50을 달성함으로써 반박된다. 핵심은 데이터 양이 아니라 전이 전략—타겟 응용 분야와 특성을 공유하는 중간 도메인을 식별하고 활용하는 것이다.

2) 학습 기간: 검증 정체 관찰을 기반으로 50 에포크에서 조기 종료하는 일반적인 관행은 어텐션 기반 아키텍처의 모델 잠재력을 상당히 과소평가할 수 있다. 확장된 학습의 추가 계산 비용(클라우드 컴퓨팅 비용 약 $2-5)은 성능 이점(14.8%p)에 비해 미미하며, 이는 상당한 운영 절감으로 이어질 수 있다.

"""
    rng.InsertAfter(disc_text2)
    
    rng.InsertAfter("C. 한계점 및 향후 연구\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Italic = True
    
    disc_text3 = """
본 연구는 향후 연구 방향을 제시하는 여러 한계점을 가진다:

1) 실시간 추론: 현재 CPU 추론 속도(~6.9 FPS)는 실시간 요구사항(30+ FPS)에 미치지 못한다. TensorRT를 사용한 GPU 최적화는 180-200 FPS를 달성하여 생산 배포를 가능하게 할 것으로 예상된다.

2) 일반화: 모델은 단일 제조사의 데이터로 학습되었다. 더 넓은 산업적 적용성을 위해 다중 제조사 검증 및 few-shot 적응 프로토콜이 필요하다.

3) 클래스 범위: 현재 두 가지 결함 클래스(Crack, Melting)만 검출된다. 막힘, 부식, 변형을 포함하도록 확장하면 실용성이 향상될 것이다.

4) 설명 가능성: XAI 기법(Grad-CAM, SHAP)의 통합은 운영자 신뢰도를 개선하고 규제 준수를 용이하게 할 것이다.

"""
    rng.InsertAfter(disc_text3)
    
    rng.InsertAfter("\n[표 V: 다른 제조 분야로의 확장 가능성]\n\n")
    
    # ===== VII. 결론 =====
    rng.InsertAfter("VII. 결론\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1
    
    conc_text = """
본 논문은 단 339장의 학습 이미지를 사용하여 DPF 결함 검출에서 91.7% mAP50을 달성하는 도메인 브리지 전이학습 프레임워크를 제시한다. 주요 기여는 다음과 같다:

1) ImageNet 사전학습과 특화된 DPF 검사 사이의 갭을 연결하기 위해 중간 X-ray 도메인을 활용하는 2단계 전이학습 접근법으로, 직접 전이 대비 19.4%p 향상을 달성한다.

2) 어텐션 기반 아키텍처에서 '늦은 개화' 현상의 문서화로, 일반적으로 사용되는 50 에포크 종료 지점 이후 14.8%p의 성능 향상이 발생함을 보여준다.

3) YOLO11의 C2PSA 어텐션 메커니즘이 동일 조건에서 YOLOv8 대비 47.2% 상대 향상을 달성함을 보여주는 포괄적 평가.

4) 제조업 AI 배포를 위한 실용적 가이드라인: 사전학습을 위한 도메인 유사 중간 데이터셋 선택, 어텐션 기반 모델의 학습 기간 연장, 최소한의 데이터 투자로 생산 준비 수준의 정확도 달성.

이러한 연구 결과는 데이터 부족이 제조업에서 AI 도입의 장벽이 될 필요가 없음을 보여준다. 적절한 전이학습 전략과 학습 프로토콜을 통해, 제한된 샘플만 있는 특수 응용 분야에서도 고성능 자동화 검사가 달성 가능하다.

"""
    rng.InsertAfter(conc_text)
    
    # ===== 참고문헌 =====
    rng.InsertAfter("참고문헌\n")
    rng.Paragraphs.Last.Range.Font.Name = "Helvetica"
    rng.Paragraphs.Last.Range.Font.Size = 10
    rng.Paragraphs.Last.Range.Font.Bold = True
    rng.Paragraphs.Last.Alignment = 1
    
    references = """
[1] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," Nature, vol. 521, no. 7553, pp. 436-444, 2015.
[2] J. Deng et al., "ImageNet: A large-scale hierarchical image database," in Proc. IEEE CVPR, 2009, pp. 248-255.
[3] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE CVPR, 2016, pp. 770-778.
[4] D. Weimer, B. Scholz-Reiter, and M. Shpitalni, "Design of deep convolutional neural network architectures for automated feature extraction in industrial inspection," CIRP Ann., vol. 65, no. 1, pp. 417-420, 2016.
[5] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, "You only look once: Unified, real-time object detection," in Proc. IEEE CVPR, 2016, pp. 779-788.
[6] A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao, "YOLOv4: Optimal speed and accuracy of object detection," arXiv:2004.10934, 2020.
[7] G. Jocher, A. Chaurasia, and J. Qiu, "Ultralytics YOLOv8," https://github.com/ultralytics/ultralytics, 2023.
[8] G. Jocher and A. Chaurasia, "Ultralytics YOLO11," https://github.com/ultralytics/ultralytics, 2024.
[9] S. J. Pan and Q. Yang, "A survey on transfer learning," IEEE Trans. Knowl. Data Eng., vol. 22, no. 10, pp. 1345-1359, 2010.
[10] J. Donahue et al., "DeCAF: A deep convolutional activation feature for generic visual recognition," in Proc. ICML, 2014, pp. 647-655.
[11] A. S. Razavian, H. Azizpour, J. Sullivan, and S. Carlsson, "CNN features off-the-shelf: An astounding baseline for recognition," in Proc. IEEE CVPRW, 2014, pp. 512-519.
[12] J. Yosinski, J. Clune, Y. Bengio, and H. Lipson, "How transferable are features in deep neural networks?" in Proc. NeurIPS, 2014, pp. 3320-3328.
[13] C. Shorten and T. M. Khoshgoftaar, "A survey on image data augmentation for deep learning," J. Big Data, vol. 6, no. 1, p. 60, 2019.
[14] O. Vinyals, C. Blundell, T. Lillicrap, K. Kavukcuoglu, and D. Wierstra, "Matching networks for one shot learning," in Proc. NeurIPS, 2016, pp. 3630-3638.
[15] Z. Zou, K. Chen, Z. Shi, Y. Guo, and J. Ye, "Object detection in 20 years: A survey," Proc. IEEE, vol. 111, no. 3, pp. 257-276, 2023.

"""
    rng.InsertAfter(references)
    
    # 문서 저장
    template_doc.SaveAs(output_path, 16)  # 16 = docx format
    print(f"한글 논문이 저장되었습니다: {output_path}")
    
    # 원본 문서에서 표와 이미지 복사 안내
    print("\n※ 원본 논문에서 표와 이미지를 수동으로 복사해야 합니다.")
    print("원본 논문에 포함된 표:")
    print("  - 표 1: 학습 전략별 성능 비교")
    print("  - 표 2: 선행연구 비교") 
    print("  - 표 3: YOLO 버전별 특징")
    print("  - 표 4: X-ray vs DPF 데이터 특성")
    print("  - 표 5: 전이학습 설정")
    print("  - 표 6: YOLO11 vs YOLOv8 최종 성능")
    print("  - 표 7: 클래스별 성능")
    print("  - 표 8: 전이학습 전략 비교")
    print("  - 표 9: 에포크별 성능")
    print("  - 표 10: 모델간 비교")
    print("  - 표 11: 학습 특성 비교")
    print("  - 표 12: 재현성 검증")
    print("  - 표 13-15: 확장 가능성")
    print("  - 표 16: 최종 평가")
    print("\n원본 논문에 포함된 이미지: 9개")
    
    source_doc.Close()
    template_doc.Close()
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    word.Quit()
