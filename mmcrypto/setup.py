from setuptools import setup, find_packages

setup(
    name="mmcrypto",
    author="Manas Mishra",
    author_email="manas.m22@gmail.com",
    description="Package to download, save and retrieve cryptocoins data from wazirx",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/manasm11/mmcrypto",
    version="0.0.4",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
