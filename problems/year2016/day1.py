from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def part2():
    with open("data/year2016/day1.txt") as f:
        spl = f.read().split(", ")

    x, y = 0, 0
    visited = {(0, 0)}
    direction = Direction.NORTH

    for i in spl:
        turn = i[0]
        steps = int(i[1:])

        if turn == "L":
            direction = Direction((direction.value - 1) % 4)
        else:
            direction = Direction((direction.value + 1) % 4)

        for _ in range(steps):
            if direction == Direction.NORTH:
                y += 1
            elif direction == Direction.SOUTH:
                y -= 1
            elif direction == Direction.EAST:
                x += 1
            elif direction == Direction.WEST:
                x -= 1

            if (x, y) in visited:
                print("Part 2:", abs(x) + abs(y))
                return

            visited.add((x, y))
