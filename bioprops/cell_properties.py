import numpy as np
from skimage import measure

def compute_cell_properties_from_nifti(data):
    labeled_mask, num_labels = measure.label(data, return_num=True)
    props = measure.regionprops(labeled_mask)
    
    sum_cov_matrix = np.zeros((3, 3))
    total_area = 0
    num_cells = 0
    
    for prop in props:
        cell_pixels = np.array(prop.coords)
        if len(cell_pixels) >= 4:
            cov_matrix = np.cov(cell_pixels, rowvar=False)
            sum_cov_matrix += cov_matrix
            total_area += prop.area
            num_cells += 1
    
    area = total_area / num_cells if num_cells > 0 else 0
    eigenvalues, _ = np.linalg.eigh(sum_cov_matrix)
    eigenvalues.sort()
    principal_moments = np.sqrt(eigenvalues)
    elongation = principal_moments[0] / principal_moments[2]
    flatness = principal_moments[1] / principal_moments[2]
    
    return {
        "Nuclear Elongation": float(elongation),
        "Nuclear Flatness": float(flatness),
        "Nuclear Volume": float(area),
    }
