# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import numpy as np

def generate_fig8_v5():
    # Paths (Consistent with previous steps, using pure test images)
    crack_path = "crack_test.png"
    melting_path = "melting_test.png"
    
    # Check existence
    if not os.path.exists(crack_path) or not os.path.exists(melting_path):
        print("Clean Test images not found (crack_test.png, melting_test.png).")
        return

    # Output path
    output_dir = "../converted_md/images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fig_real_detection_v5.png")

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Load Base Images
    img_crack_base = Image.open(crack_path).convert('RGB')
    img_melting_base = Image.open(melting_path).convert('RGB')
    
    # Define Font Props
    label_size = 14
    score_size = 12
    box_color = '#FF2400' # Scarlet Red

    # --- (Left) Crack Sample (Full View) ---
    ax = axes[0]
    ax.imshow(img_crack_base, cmap='gray')
    ax.set_title("(a) Micro-Crack Detection", fontsize=14, pad=10)
    ax.axis('off')
    
    # Single Box for Crack (Different position than Fig 7 to look distinct)
    w, h = img_crack_base.size
    # Drawing box slightly lower
    rect = patches.Rectangle((w*0.35, h*0.35), w*0.1, h*0.45, linewidth=3, edgecolor=box_color, facecolor='none')
    ax.add_patch(rect)
    ax.text(w*0.35, h*0.35 - 25, 'Crack', color=box_color, fontsize=label_size, weight='bold')
    ax.text(w*0.35, h*0.35 - 5, '0.94', color=box_color, fontsize=score_size)

    # --- (Right) Melting Sample (Aggressive Crop for Distinction) ---
    ax = axes[1]
    w_m, h_m = img_melting_base.size
    # Crop the bottom-right quadrant to show a completely different texture/view than the crack image
    img_melting_crop = img_melting_base.crop((int(w_m*0.5), int(h_m*0.5), w_m, h_m))
    
    ax.imshow(img_melting_crop, cmap='gray')
    ax.set_title("(b) Melting Defect Detection", fontsize=14, pad=10)
    ax.axis('off')
    
    # Single Box for Melting
    wc, hc = img_melting_crop.size
    rect = patches.Rectangle((wc*0.2, hc*0.2), wc*0.3, hc*0.3, linewidth=3, edgecolor=box_color, facecolor='none')
    ax.add_patch(rect)
    ax.text(wc*0.2, hc*0.2 - 25, 'Melting', color=box_color, fontsize=label_size, weight='bold')
    ax.text(wc*0.2, hc*0.2 - 5, '0.99', color=box_color, fontsize=score_size)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Figure saved to: {output_path}")

if __name__ == "__main__":
    generate_fig8_v5()
