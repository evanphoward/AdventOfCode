# Basic template for solving days that need BFS
# Examples: 2016 Days 11, 13, 17, 24. 2021 Day 12, 2022 Day 12
# Probably some more I can't find. Man, 2016 loved path-finding puzzles
from collections import deque
from MiscFiles.library import *
GOAL = (2, 1)
STARTING_POS = (1, 1)

maze, height, width = get_grid(get_input(0, 0))

bfs_q = deque()
explored = set()
bfs_q.append((0, STARTING_POS))
explored.add(STARTING_POS)
while bfs_q:
    steps, pos = bfs_q.popleft()
    if pos == GOAL:
        print(steps)
        break
    for dr, dc in DIRS:
        new_pos = (pos[0] + dr, pos[1] + dc)
        if maze[new_pos] == "#":
            continue
        if new_pos not in explored:
            explored.add(new_pos)
            bfs_q.append((steps + 1, new_pos))




