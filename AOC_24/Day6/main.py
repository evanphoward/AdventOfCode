from MiscFiles.library import *


grid, nr, nc = get_grid(get_input(2024, 6))
STARTING_POS = (0, 0)
for r in range(nr):
    for c in range(nc):
        if grid[(r, c)] == '^':
            STARTING_POS = (r, c)
            grid[r, c] = '.'


def simulate(grid, p1):
    gr, gc = STARTING_POS
    heading = 0
    seen = set()
    while (gr, gc) in grid:
        if (gr, gc, heading) in seen:
            return True
        seen.add((gr, gc, heading))
        dr, dc = DIRS[heading]
        if (gr + dr, gc + dc) not in grid:
            return set((r, c) for (r, c, _) in seen) if p1 else False
        if grid[(gr + dr, gc + dc)] == '.':
            gr += dr
            gc += dc
        else:
            heading = (heading + 1) % 4


visited_cells = simulate(grid, True)
print("Part 1:", len(visited_cells))

ans = 0
for (r, c) in visited_cells:
    if (r, c) == STARTING_POS:
        continue
    grid_c = grid.copy()
    grid_c[(r, c)] = '#'
    ans += simulate(grid_c, False)
print("Part 2:", ans)
