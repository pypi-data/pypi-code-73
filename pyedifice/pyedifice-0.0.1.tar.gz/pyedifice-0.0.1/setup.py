import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyedifice", # Replace with your own username
    version="0.0.1",
    author="David Ding",
    author_email="davidding2000@gmail.com",
    description="A declarative UI framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
