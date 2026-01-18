import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_architecture_diagram():
    # Setup figure
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # Style settings
    box_facecolor = '#f0f4f8'
    box_edgecolor = '#333333'
    text_color = '#000000'
    arrow_color = '#000000'
    font_family = 'sans-serif' # Helvetica or Arial style
    
    # Define boxes (x, y, width, height, label, subtext)
    # Layout strategy: 3 columns, 2 rows essentially
    # Row 1 (Top): Original -> Adaptive -> X-ray Trans
    # Row 2 (Bottom): IoU Val -> Augmented -> YOLO -> Final (Final is extra step)
    
    # Coordinates
    y_row1 = 4.5
    y_row2 = 1.5
    
    x_col1 = 0.5
    x_col2 = 4.0
    x_col3 = 7.5
    x_col4 = 10.0 # Wait, YOLO is col3? Let's check flow.
    # Flow: Original(1) -> Adaptive(2) -> X-ray(3)
    #       | \               |             |
    #       v  \              v             v
    #      IoU(4) ->      Augmented(5) -> YOLO(6) -> Final(7)
    
    # Re-adjusting spacing
    w = 2.8
    h = 1.6
    gap = 0.7
    
    # Box definitions
    boxes = {
        'original': {'x': 0.5, 'y': 4.5, 'text': "Original Dataset\n(16 Images)", 'sub': "Crack: 14\nMelting: 2", 'color': '#ffe6e6'}, # Light Red
        'adaptive': {'x': 4.0, 'y': 4.5, 'text': "Adaptive Augmentation\nIntensity Formula", 'sub': r"$I(c) = \alpha \log(N_{max}/N_c) + \beta$", 'color': '#e6f2ff'}, # Light Blue
        'xray':     {'x': 7.5, 'y': 4.5, 'text': "X-ray Specific\nTransformations", 'sub': "• CLAHE\n• Gamma Correction\n• Gaussian Noise", 'color': '#e6ffe6'}, # Light Green
        
        'iou':      {'x': 0.5, 'y': 1.5, 'text': "Label Validation\n(IoU-based)", 'sub': "Accuracy: 97.3%\n(Semi-auto Labeling)", 'color': '#fff9e6'}, # Light Yellowish
        'augmented':{'x': 4.0, 'y': 1.5, 'text': "Augmented Dataset\n(339 Images)", 'sub': "Balanced Classes\n(Synth + Original)", 'color': '#f2e6ff'}, # Light Purple
        'yolo':     {'x': 7.5, 'y': 1.5, 'text': "Model Training\n(YOLOv8s)", 'sub': "Backbone: CSA\nFrozen Stages: 10\nOpt: AdamW", 'color': '#e6ffff'}, # Cyan-ish
        
        'final':    {'x': 7.5, 'y': -1.2, 'text': "Final Performance", 'sub': "mAP50: 91.7%\nPrecision: 88.5%", 'color': '#ffe6f2'} # Pink
    }
    
    # Adjust Final position (below YOLO)
    boxes['final']['y'] = -0.5 # A bit lower? No, figure limits 0-7.
    # Let's shift everything up.
    shift_y = 1.0
    for k in boxes:
        boxes[k]['y'] += shift_y

    # Helper to draw box
    def draw_box(key):
        b = boxes[key]
        # Draw shadow
        shadow = patches.FancyBboxPatch((b['x']+0.05, b['y']-0.05), w, h, boxstyle="round,pad=0.1", 
                                        ec="none", fc='#dddddd', zorder=1)
        ax.add_patch(shadow)
        
        # Draw box
        rect = patches.FancyBboxPatch((b['x'], b['y']), w, h, boxstyle="round,pad=0.1", 
                                      linewidth=1.5, edgecolor=box_edgecolor, facecolor=b['color'], zorder=2)
        ax.add_patch(rect)
        
        # Text
        cx = b['x'] + w/2
        cy = b['y'] + h/2 + 0.3
        ax.text(cx, cy, b['text'], ha='center', va='center', fontsize=11, fontweight='bold', zorder=3)
        
        # Subtext
        cy_sub = b['y'] + h/2 - 0.3
        ax.text(cx, cy_sub, b['sub'], ha='center', va='center', fontsize=9, zorder=3)
        
        # Save center points for arrows
        boxes[key]['center_top'] = (cx, b['y'] + h)
        boxes[key]['center_bottom'] = (cx, b['y'])
        boxes[key]['center_left'] = (b['x'], b['y'] + h/2)
        boxes[key]['center_right'] = (b['x'] + w, b['y'] + h/2)

    for k in boxes:
        draw_box(k)

    # Helper for arrow
    def draw_arrow(start_box, end_box, side_start='center_right', side_end='center_left'):
        p1 = boxes[start_box][side_start]
        p2 = boxes[end_box][side_end]
        ax.annotate("", xy=p2, xytext=p1, 
                    arrowprops=dict(arrowstyle="->", lw=1.5, color=arrow_color))

    # Connections based on image
    # Original -> Adaptive
    draw_arrow('original', 'adaptive', 'center_right', 'center_left')
    
    # Adaptive -> X-ray
    draw_arrow('adaptive', 'xray', 'center_right', 'center_left')
    
    # Original -> IoU (Down)
    draw_arrow('original', 'iou', 'center_bottom', 'center_top')
    
    # Adaptive -> Augmented (Down)
    draw_arrow('adaptive', 'augmented', 'center_bottom', 'center_top')
    
    # X-ray -> YOLO (Down)
    draw_arrow('xray', 'yolo', 'center_bottom', 'center_top')
    
    # IoU -> Augmented (Right)
    draw_arrow('iou', 'augmented', 'center_right', 'center_left')
    
    # Augmented -> YOLO (Right)
    draw_arrow('augmented', 'yolo', 'center_right', 'center_left')
    
    # YOLO -> Final (Down)
    # Wait, 'final' Y is lower than YOLO
    draw_arrow('yolo', 'final', 'center_bottom', 'center_top')

    # Add Section Titles (Optional background zones)
    # Zone 1: Data Preparation
    # rect1 = patches.Rectangle((0.2, 1.2+shift_y), 3.4, 5.2, alpha=0.05, color='gray')
    # ax.add_patch(rect1)
    # ax.text(0.3, 6.2+shift_y, "Phase 1: Data Prep", fontsize=10, fontweight='bold', color='gray')

    plt.title("Proposed 2-Stage Domain Bridge Transfer Learning Framework", fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(r'C:\국민대프로젝트\architecture_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_architecture_diagram()
