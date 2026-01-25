def part_2():
    with open("data/year2024/day15.txt") as f:
        raw = f.read().rstrip()

    map_part, move_part = raw.split("\n\n")
    moves = move_part.replace("\n", "")

    base = map_part.splitlines()
    grid = []

    for row in base:
        new_row = []
        for ch in row:
            if ch == "#":
                new_row.extend("##")
            elif ch == ".":
                new_row.extend("..")
            elif ch == "O":
                new_row.extend("[]")
            elif ch == "@":
                new_row.extend("@.")
        grid.append(new_row)

    H, W = len(grid), len(grid[0])

    for r in range(H):
        for c in range(W):
            if grid[r][c] == "@":
                rr, rc = r, c

    DIRS = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }

    def is_box(r, c):
        return grid[r][c] in "[]"

    def collect(r, c, dr, dc):
        stack = [(r, c)]
        seen = set()
        while stack:
            cr, cc = stack.pop()
            if (cr, cc) in seen:
                continue
            seen.add((cr, cc))
            if grid[cr][cc] == "[":
                pair = (cr, cc + 1)
            else:
                pair = (cr, cc - 1)
            seen.add(pair)
            for br, bc in ((cr, cc), pair):
                nr, nc = br + dr, bc + dc
                if grid[nr][nc] == "#":
                    return None
                if is_box(nr, nc):
                    stack.append((nr, nc))
        return seen

    for m in moves:
        dr, dc = DIRS[m]
        nr, nc = rr + dr, rc + dc

        if grid[nr][nc] == "#":
            continue

        if is_box(nr, nc):
            boxes = collect(nr, nc, dr, dc)
            if boxes is None:
                continue
            order = sorted(boxes, key=lambda x: (x[0] * dr + x[1] * dc), reverse=True)
            for br, bc in order:
                grid[br + dr][bc + dc] = grid[br][bc]
                grid[br][bc] = "."

        grid[rr][rc] = "."
        rr, rc = nr, nc
        grid[rr][rc] = "@"

    ans = 0
    for r in range(H):
        for c in range(W):
            if grid[r][c] == "[":
                ans += 100 * r + c

    print("Part 2:", ans)
