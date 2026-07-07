import os
import matplotlib.pyplot as plt
from experiments import run_scaling_experiment, run_rotation_experiment, calculate_fluctuation

def plot_results(x_data, moments_dict, title, xlabel, filename):
    """
    Plots the results in 7 separate subplots (similar to Figure 3 in the paper).
    This ensures that higher-order moments with smaller magnitudes are clearly visible.
    Automatically saves the output as a high-resolution PNG file in the designated path.
    """
    fig, axes = plt.subplots(7, 1, figsize=(10, 15), sharex=True)
    fig.suptitle(title, fontsize=16, y=0.98)

    for i in range(7):
        ax = axes[i]
        # Plot each moment in its dedicated subplot
        ax.plot(x_data, moments_dict[f'phi{i+1}'], label=rf'$\phi_{i+1}$', color=f'C{i}')
        
        # Appearance and grid settings
        ax.set_ylabel(rf'$\phi_{i+1}$', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='upper right')

    # Set the X-axis label only for the bottom subplot
    axes[-1].set_xlabel(xlabel, fontsize=12)
    
    # Adjust layout to prevent overlapping and save the figure
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()

def plot_fluctuation_table(moments_dict, title, filename):
    """Draws a clean data table of the fluctuations and saves it as a PNG."""
    table_data = []
    for k, v in moments_dict.items():
        fluc = calculate_fluctuation(v)
        table_data.append([rf'$\{k}$', f"{fluc:.2f}%"])

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.axis('tight')
    ax.axis('off')
    
    col_labels = ["Moment Invariant", "Fluctuation (%)"]
    table = ax.table(cellText=table_data, colLabels=col_labels, loc='center', cellLoc='center')
    table.scale(1, 1.5)
    
    plt.title(title, pad=20, fontsize=14)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    output_dir = "result"
    os.makedirs(output_dir, exist_ok=True)
    
    images_to_test = {
        "Image_A": "assets/image_A.jpg",
        "Image_B": "assets/image_B.jpg"
    }
    
    for image_name, image_path in images_to_test.items():
        print(f"\n{'='*40}")
        print(f"PROCESSING {image_name.upper()} ({image_path})")
        print(f"{'='*40}")
        
        try:
            # --- 1. Scaling Experiment ---
            print(f"--- Running Scaling Experiment for {image_name} ---")
            res_x, res_y = run_scaling_experiment(image_path)
            
            # Save Scaling Graph
            scaling_output_path = os.path.join(output_dir, f"hu_moments_scaling_{image_name}.png")
            plot_results(res_x, res_y, f"Moment Invariants on Image Scaling ({image_name})", "Resolution", scaling_output_path)
            
            # Save Scaling Table
            scaling_table_path = os.path.join(output_dir, f"table_scaling_{image_name}.png")
            plot_fluctuation_table(res_y, f"Scaling Fluctuation ({image_name})", scaling_table_path)

            # --- 2. Rotation Experiment ---
            print(f"--- Running Rotation Experiment for {image_name} ---")
            rot_x, rot_y = run_rotation_experiment(image_path)
            
            # Save Rotation Graph
            rotation_output_path = os.path.join(output_dir, f"hu_moments_rotation_{image_name}.png")
            plot_results(rot_x, rot_y, f"Moment Invariants on Image Rotation ({image_name})", "Angle (Degrees)", rotation_output_path)
            
            # Save Rotation Table
            rotation_table_path = os.path.join(output_dir, f"table_rotation_{image_name}.png")
            plot_fluctuation_table(rot_y, f"Rotation Fluctuation ({image_name})", rotation_table_path)
            
            print(f"Successfully generated graphs and tables for {image_name} in the /result folder.")
                
        except FileNotFoundError as e:
            print(f"\nError: {e}")
            print(f"Please ensure {image_path} exists.")