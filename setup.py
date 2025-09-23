from setuptools import setup, find_packages
import pathlib

# Current directory
this_directory = pathlib.Path(__file__).parent

# Long description from README.md (fallback if missing)
try:
    long_description = (this_directory / "README.md").read_text(encoding="utf-8")
except FileNotFoundError:
    long_description = "Chest Cancer Classification project with Deep Learning, MLflow, and DVC."

# Requirements from requirements.txt (skip comments, -e ., and unsafe deps)
try:
    with open(this_directory / "requirements.txt", encoding="utf-8") as f:
        requirements = [
            line.strip()
            for line in f
            if line.strip()
            and not line.startswith("#")
            and not line.startswith("-e")
        ]
except FileNotFoundError:
    requirements = []

setup(
    name="chest_cancer_classification",
    version="0.1.0",
    author="SAHID ANKAN LAYEK",
    author_email="layeksahid20@gmail.com",  # ✅ replace with your actual email
    description="End-to-End Chest Cancer Classification with Deep Learning, MLflow, and DVC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SAHID-ANKAN-LAYEK/End-to-End-Chest-Cancer-Classification-with-Deep-Learning-MLflow-and-DVC",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
