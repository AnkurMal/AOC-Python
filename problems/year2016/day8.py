import re

import numpy as np


with open("data/year2016/day8.txt") as f:
    lines = f.read().splitlines()


def get_trans():
    arr = np.zeros((6, 50))
    pat = re.compile(r"\d+")

    for line in lines:
        num = [int(i) for i in pat.findall(line)]

        if "rect" in line:
            arr[: num[-1], : num[0]] = 1
        elif "column" in line:
            arr[:, num[0]] = np.roll(arr[:, num[0]], num[-1])
        else:
            arr[num[0]] = np.roll(arr[num[0]], num[-1])

    return arr


def part_1():
    print("Part 1:", (get_trans() == 1).sum())


def part_2():
    arr = get_trans()
    print("Part 2:\n")
    for r in range(6):
        print(
            " ".join(
                "".join("#" if x else " " for x in arr[r, i : i + 5])
                for i in range(0, 50, 5)
            )
        )
