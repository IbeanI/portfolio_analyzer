from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="portfolio_analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Daniel Zito",
    author_email="sig.danielzito@gmail.com",
    description="A comprehensive tool to analyze investment portfolio transactions",
)
