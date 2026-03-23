with open("data/year2021/day10.txt") as f:
    spl = f.read()


def part_1():
    tot = 0
    for line in spl.splitlines():
        stack = []

        for i in line:
            if i == ")":
                if stack[-1] != "(":
                    tot += 3
                    break
                else:
                    stack.pop()
                    continue
            elif i == "}":
                if stack[-1] != "{":
                    tot += 1197
                    break
                else:
                    stack.pop()
                    continue
            elif i == "]":
                if stack[-1] != "[":
                    tot += 57
                    break
                else:
                    stack.pop()
                    continue
            elif i == ">":
                if stack[-1] != "<":
                    tot += 25137
                    break
                else:
                    stack.pop()
                    continue
            stack.append(i)

    print("Part 1:", tot)


def part_2():
    points = []
    for line in spl.splitlines():
        stack = []

        for i in line:
            if i == ")":
                if stack[-1] != "(":
                    break
                else:
                    stack.pop()
                    continue
            elif i == "}":
                if stack[-1] != "{":
                    break
                else:
                    stack.pop()
                    continue
            elif i == "]":
                if stack[-1] != "[":
                    break
                else:
                    stack.pop()
                    continue
            elif i == ">":
                if stack[-1] != "<":
                    break
                else:
                    stack.pop()
                    continue
            stack.append(i)
        else:
            score = 0
            table = {"(": 1, "[": 2, "{": 3, "<": 4}
            for i in reversed(stack):
                score = score * 5 + table[i]

            points.append(score)

    points.sort()
    print("Part 2:", points[len(points) // 2])
