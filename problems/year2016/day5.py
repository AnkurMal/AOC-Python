import hashlib


def part1():
    password, i = "", 0
    while len(password) != 8:
        key = "cxdnnyjw" + str(i)
        i += 1
        res = hashlib.md5(key.encode()).hexdigest()

        if res.startswith("00000"):
            password += res[5]

    print("Part 1:", password)


def part2():
    password, i = [""] * 8, 0
    while any(not j for j in password):
        key = "cxdnnyjw" + str(i)
        i += 1
        res = hashlib.md5(key.encode()).hexdigest()

        if res.startswith("00000"):
            if res[5].isdigit():
                pos = int(res[5])
                if pos < 8 and not password[pos]:
                    password[pos] = res[6]

    print("Part 2:", "".join(password))
