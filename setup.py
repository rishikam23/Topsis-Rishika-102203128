import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="topsis-102203128",  
    version="1.0.0",
    description="A Python package for multi-criteria decision analysis using the TOPSIS method.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rishikam23/Topsis-Rishika-102203128", 
    author="Rishika Mathur", 
    author_email="rmathur_be22@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["Topsis-Rishika-102203128"],
    include_package_data=True,
    install_requires=[
        "pandas>=1.0.0", 
        "numpy>=1.18.0", 
    ],
    entry_points={
        "console_scripts": [
            "topsis=102203128:main", 
        ]
    },
)
