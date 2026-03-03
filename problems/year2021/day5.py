import re

import numpy as np


with open("data/year2021/day5.txt") as f:
    spl = f.readlines()


def part_1():
    arr = np.zeros((1000, 1000))
    for line in spl:
        x1, y1, x2, y2 = [int(i) for i in re.findall(r"\d+", line)]
        if x1 == x2 or y1 == y2:
            if x1 != x2:
                if x1 > x2:
                    x1, x2 = x2, x1
                arr[y1, x1 : x2 + 1] += 1
            else:
                if y1 > y2:
                    y1, y2 = y2, y1
                arr[y1 : y2 + 1, x1] += 1

    print("Part 1:", (arr > 1).sum())


def part_2():
    arr = np.zeros((1000, 1000))
    for line in spl:
        x1, y1, x2, y2 = [int(i) for i in re.findall(r"\d+", line)]
        if x1 == x2 or y1 == y2:
            if x1 != x2:
                if x1 > x2:
                    x1, x2 = x2, x1
                arr[y1, x1 : x2 + 1] += 1
            else:
                if y1 > y2:
                    y1, y2 = y2, y1
                arr[y1 : y2 + 1, x1] += 1
        else:
            sym_x = (x2 - x1) // abs(x1 - x2)
            sym_y = (y2 - y1) // abs(y1 - y2)

            for i, j in zip(range(x1, x2 + sym_x, sym_x), range(y1, y2 + sym_y, sym_y)):
                arr[j, i] += 1

    print("Part 2:", (arr > 1).sum())
