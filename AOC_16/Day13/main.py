from collections import deque
FAV_NUM = int(open("input").read())


def is_wall(pos):
    x, y = pos
    num = (x * x + 3 * x + 2 * x * y + y + y * y) + FAV_NUM
    return sum(bit == "1" for bit in bin(num)) % 2 == 1


def bfs(root, goal):
    explored = set()
    explored.add(root)
    bfs_q = deque()
    bfs_q.append((0, root))
    total = 0
    while bfs_q:
        steps, pos = bfs_q.popleft()
        if steps <= 50:
            total += 1
        if pos == goal:
            return steps, total
        x, y = pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = ((x + dx), (y + dy))
            if x + dx < 0 or y + dy < 0 or new_pos in explored or is_wall(new_pos):
                continue
            explored.add(new_pos)
            bfs_q.append((steps + 1, new_pos))
    return -1, -1


steps_to_goal, pos_in_fifty = bfs((1, 1), (31, 39))
print("Part 1:", steps_to_goal)
print("Part 2:", pos_in_fifty)
