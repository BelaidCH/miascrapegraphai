# scrapegraphai/setup.py
from setuptools import setup, find_packages

setup(
    name="scrapegraphai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "selenium",
        "webdriver-manager",
        "playwright",
        "free-proxy",
        "langchain",
        "langchain_community",
        # Add other dependencies here
    ],
    description="A package for scraping and processing web data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="BelaidChaikhi",
    author_email="your.email@example.com",
    url="https://github.com/BelaidChaikhi/scrapegraphai",
    )