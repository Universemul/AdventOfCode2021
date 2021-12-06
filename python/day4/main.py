import itertools
import functools
import re
import math

from copy import deepcopy

INPUT_FILE = 'input.txt'

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
                result.append(func(line.strip()) if func else line.strip())
    return result

def mark_board(number, board):
    for row in board:
        for idx, _ in enumerate(row):
            if row[idx] == number:
                row[idx] = 'x'
    return board

def is_winning(board):
    result = False
    for row in board:
        if all(x == 'x' for x in row):
            return True
    return result

def main1():
    lines = read_file(INPUT_FILE)
    numbers = lines[0].split(',')
    boards = []
    idx = 2
    while idx < len(lines[2:]):
        b = []
        while idx < len(lines) and lines[idx]:
            b.append([x.strip() for x in lines[idx].split(' ') if x])
            idx += 1
        boards.append(b)
        idx += 1
    for n in numbers:
        boards = [mark_board(n, b) for b in boards]
        for b in boards:
            if is_winning(b):
                result = (int(n) * sum([int(a) for row in b for a in row if a != 'x']))
                print(result)
                return


def main2():
    lines = read_file(INPUT_FILE)
    
if __name__ == "__main__":
    main1()
    main2()
