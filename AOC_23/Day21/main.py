import functools
import numpy as np

STARTING_POS = (-1, -1)
inp = open("input").read().split("\n")
grid = dict()
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        if cell == "S":
            grid[r, c] = "."
            STARTING_POS = (r, c)
        else:
            grid[r, c] = cell
nr = len(inp)
nc = len(inp[0])

@functools.lru_cache(maxsize=None)
def neighbors(pos):
    r, c = pos
    n_set = set()
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        tr = r + dr
        tc = c + dc
        if grid[(tr % nr, tc % nc)] == "#":
            continue
        n_set.add((tr, tc))
    return n_set


spots = {STARTING_POS}
num_nodes = []
goal = 26501365
offset = goal % nr
steps = 0
while len(num_nodes) < 3:
    if steps == 64:
        print("Part 1:", len(spots))
    if steps % nr == offset:
        num_nodes.append(len(spots))
    spots = {new_pos for pos in spots for new_pos in neighbors(pos)}
    steps += 1

coeff = np.polyfit(list(range(3)), num_nodes, 2)
index = (goal - offset) / nr
print("Part 2:", int(round(index * index * coeff[0]) + (index * coeff[1]) + coeff[2]))
