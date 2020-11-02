import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piClusterNetworking",
    version="0.0.2",
    author="Trevor White",
    author_email="trevor.white@wayne.edu",
    description="Raspberry pi cluster custom server/client library for distributed computing and code testing. This package can be imported to create a custom client/server for any program to send/receive/compute data across any number of clustered raspberry pis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trevtravtrev/piCluster",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)