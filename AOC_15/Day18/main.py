WIDTH = len(open("input").readline().strip())
CORNERS = [(0, 0), (0, WIDTH - 1), (WIDTH - 1, 0), (WIDTH - 1, WIDTH - 1)]


def parse_grid(p2):
    grid = dict()
    for r, row in enumerate(open("input").readlines()):
        for c, cell in enumerate(row):
            grid[r, c] = cell == "#" or (p2 and (r, c) in CORNERS)
    return grid


def step(grid, p2):
    new_grid = dict()
    for r in range(WIDTH):
        for c in range(WIDTH):
            neighbors = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == dc == 0 or (r + dr, c + dc) not in grid:
                        continue
                    neighbors += grid[r + dr, c + dc]
            new_grid[r, c] = (p2 and (r, c) in CORNERS) or neighbors == 3 or (neighbors == 2 and grid[r, c])
    return new_grid


for part in [False, True]:
    curr_grid = parse_grid(part)
    for _ in range(100):
        curr_grid = step(curr_grid, part)
    print("Part 2:" if part else "Part 1:", sum(curr_grid.values()))
