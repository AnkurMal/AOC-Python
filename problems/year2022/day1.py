from collections import deque


def part_1():
    with open("data/year2022/day5.txt") as f:
        spl = f.read().split("\n\n")
        spl1 = spl[0].split("\n")
        vec = []

        for i in range(len(spl1[-1])):
            if spl1[-1][i].isdigit():
                queue = deque()
                for el in spl1[:-1]:
                    if el[i] != " ":
                        queue.appendleft(el[i])
                vec.append(queue)

        for i in spl[1].split("\n"):
            ins = [int(j) - 1 for j in i.split()[1::2]]
            for j in range(ins[0] + 1):
                if len(vec[ins[1]]) == 0:
                    break
                vec[ins[2]].append(vec[ins[1]].pop())

        st = "".join(s.pop() for s in vec)
        print("Part 1:", st)


def part_2():
    with open("data/year2022/day5.txt") as f:
        spl = f.read().split("\n\n")
        spl1 = spl[0].split("\n")
        vec = []

        for i in range(len(spl1[-1])):
            if spl1[-1][i].isdigit():
                queue = deque()
                for el in spl1[:-1]:
                    if el[i] != " ":
                        queue.appendleft(el[i])
                vec.append(queue)

        for i in spl[1].split("\n"):
            ins = [int(j) - 1 for j in i.split()[1::2]]
            local = deque()

            for j in range(ins[0] + 1):
                if len(vec[ins[1]]) == 0:
                    break
                local.appendleft(vec[ins[1]].pop())
            vec[ins[2]].extend(local)

        st = "".join(s.pop() for s in vec)
        print("Part 2:", st)
