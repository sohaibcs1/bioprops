from setuptools import setup, find_packages

setup(
    name="BioProps",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "nibabel",
        "scipy",
        "scikit-image"
    ],
    author="Muhammad Sohaib",
    author_email="sohaib.cs1@gmail.com",
    description="A Python library for computing properties of cell nuclei and colonies from NIfTI files, enabling analysis of cellular structures in medical images.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/sohaibcs1/bioprops",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
