with open("data/year2022/day5.txt") as f:
    spl = f.read().split("\n\n")
spl1 = spl[0].split("\n")
vec = [
    [el[i] for el in reversed(spl1[:-1]) if el[i] != " "]
    for i in range(1, len(spl1[-1]), 4)
]


def part_1():
    for i in spl[1].split("\n"):
        ins = [int(j) - 1 for j in i.split()[1::2]]
        for j in range(ins[0] + 1):
            if len(vec[ins[1]]) == 0:
                break
            vec[ins[2]].append(vec[ins[1]].pop())

    print("Part 1:", "".join(s.pop() for s in vec))


def part_2():
    for i in spl[1].split("\n"):
        ins = [int(j) - 1 for j in i.split()[1::2]]
        local = []

        for j in range(ins[0] + 1):
            if len(vec[ins[1]]) == 0:
                break
            local.append(vec[ins[1]].pop())
        vec[ins[2]].extend(reversed(local))

    print("Part 2:", "".join(s.pop() for s in vec))
