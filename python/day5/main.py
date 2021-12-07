import collections
import itertools

INPUT_FILE = 'input.txt'

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result

def vec_to_pts(vector, with_diagonales=False):
    (x1, y1), (x2, y2) = vector
    if x1 == x2:
        inf = min(y1, y2)
        sup = max(y1, y2)
        return [(x1, y) for y in range(inf, sup + 1)]
    elif y1 == y2:
        inf = min(x1, x2)
        sup = max(x1, x2)
        return [(x, y1) for x in range(inf, sup + 1)]
    elif with_diagonales:
        slope = round((y2-y1) / (x2-x1))
        intercept = y2-slope*x2
        _range = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
        return [(x, round(slope*x+intercept)) for x in _range]
    return []


def main1():
    lines = read_file(INPUT_FILE)
    vectors = []
    for l in lines:
        c1, c2 = [x.split(',') for x in l.split(' -> ')]
        x1, y1 = [int(x) for x in c1]
        x2, y2 = [int(x) for x in c2]
        vectors.append([(x1, y1), (x2, y2)])
    points = collections.Counter(itertools.chain(*[vec_to_pts(vector, False) for vector in vectors]))
    print(len([1 for _, val in points.items() if val > 1]))


def main2():
    lines = read_file(INPUT_FILE)
    vectors = []
    for l in lines:
        c1, c2 = [x.split(',') for x in l.split(' -> ')]
        x1, y1 = [int(x) for x in c1]
        x2, y2 = [int(x) for x in c2]
        vectors.append([(x1, y1), (x2, y2)])
    points = collections.Counter(itertools.chain(*[vec_to_pts(vector, True) for vector in vectors]))
    print(len([1 for _, val in points.items() if val > 1]))

if __name__ == "__main__":
    main1()
    main2()
