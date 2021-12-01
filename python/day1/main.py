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

def main1():
    lines = read_file(INPUT_FILE, int)
    increased = 0
    for idx in range(1, len(lines)):
        if lines[idx] > lines[idx - 1]:
            increased += 1
    print(increased)

def main2():
    lines = read_file(INPUT_FILE, int)
    increased = 0
    for idx in range(3, len(lines)):
        if sum(lines[idx-3:idx]) < sum(lines[idx-2:idx+1]):
            increased += 1
    print(increased)
    
if __name__ == "__main__":
    main1()
    main2()
