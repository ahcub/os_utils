from distutils.core import setup

from setuptools import find_packages


with open('README.md') as file:
    long_description = file.read()


setup(
    name='os_utils',
    packages=find_packages(include=('os_utils', )),
    version='0.1.5',
    description='os utils to reduce code copy paste',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alex Buchkovsky',
    author_email='olex.buchkovsky@gmail.com',
    url='https://github.com/ahcub/os_utils',
    keywords=['logging', 'path', 'dirs', 'files'],
)
