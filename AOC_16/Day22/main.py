from collections import deque

nodes = {}
largest_x = 0
largest_y = 0
smallest_size = 500
for line in open("input").readlines():
    line = line.strip().split()
    pos = line[0].split("-")
    x, y = int(pos[1][1:]), int(pos[2][1:])
    largest_x = max(x, largest_x)
    largest_y = max(y, largest_y)
    smallest_size = min(int(line[1][:-1]), smallest_size)
    nodes[x, y] = (int(line[2][:-1]), int(line[3][:-1]))

viable = 0
puzzle = dict()
empty = -1
for a in nodes:
    puzzle[a] = '.' if nodes[a][0] <= smallest_size else '#'
    if nodes[a][0] == 0:
        empty = a
    for b in nodes:
        if a == b:
            continue
        used1, _ = nodes[a]
        _, avail2 = nodes[b]
        viable += (used1 > 0) and (used1 <= avail2)
print("Part 1:", viable)

goal = (largest_x, 0)
bfs_q = deque()
bfs_q.append((0, empty, goal))
explored = set()
explored.add((empty, goal))
while bfs_q:
    steps, empty, goal = bfs_q.popleft()
    if goal == (0, 0):
        print("Part 2:", steps)
        exit()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_empty = (empty[0] + dx, empty[1] + dy)
        if 0 <= new_empty[0] <= largest_x and 0 <= new_empty[1] <= largest_y and puzzle[new_empty] == '.':
            new_goal = goal
            if new_empty == goal:
                new_goal = empty
            if (new_empty, new_goal) not in explored:
                explored.add((new_empty, new_goal))
                bfs_q.append((steps + 1, new_empty, new_goal))




