#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    print pascal triangle
    """
    list = []
    if (n > 0):
        for line in range(1, n + 1):
            k = 1
            list.clear()
            for i in range(1, line + 1):
                list.append(k)
                k = int(k * (line - i)/i)
            print(list)
    else:
        print(list)
