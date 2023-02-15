#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise and rotate in place"""


def rotate_2d_matrix(matrix):
    """
    rotate in place clockwise
    """

    row = len(matrix[0])

    for k in range(row - 1, -1, -1):
        for l in range(0, row):
            matrix[l].append(matrix[k].pop(0))
