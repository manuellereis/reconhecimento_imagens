from setuptools import setup, find_packages

setup(
    name="BlacklistX",
    version="0.1.0",
    description="Add your description here",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    packages=find_packages(include=["scripts", "scripts.*"]),
    include_package_data=True,
    install_requires=[
        "face-recognition-models>=0.3.0",
        "face-recognition>=1.3.0",
        "ipykernel>=6.29.5",
        "opencv-python>=4.10.0.84",
        "psycopg2-binary>=2.9.10",
        "fastapi",
        "cmake>=4.0.2",
        "dlib>=19.24.6",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
)
