pysystems

A python package for solving multi-varible systems of equations


Install

`` $ pip install pysystems ``

or

`` $ python -m pip install pysystems ``

Usage

`` 
import pysystems

solve = pysystems.solve

print(solve("2x+y=14", "2x+17y=21")) ---> (6.78125, 0.4375)

or

print(solve("2x+7y+3z=5", "3x+12y+z=91", "2x+9y+z=11")) ---> (189.5, -36.5, -39.5)
``
