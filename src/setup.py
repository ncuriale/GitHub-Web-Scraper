from setuptools import setup, find_packages

setup(
    name='github_scraper',
    version='1.0',
    packages=find_packages(),
    author='Nathan Curiale',
    author_email="nathan.curiale@hotmail.com",
    description='GitHub Scraper',
    install_requires=[
        "numpy >= 1.9.0",
        "scipy >= 0.14.0",
        "scikit-learn >= 0.18.0",
    ],
)