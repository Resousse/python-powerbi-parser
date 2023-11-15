import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="powerbi-parser",
    version="1.0.4",
    description="Parser Power BI files to browse assets",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Resousse/python-powerbi-parser",
    author="Resousse",
    author_email="resousegit@gmail.com",
    license="Apache 2.0",
    classifiers=[
    ],
    package_dir = {'powerBIParser' : './'},
    packages=["powerBIParser"],
    package_data = {
        'powerBIParser': ['./LICENSE', './README.md', '*.py']
    },
    exclude_package_data={'powerBIParser' : ["setup.py"]},
    include_package_data=True
)