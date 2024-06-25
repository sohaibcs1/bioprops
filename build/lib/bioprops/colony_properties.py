import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.distance import pdist
from skimage import measure

def compute_colony_properties_from_nifti(data):
    labeled_mask, num_labels = measure.label(data, return_num=True)
    props = measure.regionprops(labeled_mask)

    cell_pixels_list = []
    for prop in props:
        cell_pixels = np.array(prop.coords)
        if len(cell_pixels) >= 4:
            cell_pixels_list.append(cell_pixels)

    all_cell_pixels = np.vstack(cell_pixels_list)
    cov_matrix = np.cov(all_cell_pixels, rowvar=False)
    eigenvalues, _ = np.linalg.eigh(cov_matrix)
    eigenvalues.sort()
    principal_moments = np.sqrt(eigenvalues)
    elongation = principal_moments[0] / principal_moments[2]
    flatness = principal_moments[1] / principal_moments[2]
    hull = ConvexHull(all_cell_pixels)
    convex_hull_area = hull.area
    hull_points = all_cell_pixels[hull.vertices]
    distances = pdist(hull_points)
    diameter = np.max(distances)
    radius = diameter / 2
    mean_edge_length = np.mean(distances)
    max_edge_length = np.max(distances)

    return {
        "Colony Elongation": float(elongation),
        "Colony Flatness": float(flatness),
        "Colony total Cells": len(cell_pixels_list),
        "Colony Size": float(convex_hull_area),
        "Colony Diameter": float(diameter),
        "Colony Radius": float(radius),
        "Max Edge Length": float(max_edge_length),
        "Mean Edge Length": float(mean_edge_length),
    }
