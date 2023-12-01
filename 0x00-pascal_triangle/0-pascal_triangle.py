#!/usr/bin/python3
"""
pascals tiangle
"""
from math import factorial


def pascal_triangle(n):
    """
    pascat_triangle: pascsl triangle
    args:
        n: number of rows
    """

    triangle = []

    for index in range(n):
        row = [factorial(index)//(factorial(j)*factorial(index-j))
               for j in range(index+1)]
        triangle.append(row)
    return triangle
