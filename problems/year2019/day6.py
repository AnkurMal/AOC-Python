from collections import defaultdict


with open("data/year2019/day6.txt") as f:
    data = [i.split(")") for i in f.read().splitlines()]


def part_1():
    dic = {}
    for i in data:
        dic[i[1]] = i[0]
    tot = len(dic)

    for key in dic.keys():
        curr = dic[key]
        while curr != "COM":
            curr = dic[curr]
            tot += 1

    print("Part 1:", tot)


def part_2():
    dic = defaultdict(list)
    for i in data:
        dic[i[1]].append(i[0])
        dic[i[0]].append(i[1])

    res = {}
    for key in dic:
        res[key] = False

    print("Part 2:", dfs(dic, res))


def dfs(dic, res, start="YOU", count=0):
    res[start] = True

    for node in dic[start]:
        if not res[node]:
            if node == "SAN":
                return count - 1
            result = dfs(dic, res, node, count + 1)
            if result is not None:
                return result
