from setuptools import setup, find_packages

setup(
    name="phagepickr",
    description="A tool to design evolution-proof phage cocktails against pathogenic bacteria",
    author="Alessandro Oneto",
    author_email="alekey039@hotmail.com",
    packages=find_packages(include=["phagepickr", "phagepickr.*"]),
    package_data={
        "phagepickr": ["receptor_data.json", "phagedicts.json"]
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "phagepickr=phagepickr.main:cli", 
        ],
    },
    install_requires=[
    "biopython",
    "Bottleneck",
    "joblib",
    "numexpr",
    "numpy",
    "pandas",
    "python-dateutil",
    "pytz",
    "scikit-learn",
    "scipy",
    "six",
    "threadpoolctl",
    "tzdata"
    ],
    python_requires=">=3.11",  
)