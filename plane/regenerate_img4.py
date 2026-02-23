"""
이규영_국민대_DPF_논문_img_4.png 재생성 스크립트
- 2-panel 구성: 왼쪽(Training Performance 곡선), 오른쪽(Final Performance Metrics 바 차트)
- 원본 이미지를 정확히 재현 + 논문용 대형 폰트 적용
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
ANNOTATION_SIZE = 17
LEGEND_SIZE = 17
BAR_VALUE_SIZE = 18

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

def regenerate_img4():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), 
                                     gridspec_kw={'width_ratios': [1.2, 1], 'wspace': 0.35})
    
    # ==========================================
    # 왼쪽 패널: DPF Multiclass Training Performance
    # 원본 재현: 파란 실선(학습 곡선) + 파란 점선(trend line)
    # 빨간선 없음
    # ==========================================
    
    np.random.seed(42)
    epochs = np.arange(0, 51)
    
    # 원본 이미지에서 육안으로 읽은 key points
    # 특징: 초반 급등 → 소폭 dip → 꾸준한 상승 → 수렴
    key_points = {
        0: 0.000,
        1: 0.005,
        2: 0.012,   # Starting Point
        3: 0.04,
        4: 0.08,
        5: 0.10,
        6: 0.09,    # 약간 dip (원본에서 보이는 특징)
        7: 0.10,
        8: 0.12,
        9: 0.13,
        10: 0.15,
        12: 0.18,
        15: 0.23,
        18: 0.28,
        20: 0.32,
        22: 0.36,
        25: 0.40,
        28: 0.44,
        30: 0.47,
        32: 0.49,
        35: 0.52,
        37: 0.54,
        40: 0.56,
        42: 0.58,
        45: 0.60,
        47: 0.61,
        48: 0.615,
        49: 0.62,
        50: 0.623,   # Final Point
    }
    
    # 키 포인트를 interpolation하여 전체 곡선 생성
    kp_epochs = list(key_points.keys())
    kp_values = list(key_points.values())
    map_values = np.interp(epochs, kp_epochs, kp_values)
    
    # 약간의 노이즈 추가 (원본처럼 자연스러운 진동)
    noise = np.random.normal(0, 0.006, len(epochs))
    noise[0] = 0
    noise[1] = 0
    noise[-1] = 0
    map_values_noisy = np.clip(map_values + noise, 0, 0.65)
    map_values_noisy[0] = 0.0
    map_values_noisy[-1] = 0.623
    map_values_noisy[2] = 0.012

    
    # 파란 굵은 실선: 실제 학습 곡선 (mAP50)
    ax1.plot(epochs, map_values_noisy, 'b-', linewidth=2.5, alpha=0.8, label='mAP50')

    
    # Starting Point 어노테이션 (왼쪽 하단, 원본 위치 재현)
    ax1.annotate('Starting Point\n(mAP50: 1.2%)',
                xy=(2, 0.012), xytext=(8, 0.10),
                fontsize=ANNOTATION_SIZE - 1, family=font_family,
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'),
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.8))
    
    # Final Point 어노테이션 (우상단, 원본 위치 재현)
    ax1.annotate('Final Point\n(mAP50: 62.3%)',
                xy=(49, 0.620), xytext=(33, 0.56),
                fontsize=ANNOTATION_SIZE - 1, family=font_family,
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'),
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.8))
    
    ax1.set_title('DPF Multiclass Training Performance', 
                  fontsize=TITLE_SIZE, fontweight='bold', family=font_family, pad=15)
    ax1.set_xlabel('Epoch', fontsize=LABEL_SIZE, family=font_family)
    ax1.set_ylabel('mAP50 Score', fontsize=LABEL_SIZE, family=font_family)
    ax1.set_xlim(-1, 52)
    ax1.set_ylim(-0.02, 0.72)
    ax1.tick_params(labelsize=TICK_SIZE)
    ax1.grid(False)
    
    # ==========================================
    # 오른쪽 패널: Final Performance Metrics
    # ==========================================
    metrics = ['Precision', 'Recall', 'mAP50', 'mAP50-95']
    values = [0.819, 0.542, 0.623, 0.320]
    colors = ['#FF6B6B', '#6BCABA', '#4ECDC4', '#95C9A8']
    
    bars = ax2.bar(metrics, values, color=colors, width=0.65, edgecolor='gray', linewidth=0.5)
    
    # 바 위에 값 표시
    for bar, val in zip(bars, values):
        ax2.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 0.02,
                f'{val:.3f}', ha='center', va='bottom', 
                fontsize=BAR_VALUE_SIZE, fontweight='bold', family=font_family)
    
    ax2.set_title('Final Performance Metrics', 
                  fontsize=TITLE_SIZE, fontweight='bold', family=font_family, pad=15)
    ax2.set_ylabel('Score', fontsize=LABEL_SIZE, family=font_family)
    ax2.set_ylim(0, 1.08)
    ax2.tick_params(axis='x', labelsize=TICK_SIZE - 1, rotation=0)
    ax2.tick_params(axis='y', labelsize=TICK_SIZE)
    ax2.grid(False)
    
    # ------------------------------------------
    # 저장
    # ------------------------------------------
    plt.tight_layout(pad=2.0)
    
    save_path = os.path.join(output_dir, "이규영_국민대_DPF_논문_img_4.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0.3, 
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Generated: {save_path}")

if __name__ == "__main__":
    regenerate_img4()
