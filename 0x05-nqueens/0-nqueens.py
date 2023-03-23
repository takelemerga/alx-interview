#!/usr/bin/python3
"""
N puzzle quens 
"""
import sys


def board_init(n):
    """
    initialize board
    """
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    place(board, 0)


def place(board, col):
    """
    place queens
    """
    if col >= len(board):
        print_board(board, len(board))

    for i in range(len(board)):
        if no_attack(board, i, col):
            board[i][col] = 1
            result = place(board, col + 1)
            if result:
                return True
            board[i][col] = 0
    return False


def no_attack(board, i, j):
    """
    Checks if a position of the queen is valid

    Returns:
        Boolean: True if no attack, False otherwise
    """
    # Check this row on left side
    if 1 in board[i]:
        return False

    upper_diag = zip(range(i, -1, -1),
                     range(j, -1, -1))
    for k, l in upper_diag:
        if board[k][l] == 1:
            return False

    lower_diag = zip(range(i, len(board), 1),
                     range(j, -1, -1))
    for k, l in lower_diag:
        if board[k][l] == 1:
            return False

    return True


def print_board(board, n):
    """
    Prints positions of the queens
    """
    brd = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                brd.append([i, j])
    print(brd)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    queens = sys.argv[1]
    if not queens.isnumeric():
        print("N must be a number")
        exit(1)
    elif int(queens) < 4:
        print("N must be at least 4")
        exit(1)
    board_init(int(queens))
