from .cell_properties import compute_cell_properties_from_nifti
from .colony_properties import compute_colony_properties_from_nifti

def properties_from_nifti(nifti_file):
    import nibabel as nib
    import json
    
    img = nib.load(nifti_file)
    data = img.get_fdata()
    
    colony_properties = compute_colony_properties_from_nifti(data)
    cell_properties = compute_cell_properties_from_nifti(data)
    
    combined_properties = cell_properties.copy()
    combined_properties.update(colony_properties)
    colony_properties_json_str = json.dumps(combined_properties, indent=4)
    return colony_properties_json_str
