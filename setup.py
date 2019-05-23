"""
jxctl - setup
"""
import os
import setuptools
from jxctl.clicore import __author__, __email__, __version__

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()

if os.environ["CIRCLE_BRANCH"] == "develop":
    __version__ = __version__ + ".dev" + os.environ["CIRCLE_BUILD_NUM"]

setuptools.setup(
    name="jxctl",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="A Command line interface for Jenkins",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/deepan10/jxctl",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'PyYAML>=4.2b1',
        'Click>=7.0',
        'requests>=2.20.1',
        'tabulate>=0.8.2',
        'pyfiglet>=0.7.6',
        'python-jenkins>=1.4.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'jxctl = jxctl.clicore:start'
        ]
    },
)
