import itertools
import functools
import re
import math

from collections import Counter
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
    gamma_rate = ""
    epsilon_rate = ""
    for idx in range(0, len(lines[0])):
        bits_counter = Counter([x[idx] for x in lines]).most_common(2)
        g_bit = bits_counter[0][0]
        e_bit = bits_counter[1][0]
        
        gamma_rate += g_bit
        epsilon_rate += e_bit

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    print(gamma_rate * epsilon_rate)

def get_oxygen_rating(lines, idx=0):
    if len(lines) == 1:
        return lines[0]
    most_commons = Counter([x[idx] for x in lines]).most_common(2)
    if most_commons[0][1] == most_commons[1][1] and most_commons[0][0] == '0':
        most_common = most_commons[1][0]
    else:
        most_common = most_commons[0][0]
    return get_oxygen_rating([x for x in lines if x[idx] == most_common], idx + 1)

def get_co2(lines, idx=0):
    if len(lines) == 1:
        return lines[0]
    less_commons = Counter([x[idx] for x in lines]).most_common(2)
    if less_commons[0][1] == less_commons[1][1] and less_commons[0][0] == '0':
        less_common = less_commons[0][0]
    else:
        less_common = less_commons[1][0]
    return get_co2([x for x in lines if x[idx] == less_common], idx + 1)


def main2():
    lines = read_file(INPUT_FILE)
    oxygen_rating = int(get_oxygen_rating(lines), 2)
    co2_rating = int(get_co2(lines), 2)
    print(oxygen_rating * co2_rating)
    
if __name__ == "__main__":
    main1()
    main2()
