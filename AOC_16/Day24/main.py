from collections import deque


def parse_maze():
    maze = dict()
    keys = set()
    starting_pos = (-1, -1)
    for r, row in enumerate(open("input").readlines()):
        for c, cell in enumerate(row.strip()):
            if cell not in ['#', '.']:
                if cell == '0':
                    starting_pos = (r, c)
                    maze[r, c] = '.'
                    continue
                keys.add(cell)
            maze[r, c] = cell
    return starting_pos, maze, keys


def bfs(setup, p1):
    starting_pos, maze, keys = setup
    bfs_q = deque()
    bfs_q.append((0, starting_pos, set()))
    explored = set()
    explored.add((starting_pos, frozenset(set())))
    while bfs_q:
        steps, pos, curr_keys = bfs_q.popleft()
        r, c = pos
        if curr_keys == keys and (p1 or pos == starting_pos):
            return steps
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (r + dr, c + dc)
            if maze[new_pos] == '#':
                continue
            new_keys = curr_keys.copy()
            if maze[new_pos] != '.' and maze[new_pos] not in curr_keys:
                new_keys.add(maze[new_pos])
            if (new_pos, frozenset(new_keys)) not in explored:
                explored.add((new_pos, frozenset(new_keys)))
                bfs_q.append((steps + 1, new_pos, new_keys))


maze_setup = parse_maze()
print("Part 1:", bfs(maze_setup, True))
print("Part 2:", bfs(maze_setup, False))
