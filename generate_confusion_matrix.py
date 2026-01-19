import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# Confusion Matrix 데이터 (정규화됨)
# 논문의 통계 기반: Crack TP=82.5%, Melting TP=100%, Background TP=88.2%
# False negatives: Crack→Background 17.5%
# False positives: Background→Crack 11.8%

confusion_matrix = np.array([
    [0.825, 0.000, 0.175],  # crack 행
    [0.000, 1.000, 0.000],  # melting 행
    [0.118, 0.000, 0.882]   # background 행
])

# 클래스 레이블
classes = ['crack', 'melting', 'background']

# 그림 생성
fig, ax = plt.subplots(figsize=(10, 8))

# Heatmap 생성
sns.heatmap(confusion_matrix, 
            annot=True,           # 셀에 값 표시
            fmt='.2f',            # 소수점 2자리
            cmap='Blues',         # 파란색 계열 컬러맵
            xticklabels=classes,
            yticklabels=classes,
            vmin=0,
            vmax=1,
            cbar_kws={'label': ''},
            linewidths=2,
            linecolor='white',
            square=True,
            ax=ax)

# 레이블 및 제목 설정
ax.set_xlabel('True', fontsize=14, fontweight='bold')
ax.set_ylabel('Predicted', fontsize=14, fontweight='bold')
ax.set_title('Confusion Matrix Normalized', fontsize=16, fontweight='bold', pad=20)

# 축 레이블 폰트 크기 조정
ax.tick_params(axis='both', labelsize=12)

# 레이아웃 조정
plt.tight_layout()

# 이미지 저장
output_path = r'c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md\images\confusion_matrix_normalized.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Confusion Matrix 이미지가 저장되었습니다: {output_path}")

# 이미지 표시
plt.show()

# 통계 정보 출력
print("\n=== Confusion Matrix 통계 ===")
print(f"Crack 정확도 (TP): {confusion_matrix[0,0]:.1%}")
print(f"Melting 정확도 (TP): {confusion_matrix[1,1]:.1%}")
print(f"Background 정확도 (TP): {confusion_matrix[2,2]:.1%}")
print(f"\nCrack → Background (FN): {confusion_matrix[0,2]:.1%}")
print(f"Background → Crack (FP): {confusion_matrix[2,0]:.1%}")
print(f"\n전체 정확도: {np.trace(confusion_matrix)/len(classes):.1%}")
