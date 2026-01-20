with open("data/year2016/day3.txt") as f:
    lines = f.readlines()


def part1():
    counter = 0
    for line in lines:
        nums = [int(i) for i in line.split(" ") if i]

        for i in range(3):
            if nums[i] + nums[(i + 1) % 3] <= nums[(i + 2) % 3]:
                break
        else:
            counter += 1

    print("Part 1:", counter)


def part2():
    counter = 0
    for i in range(0, len(lines) - 2, 3):
        n1 = [int(i) for i in lines[i].split(" ") if i]
        n2 = [int(i) for i in lines[i + 1].split(" ") if i]
        n3 = [int(i) for i in lines[i + 2].split(" ") if i]

        for j in range(3):
            nums = [n1[j], n2[j], n3[j]]

            for k in range(3):
                if nums[k] + nums[(k + 1) % 3] <= nums[(k + 2) % 3]:
                    break
            else:
                counter += 1

    print("Part 2:", counter)
