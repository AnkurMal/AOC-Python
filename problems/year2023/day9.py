with open("data/year2023/day9.txt") as f:
    data = f.readlines()


def part_1():
    total = 0
    for line in data:
        list = [int(x) for x in line.split()]
        sum = 0

        while not all(x == 0 for x in list):
            sum += list[-1]
            list = [list[i + 1] - list[i] for i in range(len(list) - 1)]
        total += sum

    print("Part 1:", total)


def part_2():
    total = 0
    for line in data:
        list = [int(x) for x in line.split()]
        first = []

        while not all(x == 0 for x in list):
            first.append(list[0])
            list = [list[i + 1] - list[i] for i in range(len(list) - 1)]

        sum = 0
        for i in reversed(first):
            sum = i - sum
        total += sum

    print("Part 1:", total)
