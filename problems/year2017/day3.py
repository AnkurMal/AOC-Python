def ans1(find):
    n = int(find**0.5) + 1
    n += 1 - n % 2
    li = [[0] * n for i in range(n)]
    x = y = n // 2
    i = d = val = 1
    li[x][y] = 1

    try:
        while True:
            for _ in range(i):
                val += 1
                x += d
                if val == find:
                    return abs(n // 2 - y) + abs(n // 2 - x)
                li[y][x] = val
            for _ in range(i):
                val += 1
                y -= d
                if val == find:
                    return abs(n // 2 - y) + abs(n // 2 - x)
                li[y][x] = val
            d *= -1
            i += 1
    except IndexError:
        return 0


def ans2(find):
    n = int(find**0.5) + 1
    n += 1 - n % 2
    li = [[0] * n for i in range(n)]
    x = y = n // 2
    i = d = 1
    li[x][y] = 1

    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    try:
        while True:
            for _ in range(i):
                val = 0
                x += d
                for dir in dirs:
                    x1, y1 = x + dir[0], y + dir[1]
                    if 0 <= x1 < n and 0 <= y1 < n:
                        val += li[y1][x1]
                if val > find:
                    return val
                li[y][x] = val
            for _ in range(i):
                val = 0
                y -= d
                for dir in dirs:
                    x1, y1 = x + dir[0], y + dir[1]
                    if 0 <= x1 < n and 0 <= y1 < n:
                        val += li[y1][x1]
                if val > find:
                    return val
                li[y][x] = val
            d *= -1
            i += 1
    except IndexError:
        return 0


def part_1():
    print("Part 1:", ans1(325489))


def part_2():
    print("Part 2:", ans2(325489))
