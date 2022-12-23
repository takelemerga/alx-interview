#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    print pascal triangle
    """
    lis = []
    if (n > 0):
        for line in range(1, n + 1):
            lst = []
            k = 1
            for i in range(1, line + 1):
                lst.append(k)
                k = int(k * (line - i)/i)
            lis.append(lst)
        return (lis)
    else:
        return (lis)
