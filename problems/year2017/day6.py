with open("data/year2017/day6.txt") as f:
    spl = [int(i) for i in f.read().split()]


def part_1():
    print("Part 1:", ans())


def part_2():
    print("Part 2:", ans(2))


def ans(part=1):
    n = len(spl)
    s = []

    while spl not in s:
        s.append(spl.copy())
        ind = spl.index(max(spl))
        re = spl[ind]
        spl[ind] = 0

        for i in range(1, re + 1):
            spl[(ind + i) % n] += 1
    return len(s) if part == 1 else len(s) - s.index(spl)
