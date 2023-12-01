#!/usr/bin/python3
"""
pascals tiangle
"""


def factorial(n):
    """
    factorial: returns a factorial of n
    args:
        n: number
    """
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac


def pascal_triangle(n):
    """
    pascal_triangle: pascal triangle
    args:
        n: number of rows
    """

    triangle = []

    for index in range(n):
        row = [factorial(index)//(factorial(j)*factorial(index-j))
               for j in range(index+1)]
        triangle.append(row)
    return triangle
