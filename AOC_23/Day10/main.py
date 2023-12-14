from collections import deque

grid = dict()
starting_pos = (0, 0)
inp = open("input").read().split("\n")
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        if cell == "S":
            grid[r, c] = "|"
            starting_pos = (r, c)
        else:
            grid[r, c] = cell
assert(starting_pos != (0, 0))

bfs_q = deque()
bfs_q.append((0, starting_pos))
explored = dict()
explored[starting_pos] = 0
while bfs_q:
    steps, pos = bfs_q.popleft()
    for i, (dr, dc) in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
        new_pos = (pos[0] + dr, pos[1] + dc)
        if new_pos not in grid:
            continue
        if grid[new_pos] == ".":
            continue
        valid_types = (('L', 'J', '|', 'S'), ("|", "7", "F", 'S'), ("-", "J", "7", 'S'), ("-", "L", "F", 'S'))
        if grid[new_pos] not in valid_types[i] or grid[pos] not in valid_types[i + (1 if i % 2 == 0 else -1)]:
            continue
        if new_pos not in explored:
            explored[new_pos] = steps + 1
            bfs_q.append((steps + 1, new_pos))

print("Part 1:", max(explored.values()))

inside = 0
for r in range(len(inp)):
    parity = 0
    for c in range(len(inp[0])):
        parity += (r, c) in explored and grid[(r, c)] in "|JL"
        inside += (r, c) not in explored and parity % 2 == 1

print("Part 2:", inside)
