""""""
from os.path import dirname, abspath
from setuptools import setup, find_packages

try:
    with open("README.md") as f:
        readme = f.read()
except IOError:
    readme = ""

here = dirname(abspath(__file__))
version = '0.0.1-alpha'

setup(
    name="rattlepy",
    version=version,
    url="https://github.com/frodo821/rattlepy",
    author="frodo821 <Twitter: @BoufrawFrodo2>",
    author_email='1234567890.sakai.jp@gmail.com',
    maintainer="frodo821 <Twitter: @BoufrawFrodo2>",
    maintainer_email='1234567890.sakai.jp@gmail.com',
    description="A easy-to-use pure python HTML templating libary",
    long_description=readme,
    packages=find_packages(),
    install_requires=[],
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT',
    ],
    entry_points = "")
