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
        "langchain_openai",
        "bs4",
        "minify_html",
        "html2text",
        "langchain_aws",
        "simpleeval",
        "jsonschema",
        "undetected-playwright"
    ],
    description="A package for scraping and processing web data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="BelaidChaikhi",
    author_email="belaid@digitalent.ai",
    url="https://github.com/BelaidCh/scrapegraphai",
    )