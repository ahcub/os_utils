from distutils.core import setup

from setuptools import find_packages

setup(
    name='os_utils',
    packages=find_packages(include=('os_utils', )),
    version='0.1.0',
    description='os utils to reduce code copy paste',
    author='Alex Buchkovsky',
    author_email='olex.buchkovsky@gmail.com',
    url='https://github.com/ahcub/armory/tree/master/os_utils',
    keywords=['logging', 'path', 'dirs', 'files'],
)
