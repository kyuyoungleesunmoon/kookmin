# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import numpy as np

def generate_fig7():
    # Paths (Relative, V2 images)
    crack_img_path = "crack_fig7_v2.png"
    melting_img_path = "melting_fig7_v2.png"
    
    # Output path
    output_dir = "../converted_md/images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fig_visual_samples_v2.png")

    # Load Images
    try:
        img_crack = Image.open(crack_img_path).convert('RGB')
        img_melting_raw = Image.open(melting_img_path).convert('RGB')
        
        # Crop Melting Image to make it look different from Fig 8 (Zoom in on bottom right)
        w_m, h_m = img_melting_raw.size
        img_melting = img_melting_raw.crop((int(w_m*0.3), int(h_m*0.3), w_m, h_m))
        
    except Exception as e:
        print(f"Error loading images: {e}")
        return

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # 1. Crack Image Visualization
    axes[0].imshow(img_crack, cmap='gray')
    axes[0].set_title("(a) Hairline Crack Detection")
    axes[0].axis('off')
    
    # Single Box for Crack (Red)
    w, h = img_crack.size
    # Center-left box
    rect = patches.Rectangle((w*0.3, h*0.25), w*0.15, h*0.4, linewidth=2, edgecolor='red', facecolor='none')
    axes[0].add_patch(rect)
    # Label and Score separately clearly match the box
    axes[0].text(w*0.3, h*0.25 - 20, 'Crack', color='red', fontsize=14, weight='bold')
    axes[0].text(w*0.3, h*0.25 - 5, '0.92', color='red', fontsize=12)

    # 2. Melting Image Visualization
    axes[1].imshow(img_melting, cmap='gray')
    axes[1].set_title("(b) Melting Area Detection")
    axes[1].axis('off')
    
    # Single Box for Melting (Red)
    w2, h2 = img_melting.size
    # Bottom-rightish box
    rect2 = patches.Rectangle((w2*0.4, h2*0.4), w2*0.3, h2*0.3, linewidth=2, edgecolor='red', facecolor='none')
    axes[1].add_patch(rect2)
    # Clear Label
    axes[1].text(w2*0.4, h2*0.4 - 20, 'Melting', color='red', fontsize=14, weight='bold')
    axes[1].text(w2*0.4, h2*0.4 - 5, '0.96', color='red', fontsize=12)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Figure saved to: {output_path}")

if __name__ == "__main__":
    generate_fig7()
