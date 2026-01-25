with open("data/year2016/day2.txt") as f:
    spl = f.read()


def part_1():
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    x = y = 1
    password = 0

    for line in spl.split("\n"):
        for i in line:
            if i == "U":
                x = max(x - 1, 0)
            elif i == "R":
                y = min(y + 1, 2)
            elif i == "L":
                y = max(y - 1, 0)
            else:
                x = min(x + 1, 2)

        password = password * 10 + keypad[x][y]

    print("Part 1:", password)


def part_2():
    keypad = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]
    x, y = 2, 0
    password = ""

    for line in spl.split("\n"):
        for i in line:
            if i == "U":
                if x > 0 and keypad[x - 1][y] != " ":
                    x -= 1
            elif i == "R":
                if y < 4 and keypad[x][y + 1] != " ":
                    y += 1
            elif i == "L":
                if y > 0 and keypad[x][y - 1] != " ":
                    y -= 1
            else:
                if x < 4 and keypad[x + 1][y] != " ":
                    x += 1

        password += keypad[x][y]

    print("Part 2:", password)
