from collections import deque, defaultdict
neighbors = defaultdict(set)
for line in open("input").readlines():
    line = line.strip().split("-")
    neighbors[line[0]].add(line[1])
    neighbors[line[1]].add(line[0])


def num_paths(p1):
    bfs_q = deque()
    paths = 0
    bfs_q.append((0, "start", ["start"], False))
    while bfs_q:
        steps, pos, path, has_two = bfs_q.popleft()
        if pos == "end":
            paths += 1
            continue
        for node in neighbors[pos]:
            if node == "start":
                continue
            if node.islower() and node in path:
                if has_two or p1:
                    continue
                else:
                    bfs_q.append((steps + 1, node, path + [node], True))
            else:
                bfs_q.append((steps + 1, node, path + [node], has_two))
    return paths


print("Part 1:", num_paths(True))
print("Part 2:", num_paths(False))
