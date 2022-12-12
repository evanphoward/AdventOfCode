from collections import deque


def bfs(maze, start):
    global goal, height, width
    bfs_q = deque()
    explored = set()
    bfs_q.append((0, start))
    explored.add(start)
    while bfs_q:
        steps, pos = bfs_q.popleft()
        if pos == goal:
            return steps
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos[0] < 0 or new_pos[0] >= height or new_pos[1] < 0 or new_pos[1] >= width or maze[new_pos] - maze[pos] > 1:
                continue
            if new_pos not in explored:
                explored.add(new_pos)
                bfs_q.append((steps + 1, new_pos))
    return -1


goal, starting_pos = (), ()
A = []
grid = dict()
inp = open("input").read().strip().split("\n")
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        if cell == "S":
            starting_pos = (r, c)
            cell = "a"
        elif cell == "E":
            goal = (r, c)
            cell = "z"
        if cell == "a":
            A.append((r, c))
        grid[r, c] = ord(cell) - ord('a')
height = len(inp)
width = len(inp[0])


print("Part 1:", bfs(grid, starting_pos))
print("Part 2:", min([bfs(grid, a) for a in A if bfs(grid, a) != -1]))
