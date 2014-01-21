import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    version = "0.0.1",
    name = "panatomy",
    author = "DongWoo Lee",
    author_email = "leepro@gmail.com",
    description = ("Python Anatomy Tool"),
    license = "MIT",
    keywords = "python anatomy autopsy",
    url = "http://packages.python.org/panatomy",
    packages=find_packages(),
    test_suite='tests',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
