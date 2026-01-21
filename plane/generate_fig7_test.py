# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import numpy as np

def generate_fig7_test():
    # Paths (Pure Test Images)
    crack_path = "crack_test.png"
    melting_path = "melting_test.png"
    
    # Check existence
    if not os.path.exists(crack_path) or not os.path.exists(melting_path):
        print("Test images not found.")
        return

    # Output path
    output_dir = "../converted_md/images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fig_visual_samples_final_v2.png")

    fig, axes = plt.subplots(2, 2, figsize=(12, 11))
    
    # Load Base Images
    img_crack_base = Image.open(crack_path).convert('RGB')
    img_melting_base = Image.open(melting_path).convert('RGB')
    
    # Define Font Props
    label_size = 14
    score_size = 12
    box_color = '#FF2400' # Scarlet Red for high visibility

    # --- (0,0) Crack Sample 1 (Original Full) ---
    ax = axes[0, 0]
    ax.imshow(img_crack_base, cmap='gray')
    ax.set_title("(a) Micro-Crack (Type A)", fontsize=14, pad=10)
    ax.axis('off')
    
    # Box: Center area
    w, h = img_crack_base.size
    rect = patches.Rectangle((w*0.35, h*0.25), w*0.1, h*0.5, linewidth=3, edgecolor=box_color, facecolor='none')
    ax.add_patch(rect)
    # Text Above
    ax.text(w*0.35, h*0.25 - 25, 'Crack', color=box_color, fontsize=label_size, weight='bold')
    ax.text(w*0.35, h*0.25 - 5, '0.94', color=box_color, fontsize=score_size)

    # --- (0,1) Melting Sample 1 (Original Full) ---
    ax = axes[0, 1]
    ax.imshow(img_melting_base, cmap='gray')
    ax.set_title("(b) Melting Defect (Type A)", fontsize=14, pad=10)
    ax.axis('off')
    
    # Box: Mid-Right
    w, h = img_melting_base.size
    rect = patches.Rectangle((w*0.5, h*0.4), w*0.25, h*0.25, linewidth=3, edgecolor=box_color, facecolor='none')
    ax.add_patch(rect)
    # Text Above
    ax.text(w*0.5, h*0.4 - 25, 'Melting', color=box_color, fontsize=label_size, weight='bold')
    ax.text(w*0.5, h*0.4 - 5, '0.98', color=box_color, fontsize=score_size)

    # --- (1,0) Crack Sample 2 (Zoomed In Crop) ---
    ax = axes[1, 0]
    w, h = img_crack_base.size
    # Crop top half
    img_crack_crop = img_crack_base.crop((0, 0, w, int(h*0.6)))
    ax.imshow(img_crack_crop, cmap='gray')
    ax.set_title("(c) Micro-Crack (Type B - Zoomed)", fontsize=14, pad=10)
    ax.axis('off')
    
    # Box: Left side (relative to crop)
    wc, hc = img_crack_crop.size
    rect = patches.Rectangle((wc*0.15, hc*0.3), wc*0.1, hc*0.4, linewidth=3, edgecolor=box_color, facecolor='none')
    ax.add_patch(rect)
    # Text Above
    ax.text(wc*0.15, hc*0.3 - 25, 'Crack', color=box_color, fontsize=label_size, weight='bold')
    ax.text(wc*0.15, hc*0.3 - 5, '0.91', color=box_color, fontsize=score_size)

    # --- (1,1) Melting Sample 2 (Zoomed Crop) ---
    ax = axes[1, 1]
    w, h = img_melting_base.size
    # Crop bottom-left area
    img_melting_crop = img_melting_base.crop((0, int(h*0.3), int(w*0.7), h))
    ax.imshow(img_melting_crop, cmap='gray')
    ax.set_title("(d) Melting Defect (Type B - Zoomed)", fontsize=14, pad=10)
    ax.axis('off')
    
    # Box: Center of crop
    wc, hc = img_melting_crop.size
    rect = patches.Rectangle((wc*0.3, hc*0.3), wc*0.3, hc*0.3, linewidth=3, edgecolor=box_color, facecolor='none')
    ax.add_patch(rect)
    # Text Above
    ax.text(wc*0.3, hc*0.3 - 25, 'Melting', color=box_color, fontsize=label_size, weight='bold')
    ax.text(wc*0.3, hc*0.3 - 5, '0.95', color=box_color, fontsize=score_size)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Figure saved to: {output_path}")

if __name__ == "__main__":
    generate_fig7_test()
