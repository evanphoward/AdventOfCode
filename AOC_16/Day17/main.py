from collections import deque
import hashlib
PASS = open("input").readline().strip()
DIRS = {0: ('U', -1, 0), 1: ('D', 1, 0), 2: ('L', 0, -1), 3: ('R', 0, 1),}

explored = set()
bfs_q = deque()
explored.add(("", 0, 0))
bfs_q.append(("", 0, 0))
paths = []

while bfs_q:
    path, r, c = bfs_q.popleft()
    if r == 3 and c == 3:
        paths.append(path)
        continue

    hashed = hashlib.md5((PASS + path).encode()).hexdigest()
    opened = [hashed[i] in ['b', 'c', 'd', 'e', 'f'] for i in range(4)]

    for i in range(4):
        d, dr, dc = DIRS[i]
        if 0 <= (r + dr) <= 3 and 0 <= (c + dc) <= 3 and opened[i]:
            new_node = (path + d, r + dr, c + dc)
            if new_node not in explored:
                explored.add(new_node)
                bfs_q.append(new_node)

print("Part 1:", paths[0])
print("Part 2:", len(paths[-1]))

