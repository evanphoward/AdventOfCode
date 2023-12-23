from collections import deque, defaultdict

grid = dict()
inp = open("input").read().split("\n")
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[r, c] = cell
nr = len(inp)
nc = len(inp[0])

splits = set()
for r in range(1, nr - 1):
    for c in range(1, nc - 1):
        if grid[r, c] == "." and sum(grid[r + dr, c + dc] == "#" for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]) < 2:
            splits.add((r, c))
splits.add((0, 1))
splits.add((nr - 1, nc - 2))

STARTING_POS = (0, 1)
bfs_q = deque()
bfs_q.append((0, STARTING_POS, STARTING_POS))
explored = set()
directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
edges = defaultdict(set)
reverse_edges = defaultdict(set)
while bfs_q:
    steps, pos, prev_split = bfs_q.pop()
    if pos != prev_split and pos in splits:
        bfs_q.append((0, pos, pos))
        edges[prev_split].add((pos, steps))
        reverse_edges[pos].add((prev_split, steps))
    else:
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos not in grid or grid[new_pos] == "#":
                continue
            if grid[new_pos] in directions and (dr, dc) != directions[grid[new_pos]]:
                continue
            if new_pos in splits or new_pos not in explored:
                explored.add(new_pos)
                bfs_q.append((steps + 1, new_pos, prev_split))


def find_max(use_reverse):
    q = [(0, (0, 1), {(0, 1)})]
    max_steps = 0
    while q:
        steps, pos, path = q.pop()
        if pos == (nr - 1, nc - 2):
            max_steps = max(steps, max_steps)
        else:
            neighbors = edges[pos]
            if use_reverse:
                neighbors = neighbors.union(reverse_edges[pos])
            for neighbor, weight in neighbors:
                if neighbor in path:
                    continue
                q.append((steps + weight, neighbor, path.union({neighbor})))
    return max_steps


print("Part 1:", find_max(False))
print("Part 2:", find_max(True))

