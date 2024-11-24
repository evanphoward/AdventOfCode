# Basic template for solving days that need BFS
# Examples: 2016 Days 11, 13, 17, 24. 2021 Day 12, 2022 Day 12
# Probably some more I can't find. Man, 2016 loved path-finding puzzles
from MiscFiles.library import *
GOAL = (2, 1)
STARTING_POS = (1, 1)

grid = dict()
inp = get_input(0, 0).split('\n')
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[r, c] = cell
nr = len(inp)
nc = len(inp[0])

def bfs(maze, goal):
    bfs_q = deque()
    explored = set()
    bfs_q.append((0, STARTING_POS))
    explored.add(STARTING_POS)
    while bfs_q:
        steps, pos = bfs_q.popleft()
        if pos == goal:
            print(steps)
            break
        for dr, dc in DIRS:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if maze[new_pos] == "#":
                continue
            if new_pos not in explored:
                explored.add(new_pos)
                bfs_q.append((steps + 1, new_pos))

def dijkstra(maze, goal):
    heap = [(0, STARTING_POS)]
    distances = {pos: -1 for pos in maze}
    distances[STARTING_POS] = 0
    visited = set()
    while heap:
        distance, pos = heapq.heappop(heap)
        if pos in visited:
            continue
        if pos == goal:
            return distance
        visited.add(pos)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos not in maze or new_pos in visited:
                continue
            if distances[new_pos] == -1 or distance + maze[new_pos] < distances[new_pos]:
                distances[new_pos] = distance + maze[new_pos]
            heapq.heappush(heap, (distances[new_pos], new_pos))
    return -1



