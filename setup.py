from setuptools import setup, find_packages

setup(
    name='pysystems',
    version='1.0.1',
    packages=find_packages(exclude=['.github*']),
    license='GNU',
    description='A python package to solve multi-varible systems of equations',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/gubareve/pysystems/',
    author='Evan Gubarev',
    author_email='evan@evangubarev.com'
)
