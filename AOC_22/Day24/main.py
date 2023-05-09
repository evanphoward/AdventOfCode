from collections import deque
grid = dict()
inp = open("input").read().strip().split("\n")
blizzards = [set(), set(), set(), set()]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        if cell == ">":
            blizzards[0].add((r, c))
            cell = "."
        elif cell == "v":
            blizzards[1].add((r, c))
            cell = "."
        elif cell == "<":
            blizzards[2].add((r, c))
            cell = "."
        elif cell == "^":
            blizzards[3].add((r, c))
            cell = "."
        grid[r, c] = cell
height = len(inp)
width = len(inp[0])

b_list = [blizzards]


def step_b(init_b):
    global grid
    new_b = [set(), set(), set(), set()]
    for r, c in init_b[0]:
        c += 1
        if grid[(r, c)] == "#":
            c = 1
        new_b[0].add((r, c))
    for r, c in init_b[1]:
        r += 1
        if grid[(r, c)] == "#":
            r = 1
        new_b[1].add((r, c))
    for r, c in init_b[2]:
        c -= 1
        if grid[(r, c)] == "#":
            c = width - 2
        new_b[2].add((r, c))
    for r, c in init_b[3]:
        r -= 1
        if grid[(r, c)] == "#":
            r = height - 2
        new_b[3].add((r, c))
    return new_b


def get_b(i):
    global b_list
    if i < len(b_list):
        return b_list[i]
    for _ in range(i - len(b_list) + 1):
        b_list.append(step_b(b_list[-1]))
    return b_list[-1]


def bfs(starting_r, starting_c, starting_min, goal):
    bfs_q = deque([(starting_min, (starting_r, starting_c))])
    explored = {(starting_r, starting_c, starting_min)}
    while bfs_q:
        steps, pos = bfs_q.popleft()
        if pos == goal:
            return steps
        for dr, dc in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc, steps + 1)
            if (0 <= new_pos[0] < height) and grid[(new_pos[0], new_pos[1])] == "." and \
                    all((new_pos[0], new_pos[1]) not in get_b(new_pos[2])[i] for i in range(4)) and \
                    new_pos not in explored:
                explored.add(new_pos)
                bfs_q.append((steps + 1, (new_pos[0], new_pos[1])))


there_min = bfs(0, 1, 0, (height - 1, width - 2))
print("Part 1:", there_min)
back_min = bfs(height - 1, width - 2, there_min, (0, 1))
print("Part 2:", bfs(0, 1, back_min, (height - 1, width - 2)))
