# Hu Moments Project

This project implements Hu's seven moment invariants for image analysis and evaluates their stability under scaling and rotation changes. It reads grayscale images from the `assets` folder, computes the moment invariants, and generates plots and fluctuation tables in the `result` folder.

## What this project does

- Computes Hu moment invariants from grayscale images
- Tests robustness under image scaling from $10 \times 10$ to $500 \times 500$
- Tests robustness under rotation from $1^\circ$ to $360^\circ$
- Generates visual plots and fluctuation summaries for each experiment

## Project structure

- `main.py` – entry point that runs the experiments and saves the outputs
- `moments_math.py` – implementation of raw, central, normalized moments and Hu moment formulas
- `experiments.py` – scaling and rotation experiment logic plus fluctuation calculation
- `assets/` – sample input images (`image_A.jpg`, `image_B.jpg`)
- `result/` – generated plots and tables
- `requirements.txt` – Python dependencies

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the project

From the project directory, run:

```bash
python main.py
```

This will:

1. Process the images in `assets/`
2. Run the scaling and rotation experiments
3. Save generated plots in `result/`

## Output files

The script generates the following output images in `result/`:

- `hu_moments_scaling_Image_A.png`
- `hu_moments_rotation_Image_A.png`
- `table_scaling_Image_A.png`
- `table_rotation_Image_A.png`
- Similar files for `Image_B`

## Notes

- The images should be grayscale or will be loaded as grayscale automatically.
- If an image file is missing, the script will print an error message and stop for that image.

## Author

- Mehdi Alijanibaei - AI & Automotive Software Engineering
