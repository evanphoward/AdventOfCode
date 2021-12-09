from collections import deque
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
inp = open("input").readlines()
grid = dict()
for r, row in enumerate(inp):
    for c, cell in enumerate(row.strip()):
        grid[r, c] = int(cell)

sizes = []
risk = 0
for r in range(len(inp)):
    for c in range(len(inp[0].strip())):
        if any(grid[r, c] >= adj for adj in [grid[r + dr, c + dc] for dr, dc in DIRS if (r + dr, c + dc) in grid]):
            continue
        risk += 1 + grid[r, c]
        explored = {(r, c)}
        q = deque([(r, c)])
        while q:
            basin_r, basin_c = q.popleft()
            for dr, dc in DIRS:
                new_pos = (basin_r + dr, basin_c + dc)
                if new_pos not in grid or grid[new_pos] < grid[basin_r, basin_c] or grid[new_pos] == 9:
                    continue
                if new_pos not in explored:
                    explored.add(new_pos)
                    q.append(new_pos)
        sizes.append(len(explored))

sizes = sorted(sizes)
print("Part 1:", risk)
print("Part 2:", sizes[-1] * sizes[-2] * sizes[-3])
