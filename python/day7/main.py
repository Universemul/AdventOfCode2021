import sys

from math import floor, ceil
from statistics import median, mean

INPUT_FILE = 'input.txt'


def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result


def main1():
    crabs = [int(x) for x in read_file(INPUT_FILE)[0].split(',')]
    _median = int(median(crabs))
    fuel = sum([abs(x-_median) for x in crabs])
    print(f"Part 1: {fuel}")


def main2():
    crabs = [int(x) for x in read_file(INPUT_FILE)[0].split(',')]
    _mean = mean(crabs)
    position1 = floor(_mean)
    position2 = ceil(_mean)
    fuel = sys.maxsize
    for pos in [position1, position2]:
        _fuel = 0
        for x in crabs:
            diff = abs(x - pos)
            _fuel += diff * (diff + 1) // 2
        fuel = min(_fuel, fuel)
    print(f"Part 2: {fuel}")

if __name__ == "__main__":
    main1()
    main2()
