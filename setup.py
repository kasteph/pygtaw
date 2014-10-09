from setuptools import setup

setup(
    name="pygtaw",
    version="0.0.1",
    author="Steph Samson",
    author_email="sdvsamson@gmail.com",
    description=("A tiny Google Translate API wrapper written in Python."),
    license="MIT",
    keywords="google translate API wrapper",
    url="http://github.com/stephsamson/pygtaw",
    packages=['pygtaw'],
    package_data={'pygtaw': ['LICENSE', 'README.md']},
    long_description=open('README.md').read(),
    install_requires=['requests>=2.0.0'],
)