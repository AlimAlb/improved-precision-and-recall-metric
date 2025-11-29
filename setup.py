from pathlib import Path

from setuptools import find_packages, setup


def read_readme() -> str:
    readme_path = Path(__file__).with_name("README.md")
    if readme_path.exists():
        return readme_path.read_text(encoding="utf-8")
    return ""


setup(
    name="improved-precision-recall-metric",
    version="0.1.0",
    description="Improved Precision and Recall metric for assessing generative models (NVIDIA research implementation).",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="NVIDIA Corporation",
    license="CC BY-NC 4.0",
    python_requires=">=3.6",
    packages=find_packages(include=["dnnlib", "dnnlib.*"]),
    py_modules=[
        "precision_recall",
        "run_metric",
        "experiments",
        "ffhq_datareader",
        "utils",
    ],
    install_requires=[
        "numpy>=1.16.0",
        "tensorflow",
    ],
    extras_require={
        "gpu": [
            "tensorflow-gpu>=1.12,<2.11",
        ],
    },
)



