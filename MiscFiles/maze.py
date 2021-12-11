# Basic template for solving days that need BFS
# Examples: 2016 Days 11, 13, 17, 24
# Probably some more I can't find. Man, 2016 loved path-finding puzzles
from collections import deque
GOAL = (2, 1)
STARTING_POS = (1, 1)


def parse_grid():
    grid = dict()
    inp = open("input").readlines()
    for r, row in enumerate(inp):
        for c, cell in enumerate(row):
            grid[r, c] = cell
    return grid, len(inp), len(inp[0])


def bfs(maze, p1):
    bfs_q = deque()
    explored = set()
    bfs_q.append((0, STARTING_POS))
    explored.add(STARTING_POS)
    while bfs_q:
        steps, pos = bfs_q.popleft()
        if pos == GOAL:
            return steps
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if maze[new_pos] == "#":
                continue
            if new_pos not in explored:
                explored.add(new_pos)
                bfs_q.append((steps + 1, new_pos))
    return -1


maze_setup, height, width = parse_grid()
print(bfs(maze_setup, True))
print(bfs(maze_setup, False))

