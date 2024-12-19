from MiscFiles.library import *

nr, nc = 71, 71
grid = dict()
for r in range(nr):
    for c in range(nc):
        grid[(r, c)] = '.'


inp = get_input(2024, 18).split("\n")

for i in range(1024):
    line = inp[i].split(',')
    grid[(int(line[1]), int(line[0]))] = '#'

def bfs():
    STARTING_POS = (0, 0)
    bfs_q = deque()
    explored = set()
    bfs_q.append((0, STARTING_POS))
    explored.add(STARTING_POS)
    while bfs_q:
        steps, pos = bfs_q.popleft()
        if pos == (70, 70):
            return steps
        for dr, dc in DIRS:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos not in grid or grid[new_pos] == '#':
                continue
            if new_pos not in explored:
                explored.add(new_pos)
                bfs_q.append((steps + 1, new_pos))
    return -1

i = 1024
print("Part 1:", bfs())
while bfs() > 0:
    line = inp[i].split(',')
    grid[(int(line[1]), int(line[0]))] = '#'
    i += 1
print("Part 2:", inp[i - 1])
