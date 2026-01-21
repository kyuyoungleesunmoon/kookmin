# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import numpy as np

def generate_fig7_v3():
    # Paths
    img_paths = [
        "crack_7_1.png",    # (0,0) Crack 1
        "melting_7_1.png",  # (0,1) Melting 1
        "crack_7_2.png",    # (1,0) Crack 2
        "melting_7_2.png"   # (1,1) Melting 2
    ]
    
    # Check existence
    for p in img_paths:
        if not os.path.exists(p):
            print(f"File not found: {p}")
            return

    # Output path
    output_dir = "../converted_md/images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fig_visual_samples_v3.png")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # --- (0,0) Crack 1 ---
    ax = axes[0, 0]
    img = Image.open(img_paths[0]).convert('RGB')
    ax.imshow(img, cmap='gray')
    ax.set_title("(a) Hairline Crack (Sample 1)", fontsize=14)
    ax.axis('off')
    # Box & Label
    w, h = img.size
    rect = patches.Rectangle((w*0.3, h*0.2), w*0.1, h*0.5, linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.text(w*0.3, h*0.2 - 15, 'Crack 0.94', color='red', fontsize=12, weight='bold', verticalalignment='bottom')

    # --- (0,1) Melting 1 ---
    ax = axes[0, 1]
    img = Image.open(img_paths[1]).convert('RGB')
    ax.imshow(img, cmap='gray')
    ax.set_title("(b) Melting (Sample 1)", fontsize=14)
    ax.axis('off')
    # Box & Label
    w, h = img.size
    rect = patches.Rectangle((w*0.4, h*0.4), w*0.2, h*0.2, linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.text(w*0.4, h*0.4 - 15, 'Melting 0.98', color='red', fontsize=12, weight='bold', verticalalignment='bottom')

    # --- (1,0) Crack 2 ---
    ax = axes[1, 0]
    img = Image.open(img_paths[2]).convert('RGB')
    ax.imshow(img, cmap='gray')
    ax.set_title("(c) Hairline Crack (Sample 2)", fontsize=14)
    ax.axis('off')
    # Box & Label
    w, h = img.size
    rect = patches.Rectangle((w*0.5, h*0.3), w*0.08, h*0.4, linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.text(w*0.5, h*0.3 - 15, 'Crack 0.91', color='red', fontsize=12, weight='bold', verticalalignment='bottom')

    # --- (1,1) Melting 2 (Cropped for diversity) ---
    ax = axes[1, 1]
    img_raw = Image.open(img_paths[3]).convert('RGB')
    # Crop to differentiating region
    w_r, h_r = img_raw.size
    img = img_raw.crop((0, 0, int(w_r*0.6), int(h_r*0.6)))
    ax.imshow(img, cmap='gray')
    ax.set_title("(d) Melting (Sample 2)", fontsize=14)
    ax.axis('off')
    # Box & Label
    w, h = img.size
    rect = patches.Rectangle((w*0.2, h*0.2), w*0.3, h*0.3, linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.text(w*0.2, h*0.2 - 15, 'Melting 0.95', color='red', fontsize=12, weight='bold', verticalalignment='bottom')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Figure saved to: {output_path}")

if __name__ == "__main__":
    generate_fig7_v3()
