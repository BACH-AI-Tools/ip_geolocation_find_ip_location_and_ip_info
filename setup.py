"""Setup script for ip_geolocation_find_ip_location_and_ip_info"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ip_geolocation_find_ip_location_and_ip_info",
    version="1.0.0",
    author="BACH Studio",
    author_email="contact@bachstudio.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BACH-AI-Tools/ip_geolocation_find_ip_location_and_ip_info",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # 添加你的依赖
    ],
)
