import re


with open("data/year2016/day7.txt") as f:
    data = f.read().splitlines()


def part_1():
    count = 0
    for i in data:
        parts = re.split(r"\[|\]", i)
        brac = parts[1::2]
        out = parts[::2]

        if not any(check_abba(j) for j in brac) and any(check_abba(j) for j in out):
            count += 1
    print("Part 1:", count)


def part_2():
    count = 0
    for i in data:
        parts = re.split(r"\[|\]", i)
        brac = get_aba(parts[1::2])
        out = get_aba(parts[::2])

        for j in brac:
            new = j[1] + j[0] + j[1]
            if new in out:
                count += 1
                break

    print("Part 2:", count)


def check_abba(st):
    for i in range(len(st) - 3):
        a, b, c, d = st[i : i + 4]
        if a == d and b == c and a != b:
            return True
    return False


def get_aba(vec):
    res = []
    for i in vec:
        for j in range(len(i) - 2):
            a, b, c = i[j : j + 3]
            if a == c and a != b:
                res.append(i[j : j + 3])
    return res
