from setuptools import setup, find_packages

setup(
    name="phagepickr",
    version="1.0",
    description="A tool to design evolution-proof phage cocktails against pathogenic bacteria",
    author="Alessandro Oneto",
    author_email="asoneto@ncsu.edu",
    packages=find_packages(include=["phagepickr", "phagepickr.*"]),
    package_data={
        "phagepickr": ["receptor_data.json", "phagedicts.json"]
    },
    include_package_data=True,
    entry_points={
        "console_scripts": ["phagepickr=phagepickr.main:cli"]
    },
    install_requires=[
    "biopython",
    "numpy",
    "pandas",
    "scikit-learn",
    "scipy",
    ],
    python_requires=">=3.11",  
)
