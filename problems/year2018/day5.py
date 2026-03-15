import string
import sys


def part_1():
    with open("data/year2018/day5.txt") as f:
        spl1 = f.read()

    stack = []
    for c in spl1:
        if stack and abs(ord(stack[-1]) - ord(c)) == 32:
            stack.pop()
        else:
            stack.append(c)

    print("Part 1:", len(stack))


def part_2():
    with open("data/year2018/day5.txt") as f:
        spl1 = f.read()

    mi = sys.maxsize

    for let in string.ascii_lowercase:
        filtered = (c for c in spl1 if c.lower() != let)
        stack = []
        for c in filtered:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)
        mi = min(mi, len(stack))

    print("Part 2:", mi)
