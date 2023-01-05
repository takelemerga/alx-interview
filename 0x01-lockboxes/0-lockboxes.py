#!/usr/bin/python3
"""
unlockbox module
"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened
    """
    unlockedbox = set()

    for box_index, box in enumerate(boxes):
        if len(box) == 0 or box_index == 0:
            unlockedbox.add(box_index)
        for key in box:
            if key < len(boxes) and key != box_index:
                unlockedbox.add(key)
        if len(unlockedbox) == len(boxes):
            return True
    return False
