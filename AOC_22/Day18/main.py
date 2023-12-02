from collections import deque


def outside(tx, ty, tz):
    bfs_q = deque()
    explored = set()
    bfs_q.append((tx, ty, tz))
    while bfs_q:
        pos = bfs_q.popleft()
        if pos in cubes or pos in explored:
            continue
        explored.add(pos)
        if not (0 <= pos[0] <= max_x) or not (0 <= pos[1] <= max_y) or not (0 <= pos[2] <= max_z):
            return True
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            new_pos = (pos[0] + dx, pos[1] + dy, pos[2] + dz)
            bfs_q.append(new_pos)
    return False


cubes = set(tuple(map(int, cube.split(","))) for cube in open("input").read().strip().split("\n"))
max_x = max(x[0] for x in cubes) + 1
max_y = max(x[1] for x in cubes) + 1
max_z = max(x[2] for x in cubes) + 1
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

p1 = 0
p2 = 0
for x, y, z in cubes:
    p1 += sum((x + dx, y + dy, z + dz) not in cubes for (dx, dy, dz) in dirs)
    p2 += sum(outside(x + dx, y + dy, z + dz) for (dx, dy, dz) in dirs)
print("Part 1:", p1)
print("Part 2:", p2)
