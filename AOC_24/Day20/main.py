from MiscFiles.library import *

grid, nr, nc = get_grid(get_input(2024, 20))
for r in range(nr):
    for c in range(nc):
        if grid[(r, c)] == 'S':
            STARTING_POS = (r, c)
            grid[(r, c)] = '.'
        if grid[(r, c)] == 'E':
            GOAL = (r, c)
            grid[(r, c)] = '.'


def bfs():
    bfs_q = deque()
    explored = set()
    bfs_q.append(([STARTING_POS], STARTING_POS))
    explored.add(STARTING_POS)
    while bfs_q:
        steps, pos = bfs_q.popleft()
        if pos == GOAL:
            return steps
        for dr, dc in DIRS:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if grid[new_pos] == "#":
                continue
            if new_pos not in explored:
                explored.add(new_pos)
                bfs_q.append((steps + [new_pos], new_pos))


p1, p2 = 0, 0
path = bfs()
for i in range(len(path)):
    for j in range(i + 1, len(path)):
        r1, c1 = path[i]
        r2, c2 = path[j]
        cheat_distance = abs(r1 - r2) + abs(c1 - c2)
        time_saved = j - i - (abs(r1 - r2) + abs(c1 - c2))
        if time_saved >= 100:
            p1 += cheat_distance == 2
            p2 += cheat_distance <= 20

print("Part 1:", p1)
print("Part 2:", p2)
