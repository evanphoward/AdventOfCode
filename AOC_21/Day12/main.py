from collections import deque, defaultdict
neighbors = defaultdict(set)
for line in open("input").readlines():
    line = line.strip().split("-")
    neighbors[line[0]].add(line[1])
    neighbors[line[1]].add(line[0])


def num_paths(p1):
    bfs_q = deque([("start", ["start"], False)])
    paths = 0
    while bfs_q:
        pos, path, has_two = bfs_q.popleft()
        if pos == "end":
            paths += 1
            continue
        for node in neighbors[pos]:
            if node == "start" or (node.islower() and node in path and (has_two or p1)):
                continue
            bfs_q.append((node, path + [node], True if node.islower() and node in path else has_two))
    return paths


print("Part 1:", num_paths(True))
print("Part 2:", num_paths(False))
