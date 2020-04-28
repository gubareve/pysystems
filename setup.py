from setuptools import setup, find_packages

setup(
    name='pysystemst',
    version='1.6.2',
    packages=find_packages(exclude=['.github*']),
    license='GNU',
    description='a python package to generate blocktext',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/gubareve/pysystems/',
    author='Evan Gubarev',
    author_email='evan@evangubarev.com'
)
