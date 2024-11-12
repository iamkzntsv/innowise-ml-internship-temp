from setuptools import setup, find_packages

test_deps = [
    "pip>=24.3.0",
    "flake8>=6.0.0",
    "black>=22.6.0",
]

extras = {"test": test_deps}

setup(
    name="innowise-ml-internship",
    version="0.1.0",
    author="john doe",
    author_email="johndoe@innowise.com",
    description="Description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/yourpackage",
    packages=find_packages(),
    install_requires=["pandas>=2.0.0"],
    extras_require=extras,
)
