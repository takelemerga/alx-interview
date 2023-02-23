#!/usr/bin/python3
"""pile module"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    given a pile of coins of different values
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    temp = 0

    for coin in coins:
        if total % coin <= total:
            temp += total // coin
            total = total % coin
    return temp if total == 0 else -1

