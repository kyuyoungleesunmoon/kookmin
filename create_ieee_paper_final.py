import win32com.client
import time
import os

print("IEEE 템플릿 기반 한글 논문 생성 중...")
print("(원본 논문의 표와 이미지를 자동으로 복사합니다)")

# Word Application 생성
word = win32com.client.Dispatch('Word.Application')
word.Visible = True

try:
    # 파일 경로
    template_path = r'C:\국민대프로젝트\TII_Articles_Word_template_2025.doc'
    source_path = r'C:\국민대프로젝트\이규영 국민대 DPF 논문.docx'
    output_path = r'C:\국민대프로젝트\IEEE_DPF_논문_최종본.docx'
    
    # 원본 논문 열기
    source_doc = word.Documents.Open(source_path)
    time.sleep(1)
    
    # 템플릿 열기
    template_doc = word.Documents.Open(template_path)
    time.sleep(1)
    
    # 템플릿 내용 삭제
    template_doc.Content.Delete()
    
    # Selection 객체 사용을 위해 template_doc 활성화
    template_doc.Activate()
    sel = word.Selection
    
    # =====================================================
    # 논문 내용 작성
    # =====================================================
    
    # ===== 제목 =====
    sel.TypeText("소량 데이터 환경에서의 DPF 결함 검출을 위한\n")
    sel.TypeText("도메인 브리지 전이학습: YOLO11 기반 2단계 프레임워크\n\n")
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 24
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1  # Center
    
    # ===== 저자 =====
    sel.Font.Size = 11
    sel.Font.Bold = False
    sel.TypeText("이규영\n")
    sel.Font.Size = 9
    sel.Font.Italic = True
    sel.TypeText("국민대학교 자동차공학과, 서울, 대한민국\n")
    sel.TypeText("Email: gylee@kookmin.ac.kr\n\n")
    sel.Font.Italic = False
    
    # ===== 초록 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 9
    sel.Font.Bold = True
    sel.Font.Italic = True
    sel.TypeText("Abstract—")
    sel.Font.Bold = False
    sel.TypeText("본 논문은 제조업의 데이터 부족 환경에서 디젤 미립자 필터(DPF) 결함 검출을 위한 새로운 2단계 도메인 브리지 전이학습 프레임워크를 제안한다. 기존의 직접 전이학습 방식과 달리, 본 연구는 ImageNet 사전학습과 타겟 DPF 검사 사이에 중간 도메인(X-ray 영상)을 도입하여 효과적인 특징 공간 브리지 경로를 형성한다. 단 339장의 학습 이미지만으로 YOLO11s를 사용하여 91.7% mAP50을 달성했으며, 이는 베이스라인 대비 34.8%p, 단일 단계 전이학습 대비 19.4%p의 개선이다. 실험 분석 결과, 현대 어텐션 기반 아키텍처에서 '늦은 개화(late blooming)' 현상이 발견되었으며, 51-100 에포크 구간에서 14.8%p의 성능 향상이 발생하여 50 에포크에서의 조기 종료 관행에 의문을 제기한다. YOLO11의 C2PSA 어텐션 메커니즘은 동일한 학습 프로토콜 하에서 YOLOv8 대비 47.2%의 상대적 성능 향상을 보였다.\n\n")
    sel.Font.Italic = False
    
    # Index Terms
    sel.Font.Bold = True
    sel.Font.Italic = True
    sel.TypeText("Index Terms—")
    sel.Font.Bold = False
    sel.TypeText("딥러닝, 결함 검출, 디젤 미립자 필터, 도메인 적응, 제조 품질 관리, 객체 탐지, 전이학습, YOLO.\n\n")
    sel.Font.Italic = False
    
    # ===== I. 서론 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("I. 서론\n\n")
    sel.Font.Bold = False
    sel.ParagraphFormat.Alignment = 3  # Justify
    
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 10
    sel.TypeText("제조업 품질 관리는 지속적인 도전에 직면해 있다: 제한된 학습 데이터로 신뢰할 수 있는 자동화 결함 검출을 달성하는 것이다. 전통적인 머신러닝 접근법은 수용 가능한 성능을 달성하기 위해 수천 개의 라벨링된 샘플을 필요로 하며, 이는 중소기업에게 상당한 진입 장벽을 형성한다.\n\n")
    
    sel.TypeText("DPF는 디젤 차량의 핵심 배출 제어 부품으로, 그 품질은 환경 규제 준수와 차량 성능에 직접적인 영향을 미친다. 현재의 검사 방법은 숙련된 기술자의 수동 육안 검사에 크게 의존하며, 이 과정은 시간 소모적이고, 주관적이며, 인간 오류에 취약하다.\n\n")
    
    sel.TypeText("전이학습은 컴퓨터 비전 응용 분야에서 데이터 부족 문제에 대한 유망한 해결책으로 부상했다. ImageNet과 같은 대규모 데이터셋에서 사전 학습된 모델을 활용하여, 연구자들은 제한된 데이터로 다양한 도메인에서 상당한 개선을 달성했다[1], [2]. 그러나 전이학습의 효과는 소스와 타겟 도메인 간의 유사성에 크게 의존한다.\n\n")
    
    sel.TypeText("본 논문에서는 2단계 도메인 브리지 전이학습 프레임워크를 제안한다. ImageNet에서 DPF 검사로 직접 전이하는 대신, 소스와 타겟 도메인 모두와 구조적 유사성을 공유하는 중간 도메인(X-ray 결함 검출)을 도입한다.\n\n")
    
    sel.TypeText("본 연구의 주요 기여는 다음과 같다:\n")
    sel.TypeText("• 339장의 학습 이미지로 91.7% mAP50 달성 (베이스라인 대비 34.8%p, 직접 전이 대비 19.4%p 향상)\n")
    sel.TypeText("• 어텐션 기반 아키텍처에서 '늦은 개화' 현상 발견 (에포크 50 이후 14.8%p 성능 향상)\n")
    sel.TypeText("• YOLO11과 YOLOv8의 포괄적 비교 (47.2% 상대 향상)\n")
    sel.TypeText("• 데이터 제한 환경에서의 제조업 AI 배포 가이드라인 제공\n\n")
    
    # ===== II. 관련 연구 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("II. 관련 연구\n\n")
    sel.Font.Bold = False
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Italic = True
    sel.TypeText("A. 제조 검사에서의 딥러닝\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("딥러닝은 다양한 제조 부문에서 자동화 시각 검사에 혁명을 일으켰다. CNN은 결함 검출 작업에서 뛰어난 성공을 보여주었으며, 종종 수작업 특징 기반의 전통적인 머신 비전 접근법을 능가한다[3], [4]. 특히 YOLO 계열의 객체 탐지 아키텍처는 실시간 추론 능력과 경쟁력 있는 정확도로 인기를 얻었다[5]-[8].\n\n")
    
    sel.Font.Name = "Helvetica"
    sel.Font.Italic = True
    sel.TypeText("B. 전이학습 전략\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("전이학습은 제한된 데이터로 딥러닝 모델을 학습시키는 데 사실상의 표준 접근법이 되었다[9], [10]. 근본적인 원칙은 대규모 데이터셋에서 학습된 특징 표현을 활용하여 타겟 작업에 적응시키는 것이다. 도메인 유사성은 전이 효과에 중요한 역할을 하며, Yosinski 등[12]은 CNN 초기 레이어의 특징이 대체로 일반적이고 전이 가능한 반면, 깊은 레이어는 점점 작업 특화됨을 보여주었다.\n\n")
    
    # ===== III. 제안 방법 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("III. 제안 방법\n\n")
    sel.Font.Bold = False
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Italic = True
    sel.TypeText("A. 도메인 브리지 전이학습 프레임워크\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("제안하는 프레임워크는 두 개의 순차적 전이 단계로 구성되며, 중간 도메인이 범용 ImageNet 특징과 특화된 DPF 결함 검출 작업 사이의 브리지 역할을 한다.\n\n")
    
    sel.TypeText("Stage 1 (도메인 브리지): ImageNet 사전학습된 YOLO11s 모델을 310장의 X-ray 결함 검출 데이터셋으로 미세 조정한다. X-ray 영상은 DPF 검사와 핵심 특성을 공유한다: 그레이스케일 이미지, 내부 구조 시각화, 유사한 결함 형태.\n\n")
    
    sel.TypeText("Stage 2 (타겟 적응): X-ray 사전학습된 모델을 DPF 데이터셋(339장, 2개 클래스: Crack과 Melting)으로 추가 미세 조정한다.\n\n")
    
    # 표 1 복사
    print("표 1 복사 중...")
    source_doc.Activate()
    source_doc.Tables(1).Range.Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("표 I. 전이학습 전략별 성능 비교\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Italic = True
    sel.TypeText("B. YOLO11 아키텍처 분석\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("YOLO11s는 YOLOv8의 C2f 모듈에 비해 상당한 아키텍처 발전을 나타내는 C2PSA(Cross Stage Partial with Spatial Attention) 모듈을 도입한다. C2PSA 아키텍처는 세 가지 병렬 처리 경로로 구성된다:\n")
    sel.TypeText("1) 공간 어텐션 경로: 결함을 포함할 가능성이 높은 영역을 강조\n")
    sel.TypeText("2) 채널 어텐션 경로: 가장 구별력 있는 특징 결정\n")
    sel.TypeText("3) 컨텍스트 집계 경로: 전역 컨텍스트 포착\n\n")
    
    sel.Font.Name = "Helvetica"
    sel.Font.Italic = True
    sel.TypeText("C. 학습 설정\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("모든 실험은 공정한 비교를 위해 일관된 하이퍼파라미터를 사용한다:\n")
    sel.TypeText("• 옵티마이저: AdamW, weight decay 0.0005\n")
    sel.TypeText("• 학습률: 초기 0.01, 코사인 어닐링\n")
    sel.TypeText("• 배치 크기: 16, 입력 해상도: 640×640\n")
    sel.TypeText("• 학습 에포크: Stage 1은 50, Stage 2는 100\n")
    sel.TypeText("• 랜덤 시드: 42\n\n")
    
    # ===== IV. 실험 설정 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("IV. 실험 설정\n\n")
    sel.Font.Bold = False
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Italic = True
    sel.TypeText("A. 데이터셋\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("1) DPF 결함 데이터셋: 339장의 학습 이미지와 66장의 검증 이미지, 두 가지 결함 클래스(Crack, Melting).\n\n")
    sel.TypeText("2) X-ray 결함 데이터셋 (브리지 도메인): Roboflow Universe의 310장 이미지.\n\n")
    
    # 표 4 복사 (X-ray vs DPF 데이터 특성)
    print("표 4 복사 중...")
    source_doc.Activate()
    source_doc.Tables(4).Range.Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("표 II. X-ray vs DPF 데이터 특성 비교\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # ===== V. 실험 결과 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("V. 실험 결과\n\n")
    sel.Font.Bold = False
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Italic = True
    sel.TypeText("A. 전체 성능 비교\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("YOLO11s는 91.7% mAP50을 달성하여 YOLOv8s(62.3%) 대비 29.4%p의 절대 향상을 나타낸다. 이는 15.3% 적은 파라미터를 사용하면서 47.2%의 상대적 성능 향상에 해당한다.\n\n")
    
    # 표 6 복사 (YOLO11 vs YOLOv8 최종 성능)
    print("표 6 복사 중...")
    source_doc.Activate()
    source_doc.Tables(6).Range.Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("표 III. YOLO11 vs YOLOv8 최종 성능 비교\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Italic = True
    sel.TypeText("B. 전이학습 효과 검증\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("무작위 초기화: 56.9% mAP50\n")
    sel.TypeText("직접 전이(ImageNet→DPF): 72.3% (+15.4%p)\n")
    sel.TypeText("도메인 브리지(ImageNet→X-ray→DPF): 91.7% (+34.8%p)\n\n")
    
    # 표 8 복사 (전이학습 전략 비교)
    print("표 8 복사 중...")
    source_doc.Activate()
    source_doc.Tables(8).Range.Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("표 IV. 전이학습 전략 비교\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Italic = True
    sel.TypeText("C. 늦은 개화 현상 분석\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("에포크 50에서 YOLO11s는 76.9% mAP50을 달성한다. 그러나 에포크 100까지 학습 시 91.7%에 도달한다. 이 14.8%p 향상은 최종 성능의 19.2%가 학습 후반부에 발생함을 나타낸다.\n\n")
    sel.TypeText("Phase 1 (에포크 1-25): 37.2%→69.1% (+31.9%p) - 전이 적응\n")
    sel.TypeText("Phase 2 (에포크 26-50): 69.1%→76.9% (+7.8%p) - 점진적 정제\n")
    sel.TypeText("Phase 3 (에포크 51-75): 76.9%→89.5% (+12.6%p) - 가속 개선\n")
    sel.TypeText("Phase 4 (에포크 76-100): 89.5%→91.7% (+2.2%p) - 최종 수렴\n\n")
    
    # 표 9 복사 (에포크별 성능)
    print("표 9 복사 중...")
    source_doc.Activate()
    source_doc.Tables(9).Range.Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("표 V. Stage 2 에포크별 성능\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # 이미지 2 복사 (학습 곡선)
    print("그림 1 (학습 곡선) 복사 중...")
    source_doc.Activate()
    source_doc.InlineShapes(2).Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("그림 1. Stage 2 전체 학습 곡선 (100 Epochs)\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Italic = True
    sel.TypeText("D. 클래스별 성능 분석\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("YOLO11s는 Crack 클래스에서 100.0% 정밀도를 달성하여 균열 결함에 대한 위양성 예측이 없음을 나타낸다.\n\n")
    
    # 표 7 복사 (클래스별 성능)
    print("표 7 복사 중...")
    source_doc.Activate()
    source_doc.Tables(7).Range.Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("표 VI. 클래스별 성능 비교\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # 이미지 6 복사 (혼동 행렬)
    print("그림 2 (혼동 행렬) 복사 중...")
    source_doc.Activate()
    source_doc.InlineShapes(6).Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("그림 2. YOLO11 혼동 행렬\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # 이미지 8 복사 (PR 곡선)
    print("그림 3 (PR 곡선) 복사 중...")
    source_doc.Activate()
    source_doc.InlineShapes(8).Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("그림 3. Precision-Recall 곡선\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Italic = True
    sel.TypeText("E. 통계적 유의성\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("YOLO11s와 YOLOv8s 비교: t-통계량=29.4, p-value<0.001 (99.9% 신뢰 수준). Cohen's d=4.32 (매우 큰 효과 크기). 재현성 변동 계수(CV)=0.05%.\n\n")
    
    # 이미지 7 복사 (검증 배치 예측)
    print("그림 4 (검증 배치) 복사 중...")
    source_doc.Activate()
    source_doc.InlineShapes(7).Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("그림 4. 검증 배치 예측 결과\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # 이미지 11 복사 (F1 곡선)
    print("그림 5 (F1 곡선) 복사 중...")
    source_doc.Activate()
    source_doc.InlineShapes(11).Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("그림 5. F1 점수 곡선\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # ===== VI. 토론 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("VI. 토론\n\n")
    sel.Font.Bold = False
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Italic = True
    sel.TypeText("A. 주요 발견의 해석\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("도메인 브리지 전이학습의 우수성은 특징 공간 전환의 관점에서 설명될 수 있다. 중간 X-ray 결함 도메인을 도입함으로써, 특징 공간을 통한 보다 점진적인 전환 경로를 생성한다.\n\n")
    sel.TypeText("YOLO11의 늦은 개화 현상은 C2PSA 어텐션 메커니즘의 복잡성에 기인할 수 있다. 세 가지 병렬 어텐션 경로는 최적의 시너지를 달성하기 위해 확장된 학습이 필요하다.\n\n")
    
    # 이미지 3 복사 (전이학습 비교)
    print("그림 6 (전이학습 비교) 복사 중...")
    source_doc.Activate()
    source_doc.InlineShapes(3).Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("그림 6. 전이학습 방법에 따른 성능 비교\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Italic = True
    sel.TypeText("B. 제조업을 위한 실용적 함의\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("1) 데이터 요구사항: 339장의 이미지로 91.7% mAP50을 달성함으로써 대규모 데이터 필요성에 대한 통념이 반박된다.\n\n")
    sel.TypeText("2) 학습 기간: 50 에포크에서 조기 종료하는 관행은 어텐션 기반 아키텍처의 잠재력을 과소평가할 수 있다.\n\n")
    
    sel.Font.Name = "Helvetica"
    sel.Font.Italic = True
    sel.TypeText("C. 한계점 및 향후 연구\n\n")
    sel.Font.Italic = False
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("1) 실시간 추론: CPU 추론 속도(~6.9 FPS)는 실시간 요구사항(30+ FPS)에 미달.\n")
    sel.TypeText("2) 일반화: 단일 제조사 데이터로 학습. 다중 제조사 검증 필요.\n")
    sel.TypeText("3) 클래스 범위: 두 가지 결함 클래스만 검출. 확장 필요.\n")
    sel.TypeText("4) 설명 가능성: XAI 기법 통합 필요.\n\n")
    
    # 이미지 9 복사 (데이터 증강)
    print("그림 7 (데이터 증강) 복사 중...")
    source_doc.Activate()
    source_doc.InlineShapes(9).Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("그림 7. 데이터 증강 분석\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # ===== VII. 결론 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("VII. 결론\n\n")
    sel.Font.Bold = False
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Name = "Times New Roman"
    sel.TypeText("본 논문은 339장의 학습 이미지로 DPF 결함 검출에서 91.7% mAP50을 달성하는 도메인 브리지 전이학습 프레임워크를 제시한다.\n\n")
    sel.TypeText("주요 기여:\n")
    sel.TypeText("1) 중간 X-ray 도메인을 활용하는 2단계 전이학습으로 직접 전이 대비 19.4%p 향상\n")
    sel.TypeText("2) '늦은 개화' 현상 문서화: 에포크 50 이후 14.8%p 성능 향상\n")
    sel.TypeText("3) YOLO11의 C2PSA 메커니즘이 YOLOv8 대비 47.2% 상대 향상\n")
    sel.TypeText("4) 제조업 AI 배포를 위한 실용적 가이드라인 제공\n\n")
    sel.TypeText("이러한 연구 결과는 데이터 부족이 제조업에서 AI 도입의 장벽이 될 필요가 없음을 보여준다.\n\n")
    
    # 표 16 복사 (최종 성능 평가)
    print("표 16 복사 중...")
    source_doc.Activate()
    source_doc.Tables(16).Range.Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("표 VII. 최종 성능 평가\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # 이미지 13 복사 (성능 요약)
    print("그림 8 (성능 요약) 복사 중...")
    source_doc.Activate()
    source_doc.InlineShapes(13).Select()
    word.Selection.Copy()
    time.sleep(0.5)
    template_doc.Activate()
    sel = word.Selection
    sel.Paste()
    sel.TypeParagraph()
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 8
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("그림 8. 성능 개선 요약\n\n")
    sel.ParagraphFormat.Alignment = 3
    
    # ===== 참고문헌 =====
    sel.Font.Name = "Helvetica"
    sel.Font.Size = 10
    sel.Font.Bold = True
    sel.ParagraphFormat.Alignment = 1
    sel.TypeText("참고문헌\n\n")
    sel.Font.Bold = False
    sel.ParagraphFormat.Alignment = 3
    
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 8
    refs = [
        '[1] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," Nature, vol. 521, no. 7553, pp. 436-444, 2015.',
        '[2] J. Deng et al., "ImageNet: A large-scale hierarchical image database," in Proc. IEEE CVPR, 2009, pp. 248-255.',
        '[3] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE CVPR, 2016, pp. 770-778.',
        '[4] D. Weimer et al., "Design of deep convolutional neural network architectures for automated feature extraction in industrial inspection," CIRP Ann., vol. 65, no. 1, pp. 417-420, 2016.',
        '[5] J. Redmon et al., "You only look once: Unified, real-time object detection," in Proc. IEEE CVPR, 2016, pp. 779-788.',
        '[6] A. Bochkovskiy et al., "YOLOv4: Optimal speed and accuracy of object detection," arXiv:2004.10934, 2020.',
        '[7] G. Jocher et al., "Ultralytics YOLOv8," https://github.com/ultralytics/ultralytics, 2023.',
        '[8] G. Jocher and A. Chaurasia, "Ultralytics YOLO11," https://github.com/ultralytics/ultralytics, 2024.',
        '[9] S. J. Pan and Q. Yang, "A survey on transfer learning," IEEE Trans. Knowl. Data Eng., vol. 22, no. 10, pp. 1345-1359, 2010.',
        '[10] J. Donahue et al., "DeCAF: A deep convolutional activation feature for generic visual recognition," in Proc. ICML, 2014, pp. 647-655.',
        '[11] A. S. Razavian et al., "CNN features off-the-shelf: An astounding baseline for recognition," in Proc. IEEE CVPRW, 2014, pp. 512-519.',
        '[12] J. Yosinski et al., "How transferable are features in deep neural networks?" in Proc. NeurIPS, 2014, pp. 3320-3328.',
        '[13] C. Shorten and T. M. Khoshgoftaar, "A survey on image data augmentation for deep learning," J. Big Data, vol. 6, no. 1, p. 60, 2019.',
        '[14] O. Vinyals et al., "Matching networks for one shot learning," in Proc. NeurIPS, 2016, pp. 3630-3638.',
        '[15] Z. Zou et al., "Object detection in 20 years: A survey," Proc. IEEE, vol. 111, no. 3, pp. 257-276, 2023.',
    ]
    for ref in refs:
        sel.TypeText(ref + "\n")
    
    # 문서 저장
    template_doc.SaveAs(output_path, 16)
    print(f"\n✅ 논문이 성공적으로 저장되었습니다!")
    print(f"📄 저장 위치: {output_path}")
    print(f"\n📋 포함된 내용:")
    print(f"   - 표 7개 (모두 원본에서 복사)")
    print(f"   - 그림 8개 (모두 원본에서 복사)")
    print(f"   - IEEE 2단 레이아웃")
    print(f"   - 한글 작성")
    
    source_doc.Close(False)
    template_doc.Close()
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    word.Quit()
