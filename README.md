# [pysystems](https://pypi.org/project/pysystems/)


A python package for solving multi-varible systems of equations

![PyPI](https://img.shields.io/pypi/v/pysystems)![Python package](https://github.com/gubareve/pysystems/workflows/Python%20package/badge.svg)![Upload Python Package](https://github.com/gubareve/pysystems/workflows/Upload%20Python%20Package/badge.svg)


# Install
``` $ pip install pysystems ```
or
``` $ python -m pip install pysystems ```

# Usage
``` 
import pysystems
solve = pysystems.solve
print(solve("2x+y=14", "2x+17y=21")) ---> (6.78125, 0.4375)
or
print(solve("2x+7y+3z=5", "3x+12y+z=91", "2x+9y+z=11")) ---> (189.5, -36.5, -39.5)
```
