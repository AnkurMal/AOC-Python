with open("data/year2017/day5.txt") as f:
    spl = [int(i) for i in f.readlines()]


def part_1():
    count = i = 0
    while i < len(spl):
        spl[i] += 1
        i += spl[i] - 1
        count += 1
    print("Part 1:", count)


def part_2():
    count = i = 0
    while i < len(spl):
        prev = i
        i += spl[i]
        spl[prev] += -1 if spl[prev] >= 3 else 1
        count += 1
    print("Part 2:", count)
