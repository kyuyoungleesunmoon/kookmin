import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager, rc

# 폰트 설정 (한글 지원)
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows 기본 폰트
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def create_korean_diagram():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # 스타일 설정
    box_props = dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#333', linewidth=1.5)
    arrow_props = dict(arrowstyle='->', lw=1.5, color='#333')
    
    # 박스 데이터 (중심 x, 중심 y, 텍스트, 색상)
    # 레이아웃:
    # [원본 데이터] -> [적응형 증강] -> [X-ray 변환]
    #      |               |              |
    #      V               V              V
    # [라벨 검증] -> [증강 데이터셋] -> [모델 학습] -> [최종 성능]
    
    boxes = [
        # Row 1
        {'id': 'orig', 'x': 1.5, 'y': 4.8, 'text': "원본 데이터셋\n(16장)\n\nCrack: 14\nMelting: 2", 'color': '#fff0f0'},
        {'id': 'aug_method', 'x': 5.0, 'y': 4.8, 'text': "적응형 증강 기법\n(Adaptive Augmentation)\n\n$I(c) = \\alpha \log(N_{max}/N_c) + \\beta$", 'color': '#f0f8ff'},
        {'id': 'xray', 'x': 8.5, 'y': 4.8, 'text': "X-ray 특화 변환\n\n• CLAHE\n• 감마 보정\n• 가우시안 노이즈", 'color': '#f0fff0'},
        
        # Row 2
        {'id': 'iou', 'x': 1.5, 'y': 2.0, 'text': "라벨 검증\n(IoU 기반)\n\n정확도: 97.3%", 'color': '#fff9e6'},
        {'id': 'dataset', 'x': 5.0, 'y': 2.0, 'text': "최종 데이터셋\n(339장)\n\n클래스 균형 확보", 'color': '#f3e6ff'},
        {'id': 'train', 'x': 8.5, 'y': 2.0, 'text': "모델 학습\n(YOLO11/YOLOv8)\n\nOptimizer: AdamW", 'color': '#e6ffff'},
        
        # Result
        {'id': 'result', 'x': 8.5, 'y': 0.6, 'text': "최종 성능\n\nmAP50: 91.7%", 'color': '#ffe6f2'}
    ]
    
    # 박스 그리기
    box_objs = {}
    for b in boxes:
        # FancyBboxPatch 대신 text의 bbox 속성 사용이 더 간단하지만, 제어를 위해 FancyBbox 사용은 복잡할 수 있음.
        # 여기선 text에 bbox를 씌우는 방식으로 진행 (좌표 자동 계산)
        t = ax.text(b['x'], b['y'], b['text'], ha='center', va='center', fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.5', facecolor=b['color'], edgecolor='#333', linewidth=1.5))
        box_objs[b['id']] = t

    # 화살표 그리기 함수
    def connect(id1, id2, connectionstyle="arc3,rad=0"):
        # Get bbox via renderer is tricky without drawing first.
        # Simple annotation with arrow
        ax.annotate("", 
                    xy=(boxes[get_idx(id2)]['x'], boxes[get_idx(id2)]['y']), # To (center - offset will be handled by arrowprops shrinking)
                    xytext=(boxes[get_idx(id1)]['x'], boxes[get_idx(id1)]['y']), # From
                    arrowprops=dict(arrowstyle="->", lw=1.5, color='#333', shrinkA=25, shrinkB=25, connectionstyle=connectionstyle))

    def get_idx(key):
        for i, b in enumerate(boxes):
            if b['id'] == key: return i
        return -1

    # 연결
    # 1. 가로 연결 (Row 1)
    connect('orig', 'aug_method')
    connect('aug_method', 'xray')
    
    # 2. 세로 연결
    connect('orig', 'iou')
    connect('aug_method', 'dataset')
    connect('xray', 'train')
    
    # 3. 가로 연결 (Row 2)
    connect('iou', 'dataset')
    connect('dataset', 'train')
    
    # 4. 결과 연결
    connect('train', 'result')

    plt.suptitle("그림 1. 제안하는 DPF 결함 검출 프레임워크 흐름도", fontsize=14, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    save_path = r'C:\국민대프로젝트\architecture_diagram_korean.png'
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Diagram saved: {save_path}")

if __name__ == "__main__":
    create_korean_diagram()
