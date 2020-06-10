import setuptools

setuptools.setup(
    name = "mpl_tune",
    version = "0.2",
    author = "Alexandre Emsenhuber",
    author_email = "emsenhuber@lpl.arizona.edu",
    description = "A collection of matplotlib tuning scripts",
    long_description = open( "README.md", "r" ).read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/aemsenhuber/mpl_tune",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
