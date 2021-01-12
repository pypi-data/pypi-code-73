import setuptools


setuptools.setup(
    name ="RandoWordo",
    version="1.1",
    author = "Ewen",
    author_email = "1lorimerewe2@gmail.com",
    description = "a simple random word generator",
    long_description = "All you need to know is RandWord(textfile.txt), or randoword() if you don't have a pre defined text file \
        \ the default text file does contair swears and NSFW words",
    long_description_content_type = "text/markdown",
    packages= setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",

        
        "Operating System :: OS Independent"

    ],
    python_requires='<=3.9',
)

