import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="KorailSeat",
    version="0.0.1",
    author="smbyeon",
    author_email="smbyun0214@gmail.com",
    description="Korail Seat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smbyeon/KorailSeat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)