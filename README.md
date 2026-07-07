# Hu Moments Project

A comprehensive Computer Vision implementation of **Hu's seven moment invariants** for image analysis and shape recognition. This project evaluates the robustness and stability of Hu moment invariants under geometric transformations (scaling and rotation), demonstrating their invariance properties which make them valuable for object recognition tasks.

## Overview

**Hu moment invariants** are mathematical properties of images that remain relatively constant (invariant) under rotation, scaling, and translation transformations. These seven scalar values characterize the shape of objects in images, making them useful for shape-based image retrieval, object recognition, and pattern matching applications.

This implementation:

- Computes all seven Hu moment invariants from grayscale images
- Tests invariance properties under systematic scaling transformations (10×10 to 500×500 pixels)
- Tests invariance properties under full rotation (1° to 360°)
- Quantifies moment fluctuation using the fluctuation percentage metric
- Generates publication-quality visualizations and analysis tables

## Mathematical Background

### Moment Computation Pipeline

The project implements a complete moment computation pipeline:

1. **Raw Moments** ($m_{pq}$): Fundamental moments computed from pixel coordinates and intensities
   $$m_{pq} = \sum_x \sum_y x^p y^q I(x,y)$$

2. **Central Moments** ($\mu_{pq}$): Moments centered at the image centroid $(\bar{x}, \bar{y})$
   $$\mu_{pq} = \sum_x \sum_y (x - \bar{x})^p (y - \bar{y})^q I(x,y)$$

3. **Normalized Central Moments** ($\eta_{pq}$): Scale-invariant moments via normalization
   $$\eta_{pq} = \frac{\mu_{pq}}{\mu_{00}^{\gamma}} \quad \text{where} \quad \gamma = \frac{p+q}{2} + 1$$

4. **Hu Moment Invariants** ($\phi_1$ through $\phi_7$): Rotation and scale-invariant shape descriptors derived from normalized moments

### The Seven Hu Moments

- **$\phi_1$**: Basic shape descriptor combining second-order normalized moments
- **$\phi_2$**: Second-order shape descriptor capturing aspect ratio and orientation information
- **$\phi_3$**: Third-order invariant sensitive to shape asymmetry
- **$\phi_4$**: Third-order invariant capturing additional shape characteristics
- **$\phi_5$** through **$\phi_7$**: Higher-order shape descriptors with complex polynomial combinations

## Project Structure

```
├── main.py                      # Entry point; orchestrates experiments and visualization
├── moments_math.py              # Low-level moment computation functions
├── experiments.py               # Scaling and rotation experiment implementations
├── README.md                    # Project documentation
├── requirements.txt             # Python package dependencies
├── assets/                      # Input images for analysis
│   ├── image_A.jpg
│   └── image_B.jpg
└── result/                      # Generated output (plots and tables)
```

### File Descriptions

- **`main.py`**: Main entry point that orchestrates the entire workflow
  - Loads images from `assets/`
  - Runs scaling and rotation experiments
  - Generates plots and fluctuation tables
  - Saves all outputs to `result/`

- **`moments_math.py`**: Core mathematical implementations
  - `compute_raw_moment()`: Computes raw moments from image data
  - `compute_central_moment()`: Computes moments relative to image centroid
  - `compute_normalized_moment()`: Normalizes central moments for scale invariance
  - `get_hu_moments()`: Computes all seven Hu moment invariants for a given image

- **`experiments.py`**: Experimental frameworks
  - `run_scaling_experiment()`: Tests moment stability across 50 different resolutions
  - `run_rotation_experiment()`: Tests moment stability across 360° rotation
  - `calculate_fluctuation()`: Computes percentage fluctuation of moment values (lower is better)

## Requirements

Python 3.7+ with the following dependencies:

```
numpy              # Numerical computations and array operations
opencv-python      # Image loading and transformation (resizing, rotation)
matplotlib         # Visualization and plot generation
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Full Analysis

Execute the main script from the project directory:

```bash
python main.py
```

This will:

1. Load all grayscale images from `assets/`
2. Run scaling experiment (10×10 to 500×500 pixels)
3. Run rotation experiment (1° to 360°)
4. Generate visualization plots for each moment
5. Generate fluctuation analysis tables
6. Save all outputs to `result/`

### Output Files

For each input image (e.g., `Image_A`), the script generates:

**Scaling Analysis:**

- `hu_moments_scaling_Image_A.png` – 7-panel plot showing $\phi_1$ through $\phi_7$ values across scaling resolutions
- `table_scaling_Image_A.png` – Fluctuation percentage table for each moment under scaling

**Rotation Analysis:**

- `hu_moments_rotation_Image_A.png` – 7-panel plot showing $\phi_1$ through $\phi_7$ values across rotation angles
- `table_rotation_Image_A.png` – Fluctuation percentage table for each moment under rotation

### Visualization Details

- **Plots**: Each plot displays all 7 Hu moments in separate vertically-stacked subplots for clarity
- **Resolution**: All outputs saved at 300 DPI for publication quality
- **Grid & Legend**: Each subplot includes a grid overlay and labeled legend for easy interpretation
- **Fluctuation Tables**: Display percentage fluctuation for each moment, quantifying invariance quality

## Key Findings & Insights

### Moment Invariance Properties

- **$\phi_1$ and $\phi_2$**: Generally exhibit minimal fluctuation under both scaling and rotation, demonstrating strong invariance
- **Higher-order moments** ($\phi_5$–$\phi_7$): Often show larger fluctuations, particularly under rotation, due to accumulated computational effects
- **Scale invariance**: All moments show high stability across different image resolutions
- **Rotation invariance**: Hu moments maintain relative stability across the full 360° rotation range

### Fluctuation Metric

Fluctuation is calculated as:
$$\text{Fluctuation} = \frac{\max(data) - \min(data)}{|\text{mean}(data)|} \times 100\%$$

Lower fluctuation percentages indicate better invariance properties.

## Technical Notes

- **Image Format**: Input images should be grayscale or will be automatically converted to grayscale
- **Interpolation**: Scaling uses bilinear interpolation; rotation uses linear interpolation
- **Resolution Range**: Scaling tests from 10×10 to 500×500 in 10-pixel increments (50 test points)
- **Rotation Range**: Rotation tests across full 360° range in 1° increments (360 test points)
- **Boundary Handling**: Rotated images are expanded to accommodate boundary pixels
- **Error Handling**: Script includes validation for missing or invalid image files

## References

This implementation is based on the classical work:

> Hu, M. K. (1962). "Visual pattern recognition by moment invariants." _IRE Transactions on Information Theory_, 8(2), 179-187.

The Hu moment invariants have become a fundamental technique in computer vision for shape-based image analysis and object recognition.

## Author

Mehdi Alijanibaei - AI & Automotive Software Engineering

---

_Last Updated: 2026_
