# IEEE TII Paper - English Translation

---

## A. Phase 1: Latent Diffusion-based Few-Shot Generation

To ensure diversity within the defect data using only 16 images, we adapted Stable Diffusion [19], a text-to-image generation model, specifically for the industrial X-ray domain. The goal was not simple image synthesis but to learn the semi-transparent textures and noise patterns unique to X-ray radiographs. The following strategies were employed.

**Latent Diffusion Process (LDM):** Pixel-space diffusion models require substantial computational resources for high-resolution image generation. To address this, LDM compresses images into a lower-dimensional latent space and performs diffusion in that space. The LDM consists of a forward process and a reverse process. In the forward process, Gaussian noise is progressively added to the original latent vector $z_0$ until it becomes isotropic noise $z_T$ at time step $T$. In the reverse process, a neural network $\epsilon_\theta$ receives a conditioning signal $c$ (e.g., a text prompt) and predicts the noise to be removed. The objective function is defined as:

$$\mathcal{L}_{LDM} = \mathbb{E}_{z,\epsilon,t,c}\left[\|\epsilon - \epsilon_\theta(z_t, t, \tau_\theta(c))\|^2 \right]$$

Here, $\tau_\theta$ is the text encoder (CLIP). We used prompts such as "A high-quality X-ray image of a DPF filter with [Category] defect" to control the generation process.

**Low-Rank Adaptation (LoRA):** Fully fine-tuning a large model like Stable Diffusion with only 16 images can lead to severe overfitting and catastrophic forgetting. To mitigate this, we applied Low-Rank Adaptation (LoRA) [20]. LoRA freezes the pretrained weight matrix $W$ and approximates the update $\Delta W$ as a product of two low-rank matrices, $A$ and $B$:

$$W' = W + \Delta W = W + BA$$

where the rank $r \ll \min(d_1, d_2)$. We set $r = 4$, limiting the number of trainable parameters to approximately 0.01% of the total while effectively injecting the key visual features (edges, textures) of DPF defects. This allowed the generative model to produce high-quality images that faithfully reflect the physical properties of defects even from a small dataset.

---

## B. Phase 2: Hierarchical Domain Bridge

The generalization performance of a deep learning model is guaranteed when the distributions of the training data (source domain, $\mathcal{D}_S$) and the test data (target domain, $\mathcal{D}_T$) are aligned. However, a significant domain gap exists between natural images (ImageNet) and industrial X-ray images.

**Domain Gap Quantification:** The distance between domains can be defined by $\mathcal{H}$-divergence [9]. Let the natural image domain be $\mathcal{N}$ and the DPF domain be $\mathcal{D}$. If the distance between these domains is large ($d_\mathcal{H}(\mathcal{N}, \mathcal{D}) \gg 0$), the efficiency of transfer learning degrades sharply, a phenomenon often referred to as 'negative transfer'.

To address this problem, we designed a three-stage hierarchical transfer learning scheme that introduces the Industrial X-ray Zip Dataset, comprising 8,900 X-ray images of various parts (screws, pipes, castings, etc.), as an intermediate bridge domain ($\mathcal{B}$).

**Stage 1: General Feature Learning ($\mathcal{N} \rightarrow \Theta_0$):** Weights $\Theta_0$ pretrained on ImageNet are used as initial values. At this stage, the model acquires the ability to recognize basic object contours, edges, and colors.

**Stage 2: Domain Adaptation via Bridge ($\mathcal{B} \rightarrow \Theta_1$):** The model is tuned using the intermediate domain dataset. Although the Zip Dataset contains different object types than DPFs, it shares low-level features characteristic of X-ray radiographs, such as grayscale intensity distribution, quantum noise patterns, and background textures.

$$\Theta_1 = \arg\min_\Theta \mathcal{L}_{det}(\mathcal{B}; \Theta_0)$$

Through this process, the model discards the "grammar" of natural images and adapts to the statistical properties of industrial X-ray images (domain alignment).

**Stage 3: Task-Specific Fine-tuning ($\mathcal{D} \rightarrow \Theta_2$):** Finally, the model is trained on the target data, a mixture of 16 real DPF images and 500 synthetic images. Because the model is already pre-aligned to the X-ray domain from Stage 2, it can learn the unique high-level semantics of defects quickly and stably with only a small amount of target data. This is a key factor in accelerating convergence speed and reducing performance variability in the few-shot learning environment.

---

## C. Phase 3: Uncertainty-Aware Detection

Generated synthetic data may have subtle distribution shifts from real data, which can degrade the model's prediction confidence. To compensate for this, we enhanced the detection head based on YOLO11 [8] to estimate uncertainty.

**Gaussian Bounding Box Modeling:** Standard object detection models predict bounding box coordinates $(x, y, w, h)$ as deterministic values. However, to account for labeling noise and boundary ambiguity in generated images, we model each coordinate as a Gaussian distribution $\mathcal{N}(\mu, \sigma^2)$. The General Distribution Loss, which minimizes the difference between the predicted box distribution $\hat{P}$ and the ground-truth box distribution $P^*$ (a Dirac delta function), is defined as follows:

$$\mathcal{L}_{GD} = -\log P(\text{box} | \mu, \sigma)$$

When expanded, the model tends to increase the variance $\sigma$ for unreliable samples (e.g., generated artifacts) to reduce the penalty. This effectively grants tolerance to 'hard samples' during training.

**C2PSA (Cross-Stage Partial Self-Attention) with Linear Complexity:** Small defects (small objects) have few pixels, and their features can easily be lost through convolution operations alone. To address this, an attention module [30, 31] that captures global context is essential. We integrated the C2PSA module into YOLO11's C3k2 Block. Conventional self-attention has a computational complexity of $O(n^2)$ with respect to input length $n$, making it unsuitable for high-resolution processing. We introduced a linear attention mechanism to reduce the complexity to $O(n)$.

$$\text{Attention}(Q, K, V) = \frac{\phi(Q)(\phi(K)^T V)}{\phi(Q)(\phi(K)^T \vec{1})}$$

Here, $\phi$ is a kernel function. This structure effectively captures the contextual information needed to distinguish background noise from fine cracks without degrading real-time inference speed (FPS) on edge devices.

**Comprehensive Loss Function:** The final model is trained with a combination of the uncertainty loss, a sample-weighted classification loss to address class imbalance, and a CIoU loss for box accuracy.

$$\mathcal{L}_{total} = \mathcal{L}_{GD} + \mathcal{L}_{SW-cls} + \mathcal{L}_{CIoU}$$

**Sample-Weighted Loss ($\mathcal{L}_{SW-cls}$):** By applying the inverse of the class frequency as a weight $w_c$, a larger penalty is assigned to infrequent defects (e.g., Crack).

$$\mathcal{L}_{SW-cls} = -\sum_c w_c \cdot y_{c} \log(\hat{y}_c)$$

This composite loss function design addresses both the quantitative shortage and qualitative imbalance of data.

---

## Experimental Setup

### A. Dataset Construction

The experiments in this study were conducted by organically combining three types of datasets.

**Industrial X-ray Zip Dataset (Bridge Domain):** A total of 8,900 X-ray images of various mechanical parts (pipes, screws, cylinders, etc.) were constructed for domain adaptation. This dataset was captured under tube voltage conditions of 100-160 kV and has a grayscale histogram distribution similar to that of DPF X-ray images.

**Few-Shot DPF Dataset (Target Domain):**
- **Real Data:** 16 defect images collected from the actual manufacturing process (Crack: 8 images, Melting: 8 images).
- **Synthetic Data:** 500 virtual defect images generated in Phase 1. The generated images were screened by a quality engineer to select only samples with verified physical plausibility.

**Test Set:** To objectively evaluate model performance, 30 real DPF defect images that were never used in training were separately secured. These were classified into 'Easy', 'Medium', and 'Hard' difficulty levels to test the model's limitations.

### B. Implementation Details

All experiments were performed on the PyTorch 2.1.0 framework. The hardware setup consisted of distributed training (DDP) using four NVIDIA RTX 3090 (24GB VRAM) GPUs.

- **Input Resolution:** The input resolution was set to $1280 \times 1280$ pixels for fine defect detection.
- **Optimizer:** The AdamW [26] optimizer was used with momentum $\beta = 0.9$ and weight decay of $5 \times 10^{-4}$.
- **Learning Rate Schedule:** The initial learning rate increases linearly from 0 to $1 \times 10^{-3}$ during the warmup period (3 epochs), and then decreases to $1 \times 10^{-5}$ following a cosine annealing schedule.

**Table I: Training Hyperparameter Settings**

| Parameter | Stage 1 (Bridge) | Stage 2 (Target Fine-tuning) | Note |
|---|---|---|---|
| Epochs | 50 | 100 | Sufficient convergence time |
| Batch Size | 16 | 8 | GPU memory and batch normalization optimization |
| Optimizer | AdamW [26] | AdamW | - |
| Initial LR | 1e-3 | 1e-4 | Prevents catastrophic forgetting |
| Augmentation | Basic | Mosaic + Mixup (Off last 10) | Guides precise detection |

### C. Evaluation Metrics

Model performance was evaluated using Mean Average Precision (mAP), the standard metric in the object detection field.

**Precision & Recall:**

$$\text{Precision} = \frac{TP}{TP+FP}, \quad \text{Recall} = \frac{TP}{TP+FN}$$

- **mAP50:** The average of Average Precision (AP) at an Intersection over Union (IoU) threshold of 0.5. Suitable for determining the 'existence' of a detection.
- **mAP50-95:** The average AP from IoU 0.5 to 0.95 in 0.05 increments. Rigorously evaluates the 'localization accuracy' of the bounding box.

---

## Experimental Results and Analysis

### A. Overall Performance

To validate the proposed GLAD framework, comparative experiments were conducted against YOLOv8s, an existing state-of-the-art lightweight model. The final performance is summarized in Table 2.

**Table 2: YOLO11 vs YOLOv8 Final Performance Comparison**

| Model | mAP50 (%) | mAP50-95 (%) | Precision (%) | Recall (%) | F1 Score | Params (M) |
|---|---|---|---|---|---|---|
| YOLOv8s | 62.3 | 45.2 | 71.8 | 68.5 | 0.701 | 11.1 |
| YOLO11s | 91.7 | 72.6 | 92.8 | 82.2 | 0.872 | 9.4 |
| Absolute Improvement | +29.4 | +27.4 | +21.0 | +13.7 | +0.171 | -1.7 |

---
