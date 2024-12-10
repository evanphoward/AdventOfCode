from MiscFiles.library import *

ans = 0

grid, nr, nc = get_grid(get_input(2024, 10))

zeroes = set()
nines = set()
g = nx.DiGraph()
for r in range(nr):
    for c in range(nc):
        if grid[(r, c)] == '.':
            grid[(r, c)] = '9'
        grid[(r, c)] = int(grid[(r, c)])
        if grid[(r, c)] == 0:
            zeroes.add((r, c))
        if grid[(r, c)] == 9:
            nines.add((r, c))

for r in range(nr):
    for c in range(nc):
        for dr, dc in DIRS:
            new_pos = r + dr, c + dc
            if new_pos not in grid:
                continue
            if grid[new_pos] - grid[(r, c)] == 1:
                g.add_edge(u_of_edge=(r, c), v_of_edge=new_pos)

p1, p2 = 0, 0
for zero in zeroes:
    for nine in nines:
        num_paths = len(list(nx.all_simple_paths(g, zero, nine)))
        if num_paths > 0:
            p1 += 1
        p2 += num_paths

print("Part 1:", p1)
print("Part 2:", p2)