import re

import numpy as np


with open("data/year2018/day3.txt") as f:
    spl = f.readlines()


def part_1():
    arr = np.zeros((1000, 1000))
    for line in spl:
        x, y, w, h = [int(i) for i in re.findall(r"\d+", line)[1:]]
        arr[y : y + h, x : x + w] += 1
    print("Part 1:", (arr > 1).sum())


def part_2():
    arr = np.zeros((1000, 1000))
    coords = []

    for line in spl:
        x, y, w, h = [int(i) for i in re.findall(r"\d+", line)[1:]]
        coords.append((x, y, w, h))
        arr[y : y + h, x : x + w] += 1

    for c, (x, y, w, h) in enumerate(coords):
        if np.all(arr[y : y + h, x : x + w] == 1):
            print("Part 2:", c + 1)
            break
