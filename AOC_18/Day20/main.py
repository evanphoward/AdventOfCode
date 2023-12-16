from collections import defaultdict, deque

edges = defaultdict(set)
directions = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
r, c = 0, 0
paren_pos = []
for symbol in open("input").read().strip()[1:-1]:
    if symbol == "(":
        paren_pos.append((r, c))
    elif symbol == ")":
        r, c = paren_pos.pop()
    elif symbol == "|":
        r, c = paren_pos[-1]
    else:
        dr, dc = directions[symbol]
        edges[(r, c)].add((dr, dc))
        r += dr
        c += dc


bfs_q = deque()
explored = set()
bfs_q.append((0, (0, 0)))
explored.add((0, 0))
max_steps = 0
p2 = 0
while bfs_q:
    steps, pos = bfs_q.popleft()
    if steps >= 1000:
        p2 += 1
    max_steps = max(steps, max_steps)
    for dr, dc in edges[pos]:
        new_pos = (pos[0] + dr, pos[1] + dc)
        if new_pos not in explored:
            explored.add(new_pos)
            bfs_q.append((steps + 1, new_pos))

print("Part 1:", max_steps)
print("Part 2:", p2)
