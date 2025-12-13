with open("data/year2022/day6.txt") as f:
    data = f.read()


def part_1():
    solve(4, 1)


def part_2():
    solve(14, 2)


def solve(marker, part):
    for i in range(len(data) - marker):
        if len(set(data[i : i + marker])) == marker:
            print(f"Part {part}: {i + marker}")
            break
