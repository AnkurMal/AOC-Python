from collections import Counter, defaultdict
import re


with open("data/year2018/day4.txt") as f:
    spl = f.read().splitlines()


def part_1():
    spl1 = [i.split("] ") for i in spl]
    spl1.sort(key=lambda x: x[0])
    ident = 0
    dur = defaultdict(list)
    tot = defaultdict(int)

    for ind, i in enumerate(spl1):
        if var := re.findall(r"\d+", i[1]):
            ident = int(var[0])
        elif i[1] == "wakes up":
            t1 = int(spl1[ind - 1][0][-2:])
            t2 = int(i[0][-2:])
            dur[ident].append((t1, t2))
            tot[ident] += t2 - t1

    key = sorted(tot.items(), key=lambda x: x[1])[-1][0]
    frames = sorted(
        Counter(j for i in dur[key] for j in range(i[0], i[1])).items(),
        key=lambda x: x[1],
    )[-1][0]

    print("Part 1:", key * frames)


def part_2():
    spl1 = [i.split("] ") for i in spl]
    spl1.sort(key=lambda x: x[0])
    ident = 0
    dur = defaultdict(list)

    for ind, i in enumerate(spl1):
        if var := re.findall(r"\d+", i[1]):
            ident = int(var[0])
        elif i[1] == "wakes up":
            t1 = int(spl1[ind - 1][0][-2:])
            t2 = int(i[0][-2:])
            dur[ident].append((t1, t2))

    max_list = [0] * 3
    for key in dur:
        frames = list(
            sorted(
                Counter(j for i in dur[key] for j in range(i[0], i[1])).items(),
                key=lambda x: x[1],
            )[-1]
        )
        frames.append(key)
        if frames[1] > max_list[1]:
            max_list = frames

    print("Part 2:", max_list[0] * max_list[-1])
