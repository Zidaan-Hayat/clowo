import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="owoifyer", # Replace with your own username
    version="1.0.0",
    author="Zzz9194",
    author_email="doczidaan@gmail.com",
    description="Turn your bland old english into a fuwwy poetic mastewpiece",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zidaan-Hayat/owoifyer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)