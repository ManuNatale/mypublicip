import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypublicip",
    version="1.0.3",
    author="ManuNatale",
    author_email="",
    description="Get the public IP address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ManuNatale/mypublicip",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    setup_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3',
)