def step(grid):
    new_grid = dict({x: grid[x] + 1 for x in grid})
    old_flashes = -1
    flashed = set()
    while len(flashed) > old_flashes:
        old_flashes = len(flashed)
        for pos in new_grid:
            if pos not in flashed and new_grid[pos] > 9:
                flashed.add(pos)
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        new_pos = (pos[0] + dr, pos[1] + dc)
                        if new_pos not in new_grid or dr == dc == 0:
                            continue
                        new_grid[new_pos] += 1
    for pos in flashed:
        new_grid[pos] = 0
    return len(flashed), new_grid


states = [(0, dict({(r, c): int(cell) for r, row in enumerate(open("input").read().split("\n")) for c, cell in enumerate(row)}))]
while states[-1][0] < 100:
    states.append(step(states[-1][1]))

print("Part 1:", sum(x[0] for x in states[0:101]))
print("Part 2:", len(states) - 1)
