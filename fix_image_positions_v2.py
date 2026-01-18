# -*- coding: utf-8 -*-
"""
IEEE 논문 이미지 위치 수정 스크립트 v2
원본 문서의 이미지를 올바른 위치에 배치
"""

import win32com.client
import time
import pythoncom

def fix_image_positions():
    pythoncom.CoInitialize()
    word = win32com.client.DispatchEx('Word.Application')
    word.Visible = True
    
    try:
        # 원본 문서 열기
        source_path = r'C:\국민대프로젝트\이규영 국민대 DPF 논문.docx'
        source_doc = word.Documents.Open(source_path)
        print("원본 문서 열기 완료")
        time.sleep(1)
        
        # 새 문서 생성
        target_doc = word.Documents.Add()
        print("새 문서 생성 완료")
        time.sleep(0.5)
        
        # 페이지 설정
        try:
            ps = target_doc.PageSetup
            ps.PageWidth = 612  # 8.5 inch = 612 points
            ps.PageHeight = 792  # 11 inch = 792 points
            ps.LeftMargin = 47
            ps.RightMargin = 47
            ps.TopMargin = 50
            ps.BottomMargin = 50
            ps.TextColumns.SetCount(2)
            ps.TextColumns.Spacing = 14.4
            print("페이지 설정 완료")
        except Exception as e:
            print(f"페이지 설정 경고: {e}")
        
        def add_text(text):
            """문서 끝에 텍스트 추가"""
            target_doc.Activate()
            word.Selection.EndKey(Unit=6)  # wdStory
            word.Selection.TypeText(text)
        
        def add_paragraph():
            """새 단락 추가"""
            target_doc.Activate()
            word.Selection.EndKey(Unit=6)
            word.Selection.TypeParagraph()
        
        def copy_image(shape_index):
            """원본에서 이미지 복사하여 타겟에 붙여넣기"""
            try:
                source_doc.Activate()
                time.sleep(0.2)
                source_doc.InlineShapes(shape_index).Select()
                word.Selection.Copy()
                time.sleep(0.3)
                
                target_doc.Activate()
                time.sleep(0.2)
                word.Selection.EndKey(Unit=6)
                word.Selection.Paste()
                time.sleep(0.3)
                return True
            except Exception as e:
                print(f"이미지 {shape_index} 복사 실패: {e}")
                return False
        
        # ============ 제목 ============
        add_text("도메인 브리지 전이학습을 활용한 소규모 데이터 기반 DPF 결함 검출:\n")
        add_text("YOLO11 기반 2단계 프레임워크\n\n")
        
        # ============ 저자 ============
        add_text("이규영\n")
        add_text("국민대학교 자동차공학과, 서울, 대한민국\n")
        add_text("Email: gylee@kookmin.ac.kr\n\n")
        
        # ============ 초록 ============
        add_text("초록—본 논문은 데이터가 제한된 제조 환경에서 디젤 미립자 필터(DPF) 결함 검출을 위한 새로운 2단계 도메인 브리지 전이학습 프레임워크를 제시한다. ")
        add_text("기존의 직접 전이학습 방식과 달리, 본 방법은 ImageNet 사전학습과 목표 DPF 검사 사이에 중간 도메인(X-ray 이미징)을 도입하여 효과적인 특징 공간 연결 경로를 생성한다. ")
        add_text("단 339장의 학습 이미지만으로 YOLO11s에서 91.7% mAP50을 달성했으며, 이는 기준선 학습 대비 34.8%p, 단일 단계 전이학습 대비 19.4%p 향상된 결과이다. ")
        add_text("실험 분석을 통해 최신 어텐션 기반 아키텍처에서 '늦은 개화(late blooming)' 현상을 발견했으며, 51-100 에포크 구간에서 14.8%p의 성능 향상이 발생하여 50 에포크 조기 종료 관행에 의문을 제기한다. ")
        add_text("YOLO11의 C2PSA 어텐션 메커니즘은 동일 학습 프로토콜에서 YOLOv8 대비 47.2% 상대적 개선을 보여준다.\n\n")
        
        add_text("핵심어—딥러닝, 결함 검출, 디젤 미립자 필터, 도메인 적응, 제조 품질 관리, 객체 검출, 전이학습, YOLO\n\n")
        
        # ============ I. 서론 ============
        add_text("I. 서론\n\n")
        
        add_text("제조 산업은 품질 관리에서 지속적인 과제에 직면해 있다: 제한된 학습 데이터로 신뢰할 수 있는 자동 결함 검출을 달성하는 것이다. ")
        add_text("전통적인 머신러닝 접근법은 허용 가능한 성능을 달성하기 위해 수천 개의 레이블링된 샘플이 필요하며, 이는 중소 규모 제조업체에게 상당한 장벽을 만든다. ")
        add_text("이러한 데이터 부족 문제는 DPF 품질 관리와 같은 특수 부품 검사에서 특히 심각한데, 결함 샘플이 본질적으로 희귀하고 수집 비용이 높기 때문이다.\n\n")
        
        add_text("DPF는 디젤 차량의 핵심 배출 제어 부품으로, 그 품질은 환경 규정 준수와 차량 성능에 직접적인 영향을 미친다. ")
        add_text("현재 검사 방법은 숙련된 기술자의 수동 육안 검사에 크게 의존하며, 이는 시간 소모적이고, 주관적이며, 인적 오류에 취약한 과정이다. ")
        add_text("주요 결함 유형인 균열과 용융 손상은 결함이 있는 제품이 최종 사용자에게 도달하는 것을 방지하기 위해 세심한 식별이 필요하다.\n\n")
        
        add_text("전이학습은 컴퓨터 비전 응용 분야에서 데이터 부족 문제에 대한 유망한 해결책으로 부상했다. ")
        add_text("ImageNet과 같은 대규모 데이터셋에서 사전 학습된 모델을 활용함으로써, 연구자들은 제한된 데이터로 다양한 도메인에서 상당한 개선을 달성했다. ")
        add_text("그러나 전이학습의 효과는 소스와 타겟 도메인 간의 유사성에 크게 의존하며—이 요소는 산업 검사 작업에서 체계적으로 탐구되지 않았다.\n\n")
        
        add_text("본 논문에서는 이러한 한계를 해결하는 2단계 도메인 브리지 전이학습 프레임워크를 제안한다. ")
        add_text("ImageNet에서 DPF 검사로 직접 전이하는 대신, 소스와 타겟 도메인 모두와 구조적 유사성을 공유하는 중간 도메인(X-ray 결함 검출)을 도입한다. ")
        add_text("이 브리지 접근법은 더 점진적인 특징 공간 전환을 생성하여 최소한의 데이터로 더 효과적인 지식 전이를 가능하게 한다.\n\n")
        
        add_text("주요 기여는 다음과 같다:\n")
        add_text("• 339장의 학습 이미지만으로 91.7% mAP50을 달성하는 새로운 도메인 브리지 전이학습 프레임워크\n")
        add_text("• 어텐션 기반 아키텍처에서 '늦은 개화' 현상의 발견 및 문서화\n")
        add_text("• 동일 프로토콜에서 YOLO11과 YOLOv8의 포괄적 비교\n")
        add_text("• 데이터 제한 환경에서의 제조 AI 배포를 위한 실용적 가이드라인\n\n")
        
        # ============ 그림 1 삽입 (제안 방법론 흐름도) - InlineShape 2 ============
        print("그림 1 (방법론 흐름도) 복사 중...")
        if copy_image(2):
            add_text("\n그림 1. 제안하는 도메인 브리지 전이학습 프레임워크의 전체 구조.\n\n")
        
        # ============ II. 관련 연구 ============
        add_text("II. 관련 연구\n\n")
        
        add_text("A. 제조 검사에서의 딥러닝\n\n")
        add_text("딥러닝은 다양한 제조 분야에서 자동화된 시각 검사에 혁명을 일으켰다. ")
        add_text("합성곱 신경망(CNN)은 결함 검출 작업에서 수작업 특징 기반의 전통적인 머신 비전 접근법을 능가하는 놀라운 성공을 보여주었다. ")
        add_text("객체 검출 아키텍처, 특히 YOLO 계열은 실시간 추론 능력과 경쟁력 있는 정확도로 인해 인기를 얻었다.\n\n")
        
        add_text("B. 전이학습 전략\n\n")
        add_text("전이학습은 제한된 데이터로 딥러닝 모델을 학습시키기 위한 사실상의 표준 접근법이 되었다. ")
        add_text("도메인 유사성은 전이 효과에서 중요한 역할을 한다. ")
        add_text("Yosinski 등은 초기 CNN 레이어의 특징이 대체로 일반적이고 전이 가능하며, 깊은 레이어는 점점 더 작업 특화된다는 것을 입증했다.\n\n")
        
        # ============ III. 제안 방법 ============
        add_text("III. 제안 방법\n\n")
        
        add_text("A. 도메인 브리지 전이학습 프레임워크\n\n")
        add_text("제안하는 프레임워크는 두 개의 순차적 전이 단계로 구성되며, 중간 도메인이 범용 ImageNet 특징과 특화된 DPF 결함 검출 작업 사이의 브리지 역할을 한다.\n\n")
        
        add_text("Stage 1 (도메인 브리지): ImageNet 사전학습된 YOLO11s 모델을 균열 및 기공 주석이 있는 310장의 이미지를 포함하는 X-ray 결함 검출 데이터셋에서 파인튜닝한다.\n\n")
        
        add_text("Stage 2 (타겟 적응): X-ray 사전학습된 모델을 DPF 데이터셋(339장, 2클래스: Crack, Melting)에서 추가 파인튜닝한다.\n\n")
        
        add_text("B. YOLO11 아키텍처 분석\n\n")
        add_text("YOLO11s는 C2PSA(Cross Stage Partial with Spatial Attention) 모듈을 도입한다. ")
        add_text("C2PSA 아키텍처는 세 가지 병렬 처리 경로로 구성된다: 공간 어텐션 경로, 채널 어텐션 경로, 컨텍스트 집계 경로.\n\n")
        
        add_text("C. 학습 구성\n\n")
        add_text("• 옵티마이저: AdamW (weight decay 0.0005)\n")
        add_text("• 학습률: 초기 0.01, 코사인 어닐링으로 0.0001까지\n")
        add_text("• 배치 크기: 16\n")
        add_text("• 입력 해상도: 640×640 픽셀\n")
        add_text("• 학습 에포크: Stage 1은 50, Stage 2는 100\n\n")
        
        # ============ IV. 실험 설정 ============
        add_text("IV. 실험 설정\n\n")
        
        add_text("A. 데이터셋\n\n")
        add_text("DPF 결함 데이터셋: 339장의 학습 이미지와 66장의 검증 이미지, 두 가지 결함 클래스(Crack, Melting).\n")
        add_text("X-ray 결함 데이터셋: 균열 및 기공 결함 주석이 있는 310장의 이미지.\n\n")
        
        # ============ 그림 2 삽입 (데이터 증강 분석) - InlineShape 9 ============
        print("그림 2 (데이터 증강) 복사 중...")
        if copy_image(9):
            add_text("\n그림 2. DPF 데이터셋의 증강 전략 및 클래스 분포.\n\n")
        
        add_text("B. 평가 지표\n\n")
        add_text("• mAP50: IoU 임계값 0.5에서의 평균 정밀도\n")
        add_text("• mAP50-95: IoU 임계값 0.5에서 0.95까지의 평균 AP\n")
        add_text("• Precision, Recall, F1-Score\n\n")
        
        # ============ V. 실험 결과 ============
        add_text("V. 실험 결과\n\n")
        
        add_text("A. 전체 성능 비교\n\n")
        add_text("YOLO11s는 91.7% mAP50을 달성하여 YOLOv8s(62.3%) 대비 29.4%p의 절대적 개선을 보인다. ")
        add_text("이는 15.3% 적은 파라미터(9.4M vs 11.1M)를 사용하면서 47.2%의 상대적 성능 향상에 해당한다.\n\n")
        
        add_text("표 I. YOLO11 vs YOLOv8 최종 성능 비교\n")
        add_text("Model    | Params | mAP50 | mAP50-95 | Precision | Recall | F1\n")
        add_text("YOLOv8s  | 11.1M  | 62.3% |  37.8%   |   71.8%   | 68.5%  | 0.70\n")
        add_text("YOLO11s  |  9.4M  | 91.7% |  54.2%   |   92.8%   | 82.5%  | 0.87\n\n")
        
        add_text("B. 전이학습 효과\n\n")
        add_text("표 II. 전이학습 전략 비교 (YOLO11s)\n")
        add_text("Strategy       | Pre-training Path        | mAP50  | Gain\n")
        add_text("Baseline       | Random → DPF             | 56.9%  |   —\n")
        add_text("Direct Transfer| ImageNet → DPF           | 72.3%  | +15.4%p\n")
        add_text("Domain Bridge  | ImageNet → X-ray → DPF   | 91.7%  | +34.8%p\n\n")
        
        # ============ 그림 3 삽입 (전이학습 비교) - InlineShape 7 ============
        print("그림 3 (전이학습 비교) 복사 중...")
        if copy_image(7):
            add_text("\n그림 3. 세 가지 전이학습 시나리오의 최종 성능 비교.\n\n")
        
        add_text("C. 늦은 개화 현상 분석\n\n")
        add_text("50 에포크에서 YOLO11s는 76.9% mAP50을 달성한다. ")
        add_text("그러나 100 에포크까지 학습을 계속하면 91.7%에 도달한다. ")
        add_text("이 14.8%p 향상은 최종 성능의 19.2%가 학습 후반부에 발생한다는 것을 의미한다.\n\n")
        
        add_text("표 III. 에포크별 성능 진행\n")
        add_text("Epoch | YOLO11s mAP50 | YOLOv8s mAP50 | Difference | Phase\n")
        add_text("  1   |    37.2%      |    35.1%      |   +2.1%p   | Phase 1\n")
        add_text(" 25   |    69.1%      |    58.3%      |  +10.8%p   | Phase 1\n")
        add_text(" 50   |    76.9%      |    62.1%      |  +14.8%p   | Phase 2\n")
        add_text(" 75   |    89.5%      |    62.2%      |  +27.3%p   | Phase 3\n")
        add_text("100   |    91.7%      |    62.3%      |  +29.4%p   | Phase 4\n\n")
        
        # ============ 그림 4 삽입 (학습 곡선) - InlineShape 3 ============
        print("그림 4 (학습 곡선) 복사 중...")
        if copy_image(3):
            add_text("\n그림 4. YOLO11의 100 에포크 학습 과정. 빨간색 상자는 조기 종료 지점(Epoch 50)을 표시한다.\n\n")
        
        add_text("D. 클래스별 성능 분석\n\n")
        add_text("표 IV. 클래스별 성능 비교\n")
        add_text("Class   | Model   |   AP   | Precision | Recall\n")
        add_text("Crack   | YOLOv8s | 61.8%  |   68.5%   | 71.2%\n")
        add_text("Crack   | YOLO11s | 91.2%  |  100.0%   | 82.5%\n")
        add_text("Melting | YOLOv8s | 62.8%  |   75.1%   | 65.8%\n")
        add_text("Melting | YOLO11s | 92.2%  |   85.6%   | 81.9%\n\n")
        
        # ============ 그림 5 삽입 (혼동 행렬) - InlineShape 6 ============
        print("그림 5 (혼동 행렬) 복사 중...")
        if copy_image(6):
            add_text("\n그림 5. YOLO11의 정규화된 혼동 행렬.\n\n")
        
        # ============ 그림 6 삽입 (PR 곡선) - InlineShape 11 ============
        print("그림 6 (PR 곡선) 복사 중...")
        if copy_image(11):
            add_text("\n그림 6. YOLO11의 클래스별 Precision-Recall 곡선.\n\n")
        
        add_text("E. 시각적 결과 분석\n\n")
        
        # ============ 그림 7 삽입 (검증 예측 결과) - InlineShape 10 ============
        print("그림 7 (검증 예측 결과) 복사 중...")
        if copy_image(10):
            add_text("\n그림 7. YOLO11의 실제 검증 이미지 예측 결과.\n\n")
        
        # ============ 그림 8 삽입 (추가 검증 결과) - InlineShape 13 ============
        print("그림 8 (추가 검증 결과) 복사 중...")
        if copy_image(13):
            add_text("\n그림 8. 두 번째 검증 배치의 예측 결과.\n\n")
        
        # ============ VI. 토론 ============
        add_text("VI. 토론\n\n")
        
        add_text("A. 핵심 발견 해석\n\n")
        add_text("도메인 브리지 전이학습의 우월성은 특징 공간 전환의 관점에서 설명할 수 있다. ")
        add_text("ImageNet에서 DPF로 직접 전이할 때, 모델은 큰 도메인 갭을 연결해야 한다. ")
        add_text("중간 X-ray 결함 도메인을 도입함으로써 특징 공간을 통한 더 점진적인 전환 경로를 만든다.\n\n")
        
        add_text("YOLO11에서의 늦은 개화 현상은 C2PSA 어텐션 메커니즘의 복잡성에 기인할 수 있다. ")
        add_text("세 가지 병렬 어텐션 경로는 최적의 시너지를 달성하기 위해 확장된 학습이 필요하다.\n\n")
        
        # ============ 그림 9 삽입 (성능 개선 요약) - InlineShape 14 ============
        print("그림 9 (성능 개선 요약) 복사 중...")
        if copy_image(14):
            add_text("\n그림 9. 본 연구의 핵심 성과 종합 시각화.\n\n")
        
        add_text("B. 제조업을 위한 실용적 함의\n\n")
        add_text("1) 데이터 요구사항: 339장의 이미지로 91.7% mAP50 달성\n")
        add_text("2) 학습 기간: 50 에포크 조기 종료는 어텐션 기반 아키텍처의 잠재력을 과소평가\n\n")
        
        add_text("C. 한계 및 향후 연구\n\n")
        add_text("1) 실시간 추론: 현재 CPU 추론 속도(~6.9 FPS)는 개선 필요\n")
        add_text("2) 일반화: 다중 제조업체 검증 필요\n")
        add_text("3) 클래스 범위: 추가 결함 유형으로 확장 필요\n\n")
        
        # ============ VII. 결론 ============
        add_text("VII. 결론\n\n")
        
        add_text("본 논문은 339장의 학습 이미지만으로 DPF 결함 검출에서 91.7% mAP50을 달성하는 도메인 브리지 전이학습 프레임워크를 제시한다.\n\n")
        
        add_text("주요 기여:\n")
        add_text("1) 중간 X-ray 도메인을 활용한 2단계 전이학습 (직접 전이 대비 +19.4%p)\n")
        add_text("2) 어텐션 기반 아키텍처의 '늦은 개화' 현상 문서화 (50 에포크 이후 14.8%p 향상)\n")
        add_text("3) YOLO11 C2PSA가 YOLOv8 대비 47.2% 상대적 개선\n")
        add_text("4) 제조 AI 배포를 위한 실용적 가이드라인\n\n")
        
        add_text("이러한 결과는 적절한 전이학습 전략으로 제한된 샘플에서도 고성능 자동 검사가 달성 가능함을 보여준다.\n\n")
        
        # ============ 참고문헌 ============
        add_text("참고문헌\n\n")
        
        references = [
            '[1] Y. LeCun et al., "Deep learning," Nature, vol. 521, pp. 436-444, 2015.',
            '[2] J. Deng et al., "ImageNet: A large-scale hierarchical image database," CVPR, 2009.',
            '[3] D. Weimer et al., "Design of deep CNN architectures for automated feature extraction," CIRP Ann., 2016.',
            '[4] Z. Zou et al., "Object detection in 20 years: A survey," Proc. IEEE, 2023.',
            '[5] J. Redmon et al., "You only look once: Unified, real-time object detection," CVPR, 2016.',
            '[6] A. Bochkovskiy et al., "YOLOv4: Optimal speed and accuracy," arXiv:2004.10934, 2020.',
            '[7] G. Jocher et al., "Ultralytics YOLOv8," https://github.com/ultralytics/ultralytics, 2023.',
            '[8] G. Jocher et al., "Ultralytics YOLO11," https://github.com/ultralytics/ultralytics, 2024.',
            '[9] S. J. Pan and Q. Yang, "A survey on transfer learning," IEEE TKDE, 2010.',
            '[10] J. Yosinski et al., "How transferable are features in deep neural networks?" NeurIPS, 2014.',
        ]
        
        for ref in references:
            add_text(ref + "\n")
        
        # 저장
        output_path = r'C:\국민대프로젝트\IEEE_DPF_Paper_Korean_Final_Rev5.docx'
        target_doc.SaveAs(output_path)
        print(f"\n✅ 논문이 성공적으로 저장되었습니다!")
        print(f"📄 저장 위치: {output_path}")
        
        # 문서 닫기
        source_doc.Close(False)
        target_doc.Close(True)
        
    except Exception as e:
        print(f"오류 발생: {e}")
        import traceback
        traceback.print_exc()
    finally:
        try:
            word.Quit()
        except:
            pass
        pythoncom.CoUninitialize()

if __name__ == "__main__":
    fix_image_positions()
