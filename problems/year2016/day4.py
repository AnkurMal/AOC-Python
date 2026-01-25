from collections import Counter


with open("data/year2016/day4.txt") as f:
    data = f.read()


def part_1():
    sum = 0
    for line in data.splitlines():
        spl = line.split("-")
        gen = "".join(
            i[0]
            for i in sorted(
                Counter("".join(spl[:-1])).items(), key=lambda x: (-x[1], x[0])
            )[:5]
        )
        checksum = spl[-1][-6:-1]

        if gen == checksum:
            sum += int(spl[-1][0:3])

    print("Part 1:", sum)


def part_2():
    for line in data.splitlines():
        spl = line.split("-")
        gen = "".join(
            i[0]
            for i in sorted(
                Counter("".join(spl[:-1])).items(), key=lambda x: (-x[1], x[0])
            )[:5]
        )
        checksum = spl[-1][-6:-1]

        if gen == checksum:
            new = "".join(
                chr((ord(i) - ord("a") + int(spl[-1][0:3])) % 26 + ord("a"))
                if i != "-"
                else " "
                for i in line[:-11]
            )

            if "north" in new:
                print("Part 2:", int(spl[-1][0:3]))
                return
