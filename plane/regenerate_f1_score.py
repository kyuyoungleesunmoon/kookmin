"""
fig_f1_score_analysis.png 재생성 스크립트
- 2-panel 구성:
  (a) Radar Chart: YOLOv8 vs YOLO11 Overall Performance Comparison
  (b) Grouped Bar Chart: Class-wise Performance (YOLO11)
- 원본 이미지를 정확히 재현 + 논문용 대형 폰트
"""
import matplotlib.pyplot as plt
import numpy as np
import os

# ============================================
# 폰트 크기 설정 (논문용 대형 폰트)
# ============================================
TITLE_SIZE = 24
LABEL_SIZE = 20
TICK_SIZE = 17
ANNOTATION_SIZE = 16
LEGEND_SIZE = 16
BAR_VALUE_SIZE = 16

font_family = 'serif'

plt.rcParams.update({
    'font.family': font_family,
    'font.size': TICK_SIZE,
    'axes.titlesize': TITLE_SIZE,
    'axes.labelsize': LABEL_SIZE,
    'xtick.labelsize': TICK_SIZE,
    'ytick.labelsize': TICK_SIZE,
    'legend.fontsize': LEGEND_SIZE
})

# ============================================
# 출력 경로
# ============================================
output_dir = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md\images"

def regenerate_f1_score():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8),
                                     gridspec_kw={'width_ratios': [1, 1], 'wspace': 0.35},
                                     subplot_kw={'projection': None})
    # ax1을 polar로 교체
    ax1.remove()
    ax1 = fig.add_subplot(1, 2, 1, projection='polar')

    # ==========================================
    # (a) Radar Chart: Overall Performance Comparison
    # ==========================================
    categories = ['mAP50-95', 'mAP50', 'F1 Score', 'Recall', 'Precision']
    N = len(categories)

    # 원본 이미지에서 읽은 데이터 (퍼센트 단위)
    # 축 순서: mAP50-95, mAP50, F1 Score, Recall, Precision
    # YOLOv8s (회색 점선 - mAP50 높고, 나머지 중간~낮음)
    yolov8_values = [45.0, 93.0, 28.0, 30.0, 50.0]
    # YOLO11s (파란 실선 - mAP50-95 높고, mAP50도 높고, Precision 높음, F1/Recall 낮음)
    yolo11_values = [93.0, 95.0, 10.0, 30.0, 90.0]

    # 각도 계산 (5각형)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    
    # 닫힌 다각형을 위해 첫 값 반복
    yolov8_values_closed = yolov8_values + [yolov8_values[0]]
    yolo11_values_closed = yolo11_values + [yolo11_values[0]]
    angles_closed = angles + [angles[0]]

    # Radar chart 설정
    ax1.set_theta_offset(np.pi / 2)  # 12시 방향 시작
    ax1.set_theta_direction(-1)       # 시계 방향

    # 그리드 설정
    ax1.set_ylim(0, 100)
    ax1.set_yticks([20, 40, 60, 80, 100])
    ax1.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=TICK_SIZE - 4, color='gray')

    # 카테고리 라벨
    ax1.set_xticks(angles)
    ax1.set_xticklabels(categories, fontsize=LABEL_SIZE - 2, fontweight='bold', family=font_family)

    # YOLOv8s (회색 점선, 마커: 회색 원)
    ax1.plot(angles_closed, yolov8_values_closed, 'o--', color='gray', linewidth=2.0,
             markersize=7, markerfacecolor='gray', label='YOLOv8s')

    # YOLO11s (파란 실선 + 채움, 마커: 파란 원)
    ax1.plot(angles_closed, yolo11_values_closed, 'o-', color='#2196F3', linewidth=2.5,
             markersize=7, markerfacecolor='#2196F3', label='YOLO11s (Ours)')
    ax1.fill(angles_closed, yolo11_values_closed, alpha=0.15, color='#2196F3')

    # 범례
    ax1.legend(loc='upper right', bbox_to_anchor=(1.15, 1.12), fontsize=LEGEND_SIZE,
               framealpha=0.9, edgecolor='gray')

    # 제목
    ax1.set_title('(a) Overall Performance Comparison\n(YOLOv8 vs YOLO11)',
                  fontsize=TITLE_SIZE - 2, fontweight='bold', family=font_family,
                  pad=30, y=1.08)

    # ==========================================
    # (b) Grouped Bar Chart: Class-wise Performance (YOLO11)
    # ==========================================
    classes = ['Crack', 'Melting']
    precision_vals = [100.0, 85.6]
    recall_vals = [82.5, 81.9]
    ap_vals = [91.2, 92.2]

    x = np.arange(len(classes))
    bar_width = 0.22

    # 바 그리기
    bars1 = ax2.bar(x - bar_width, precision_vals, bar_width, color='#4CAF50',
                    edgecolor='white', linewidth=0.5, label='Precision')
    bars2 = ax2.bar(x, recall_vals, bar_width, color='#FF9800',
                    edgecolor='white', linewidth=0.5, label='Recall')
    bars3 = ax2.bar(x + bar_width, ap_vals, bar_width, color='#D32F2F',
                    edgecolor='white', linewidth=0.5, label='AP')

    # 바 위에 값 표시 (겹침 방지를 위한 오프셋 조정)
    for bar, val in zip(bars1, precision_vals):
        ax2.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 1.5,
                f'{val:.1f}%', ha='center', va='bottom',
                fontsize=BAR_VALUE_SIZE, fontweight='bold', family=font_family,
                color='#388E3C')
    for bar, val in zip(bars2, recall_vals):
        ax2.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 1.5,
                f'{val:.1f}%', ha='center', va='bottom',
                fontsize=BAR_VALUE_SIZE, fontweight='bold', family=font_family,
                color='#E65100')
    for bar, val in zip(bars3, ap_vals):
        ax2.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 1.5,
                f'{val:.1f}%', ha='center', va='bottom',
                fontsize=BAR_VALUE_SIZE, fontweight='bold', family=font_family,
                color='#B71C1C')

    # 축 설정
    ax2.set_title('(b) Class-wise Performance (YOLO11)',
                  fontsize=TITLE_SIZE - 2, fontweight='bold', family=font_family, pad=15)
    ax2.set_ylabel('Score (%)', fontsize=LABEL_SIZE, family=font_family)
    ax2.set_xticks(x)
    ax2.set_xticklabels(classes, fontsize=LABEL_SIZE, family=font_family)
    ax2.set_ylim(0, 110)
    ax2.tick_params(axis='y', labelsize=TICK_SIZE)
    ax2.grid(False)

    # 범례
    ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=3,
               fontsize=LEGEND_SIZE, framealpha=0.9, edgecolor='gray')

    # ------------------------------------------
    # 저장
    # ------------------------------------------
    plt.tight_layout(pad=2.0)

    save_path = os.path.join(output_dir, "fig_f1_score_analysis.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0.3,
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Generated: {save_path}")

if __name__ == "__main__":
    regenerate_f1_score()
