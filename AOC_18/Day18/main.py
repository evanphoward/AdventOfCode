grid = dict()
inp = open("input").read().strip().split("\n")
for r, row in enumerate(inp):
    for c, cell in enumerate(row.strip()):
        grid[r, c] = cell

height = len(inp)
width = len(inp[0])
nbrs = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1)]


def step(g):
    new_g = dict()
    for r in range(height):
        for c in range(width):
            trees = 0
            lumber = 0
            for dr, dc in nbrs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < height and 0 <= nc < width:
                    if g[(nr, nc)] == "|":
                        trees += 1
                    elif g[(nr, nc)] == "#":
                        lumber += 1
            if g[(r, c)] == ".":
                new_g[(r, c)] = "|" if trees >= 3 else "."
            elif g[(r, c)] == "|":
                new_g[(r, c)] = "#" if lumber >= 3 else "|"
            elif g[(r, c)] == "#":
                new_g[(r, c)] = "#" if lumber >= 1 and trees >= 1 else "."
            else:
                assert False
    return new_g


def vl(g):
    trees = sum(x == "|" for x in g.values())
    lumber = sum(x == "#" for x in g.values())
    return trees * lumber


seen = dict()
for i in range(1000000000):
    hashed = tuple(sorted(grid.items()))
    if hashed in seen:
        cycle_len = i - seen[hashed]
        vls = {0: vl(grid)}
        for j in range(1, cycle_len):
            grid = step(grid)
            vls[j] = vl(grid)
        print("Part 2:", vls[(1000000000 - i) % cycle_len])
        break
    seen[hashed] = i
    grid = step(grid)
    if i == 9:
        print("Part 1:", vl(grid))


