from itertools import permutations

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
    numbers = {2, 3, 4, 7}
    total = 0
    for line in lines:
        pattern, output = line.split(" | ")
        output = output.split(' ')
        total += sum(len(x) in numbers for x in output)
    print(total)

def main2():
    lines = read_file(INPUT_FILE)

if __name__ == "__main__":
    main1()
    main2()
