import numpy as np

with open("data/year2021/day6.txt") as f:
    spl = f.read()


def count(it):
    fish_timers = np.array([int(i) for i in spl.split(",")])
    counts = np.bincount(fish_timers, minlength=9)

    for _ in range(it):
        counts = np.roll(counts, -1)
        counts[6] += counts[8]
    return counts.sum()


def part_1():
    print("Part 1:", count(80))


def part_2():
    print("Part 2:", count(256))
