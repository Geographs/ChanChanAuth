import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ChanChanAuth",
    version="0.0.1",
    author="Geographs",
    author_email="87452561+Geographs@users.noreply.github.com",
    description="A simple Python wrapper for https://api.ccauth.app/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Geographs/ChanChanAuth",
    project_urls={
        "Bug Tracker": "https://github.com/Geographs/ChanChanAuth/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
