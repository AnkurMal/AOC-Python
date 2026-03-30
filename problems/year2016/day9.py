with open("data/year2016/day9.txt") as f:
    data = "".join(f.read().split())


def decompressed_length(s, recursive=False):
    length = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            j = s.index(")", i)
            num_chars, times = map(int, s[i + 1 : j].split("x"))
            chunk = s[j + 1 : j + 1 + num_chars]
            if recursive:
                length += times * decompressed_length(chunk, recursive=True)
            else:
                length += times * num_chars
            i = j + 1 + num_chars
        else:
            length += 1
            i += 1
    return length


def part_1():
    print("Part 1:", decompressed_length(data))


def part_2():
    print("Part 2:", decompressed_length(data, recursive=True))
