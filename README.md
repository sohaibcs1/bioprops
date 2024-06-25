# BioProps

BioProps is a Python library for computing properties from medical images, particularly for analyzing cell nuclei and colonies in 3D space. It provides functions to calculate properties such as elongation, flatness, volume, size, and edge lengths from NIfTI files representing binary cell data.

## Installation

You can install BioProps using pip:

```sh
pip install BioProps
```

## Usage

```python
from bioprops import properties_from_nifti

nifti_file = 'path_to_your_nifti_file.nii.gz'
properties = properties_from_nifti(nifti_file)
print(properties)
```

## Functions

### `properties_from_nifti(nifti_file)`

Calculates properties of cell nuclei and colonies from a NIfTI file.

- **Parameters**:
  - `nifti_file` (str): Path to the NIfTI file.

- **Returns**:
  - (str): JSON-formatted string containing computed properties.

## Example

For example, to calculate properties from a NIfTI file:

```python
from bioprops import properties_from_nifti

nifti_file = 'example.nii.gz'
properties = properties_from_nifti(nifti_file)
print(properties)
```

## Dependencies

- numpy
- nibabel
- scipy
- scikit-image

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
