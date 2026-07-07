import numpy as np

def compute_raw_moment(img, p, q):
    y_indices, x_indices = np.indices(img.shape)
    moment = np.sum((x_indices ** p) * (y_indices ** q) * img)
    return moment

def compute_central_moment(img, p, q, x_bar, y_bar):
    y_indices, x_indices = np.indices(img.shape)
    central_moment = np.sum(((x_indices - x_bar) ** p) * ((y_indices - y_bar) ** q) * img)
    return central_moment

def compute_normalized_moment(mu_pq, mu_00, p, q):
    gamma = ((p + q) / 2.0) + 1.0
    normalized_moment = mu_pq / (mu_00 ** gamma)
    return normalized_moment

def get_hu_moments(img):
    m00 = compute_raw_moment(img, 0, 0)
    if m00 == 0:
        return np.zeros(7)   
    # 2. Centroid coordinates
    x_bar = compute_raw_moment(img, 1, 0) / m00
    y_bar = compute_raw_moment(img, 0, 1) / m00
    # 3. Central moments
    mu00 = m00 
    mu20 = compute_central_moment(img, 2, 0, x_bar, y_bar)
    mu02 = compute_central_moment(img, 0, 2, x_bar, y_bar)
    mu11 = compute_central_moment(img, 1, 1, x_bar, y_bar)
    mu30 = compute_central_moment(img, 3, 0, x_bar, y_bar)
    mu03 = compute_central_moment(img, 0, 3, x_bar, y_bar)
    mu21 = compute_central_moment(img, 2, 1, x_bar, y_bar)
    mu12 = compute_central_moment(img, 1, 2, x_bar, y_bar)
    # 4. Normalized central moments
    n20 = compute_normalized_moment(mu20, mu00, 2, 0)
    n02 = compute_normalized_moment(mu02, mu00, 0, 2)
    n11 = compute_normalized_moment(mu11, mu00, 1, 1)
    n30 = compute_normalized_moment(mu30, mu00, 3, 0)
    n03 = compute_normalized_moment(mu03, mu00, 0, 3)
    n21 = compute_normalized_moment(mu21, mu00, 2, 1)
    n12 = compute_normalized_moment(mu12, mu00, 1, 2)
    # 5. Hu's Invariants Formulas
    phi1 = n20 + n02
    phi2 = (n20 - n02)**2 + 4 * (n11**2)
    phi3 = (n30 - 3*n12)**2 + (3*n21 - n03)**2
    phi4 = (n30 + n12)**2 + (n21 + n03)**2
    phi5 = (n30 - 3*n12) * (n30 + n12) * ((n30 + n12)**2 - 3*(n21 + n03)**2) + \
           (3*n21 - n03) * (n21 + n03) * (3*(n30 + n12)**2 - (n21 + n03)**2)
    phi6 = (n20 - n02) * ((n30 + n12)**2 - (n21 + n03)**2) + \
           4 * n11 * (n30 + n12) * (n21 + n03)
    phi7 = (3*n21 - n03) * (n30 + n12) * ((n30 + n12)**2 - 3*(n21 + n03)**2) - \
           (n30 - 3*n12) * (n21 + n03) * (3*(n30 + n12)**2 - (n21 + n03)**2)
           
    return np.array([phi1, phi2, phi3, phi4, phi5, phi6, phi7])