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

def compute(days: int):
    fishes = [0 for _ in range(0, 9)]
    for i in [int(x) for x in read_file(INPUT_FILE)[0].split(',')]:
        fishes[i] += 1
    while days > 0:
        popped = fishes.pop(0) # remove the fished with the lowest timer (0)
        fishes.append(popped) # x new fished a the end, with the biggest timer
        fishes[6] += popped # Reset timer
        days -= 1
    print(sum(fishes))

def main1():
    compute(80)

def main2():
    compute(256)
    
if __name__ == "__main__":
    main1()
    main2()
