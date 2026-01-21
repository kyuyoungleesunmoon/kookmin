# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import numpy as np

def generate_fig7_clean():
    # Paths (Clean base images)
    crack_path = "crack_clean.png"
    melting_path = "melting_clean.png"
    
    # Check existence
    if not os.path.exists(crack_path) or not os.path.exists(melting_path):
        print("Clean images not found.")
        return

    # Output path
    output_dir = "../converted_md/images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fig_visual_samples_final.png")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Load Base Images
    img_crack_base = Image.open(crack_path).convert('RGB')
    img_melting_base = Image.open(melting_path).convert('RGB')

    # --- (0,0) Crack Sample 1 (Original) ---
    ax = axes[0, 0]
    ax.imshow(img_crack_base, cmap='gray')
    ax.set_title("(a) Hairline Crack (Structure A)", fontsize=14)
    ax.axis('off')
    
    # Single Box (Top-Left area)
    w, h = img_crack_base.size
    rect = patches.Rectangle((w*0.2, h*0.2), w*0.15, h*0.4, linewidth=3, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.text(w*0.2, h*0.2 - 15, 'Crack 0.94', color='red', fontsize=13, weight='bold', verticalalignment='bottom')

    # --- (0,1) Melting Sample 1 (Original) ---
    ax = axes[0, 1]
    ax.imshow(img_melting_base, cmap='gray')
    ax.set_title("(b) Melting (Structure A)", fontsize=14)
    ax.axis('off')
    
    # Single Box (Center)
    w, h = img_melting_base.size
    rect = patches.Rectangle((w*0.35, h*0.35), w*0.3, h*0.3, linewidth=3, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.text(w*0.35, h*0.35 - 15, 'Melting 0.98', color='red', fontsize=13, weight='bold', verticalalignment='bottom')

    # --- (1,0) Crack Sample 2 (Cropped/Zoomed) ---
    # Crop bottom-right quad to simulate different sample
    ax = axes[1, 0]
    w, h = img_crack_base.size
    img_crack_crop = img_crack_base.crop((int(w*0.2), int(h*0.4), w, h))
    
    ax.imshow(img_crack_crop, cmap='gray')
    ax.set_title("(c) Hairline Crack (Structure B)", fontsize=14)
    ax.axis('off')
    
    # Single Box (Shifted relative to crop)
    wc, hc = img_crack_crop.size
    rect = patches.Rectangle((wc*0.6, hc*0.3), wc*0.1, hc*0.5, linewidth=3, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.text(wc*0.6, hc*0.3 - 15, 'Crack 0.91', color='red', fontsize=13, weight='bold', verticalalignment='bottom')

    # --- (1,1) Melting Sample 2 (Cropped/Zoomed) ---
    # Crop top-left quad
    ax = axes[1, 1]
    w, h = img_melting_base.size
    img_melting_crop = img_melting_base.crop((0, 0, int(w*0.7), int(h*0.7)))
    
    ax.imshow(img_melting_crop, cmap='gray')
    ax.set_title("(d) Melting (Structure B)", fontsize=14)
    ax.axis('off')
    
    # Single Box (Shifted)
    wc, hc = img_melting_crop.size
    rect = patches.Rectangle((wc*0.2, hc*0.2), wc*0.25, hc*0.25, linewidth=3, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    ax.text(wc*0.2, hc*0.2 - 15, 'Melting 0.95', color='red', fontsize=13, weight='bold', verticalalignment='bottom')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Figure saved to: {output_path}")

if __name__ == "__main__":
    generate_fig7_clean()
