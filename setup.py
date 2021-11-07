import pathlib
import re

from setuptools import setup

ROOT = pathlib.Path(__file__).parent

with open('ferrischat_cli/__init__.py', 'r') as f:
    content = f.read()
    try:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)  # type: ignore
    except AttributeError:
        raise RuntimeError('Unable to find version string')

    try:
        author = re.search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)  # type: ignore
    except AttributeError:
        author = 'Cryptex'

# with open('requirements.txt', 'r') as f:
#     requirements = f.readlines()


with open(ROOT / 'README.md', encoding='utf-8') as f:
    readme = f.read()

with open(ROOT / 'requirements.txt', encoding='utf-8') as f:
    requirements = f.readlines()

setup(
    name="ferrischat-cli",
    author=author,
    url="https://github.com/Cryptex-github/ferrischat-cli",
    project_urls={
        "Issue tracker": "https://github.com/Cryptex-github/ferrischat-cli/issues/new",
    },
    version=version,
    packages=["ferrischat_cli"],
    license="EUPL v1.2",
    description="A CLI Client for FerrisChat using FerrisWheel",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8.0",
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)
