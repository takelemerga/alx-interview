#!/usr/bin/python3
"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    validate UTF-8 encoding
    """
    for b in data:
        if b >> 7 == 0:
            continue
        elif b >> 5 == 0b110:
            continue
        elif b >> 4 == 0b1110:
            continue
        elif b >> 3 == 0b11110:
            continue
        else:
            return False
    return True
