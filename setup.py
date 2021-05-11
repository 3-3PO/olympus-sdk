import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="olympus-sdk", # Replace with your own username
    version="0.1.0",
    author="3-3PO",
    description="SDK for Olympus DAO (OHM) contracts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/3-3PO/olympus-sdk",
    project_urls={
        "Bug Tracker": "https://github.com/3-3PO/olympus-sdk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "olympus"},
    packages=setuptools.find_packages(where="olympus"),
    python_requires=">=3.6",
    install_requires=[
        'web3>5,<6',
    ],
)