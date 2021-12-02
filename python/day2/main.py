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
    lines = read_file(INPUT_FILE)
    position = 0
    depth = 0
    for l in lines:
        inst, value = l.split(' ')
        value = int(value)
        if inst == "forward":
            position += value
        elif inst == "down":
            depth += value
        else:
            depth -= value
    print(position * depth)

def main2():
    lines = read_file(INPUT_FILE)
    position = 0
    depth = 0
    aim = 0
    for l in lines:
        inst, value = l.split(' ')
        if inst == "forward":
            position += int(value)
            depth += aim * int(value)
        elif inst == "down":
            aim += int(value)
        else:
            aim -= int(value)
    print(depth * position)
    
if __name__ == "__main__":
    main1()
    main2()
