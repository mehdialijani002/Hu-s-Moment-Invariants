import cv2
import numpy as np
from moments_math import get_hu_moments

def calculate_fluctuation(data_array):
    """Calculates the fluctuation percentage based on Equation (4) in the paper."""
    data = np.array(data_array)
    mean_val = np.mean(data)
    if mean_val == 0: 
        return 0
    return ((np.max(data) - np.min(data)) / np.abs(mean_val)) * 100

def run_scaling_experiment(image_path):
    """Tests Hu Moments against an image resized from 10x10 to 500x500."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")

    resolutions = range(10, 510, 10)
    hu_moments_history = {f'phi{i+1}': [] for i in range(7)}
    
    for res in resolutions:
        # Interpolation simulates the discrete pixel generation during scaling
        resized_img = cv2.resize(img, (res, res), interpolation=cv2.INTER_LINEAR)
        moments = get_hu_moments(resized_img)
        
        for i in range(7):
            hu_moments_history[f'phi{i+1}'].append(moments[i])
            
    return list(resolutions), hu_moments_history

def run_rotation_experiment(image_path, target_resolution=(250, 250)):
    """Tests Hu Moments against an image rotated from 1 to 360 degrees."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")
        
    img = cv2.resize(img, target_resolution)
    h, w = img.shape
    center = (w // 2, h // 2)
    angles = range(1, 361)
    
    hu_moments_history = {f'phi{i+1}': [] for i in range(7)}
    
    for angle in angles:
        # 1. Get the standard rotation matrix
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        
        # 2. Grab the sine and cosine values from the rotation matrix
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        
        # 3. Calculate the new "bigger picture frame" dimensions
        new_w = int((h * sin) + (w * cos))
        new_h = int((h * cos) + (w * sin))
        
        # 4. Adjust the rotation matrix to shift the image to the new center
        M[0, 2] += (new_w / 2) - center[0]
        M[1, 2] += (new_h / 2) - center[1]
        
        # 5. Rotate the image using the newly calculated frame dimensions
        rotated_img = cv2.warpAffine(img, M, (new_w, new_h), flags=cv2.INTER_LINEAR)
        
        moments = get_hu_moments(rotated_img)
        for i in range(7):
            hu_moments_history[f'phi{i+1}'].append(moments[i])
            
    return list(angles), hu_moments_history