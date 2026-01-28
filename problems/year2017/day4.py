from collections import Counter


with open("data/year2017/day4.txt") as f:
    spl = f.read()


def part_1():
    tot = 0
    for line in spl.split("\n"):
        count = Counter(line.split()).values()
        if all(i == 1 for i in count):
            tot += 1
    print("Part 1:", tot)


def part_2():
    tot = 0
    for line in spl.split("\n"):
        sor = [str(sorted(i)) for i in line.split()]
        count = Counter(sor).values()
        if all(i == 1 for i in count):
            tot += 1

    print("Part 2:", tot)
