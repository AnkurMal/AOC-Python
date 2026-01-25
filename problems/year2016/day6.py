from collections import Counter
import numpy


with open("data/year2016/day6.txt") as f:
    data = f.read().splitlines()


def part_1():
    print("Part 1:", answer(True))


def part_2():
    print("Part 1:", answer())


def answer(reversed=False):
    arr = numpy.array([list(i) for i in data])
    return "".join(
        sorted(Counter(i).items(), key=lambda x: x[1], reverse=reversed)[0][0]
        for i in arr.T
    )
