#!/usr/bin/python3

"""prime game module"""

mariaWins = 0
benWins = 0
winner = ""


def isWinner(x, nums):
    """returns the winner"""
    global mariaWins
    global benWins

    for i in nums:
        playgame(i)
    if (mariaWins > benWins):
        winner = "Maria"
    elif (mariaWins < benWins):
        winner = "Ben"
    else:
        return None
    return winner


def playgame(num_integers):
    """play game"""

    lst = []
    for j in range(1, num_integers + 1):
        lst.append(j)

    mariaPlay(lst)


def mariaPlay(lst):
    """maria play"""
    prime = False
    for k in lst:
        prime = isPrime(k)
        if (prime):
            for h in range(k):
                multiples = h * k
                if (multiples in lst):
                    lst.remove(multiples)
    if (prime):
        benPlay(lst)
    else:
        global benWins
        benWins += 1


def benPlay(lst):
    """ben play"""
    prime = False
    for k in lst:
        prime = isPrime(k)
        if (prime):
            for h in range(k):
                multiples = h * k
                if (multiples in lst):
                    lst.remove(multiples)
    if (prime):
        mariaPlay(lst)
    else:
        global mariaWins
        mariaWins += 1


def isPrime(n):
    """check number"""
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True
