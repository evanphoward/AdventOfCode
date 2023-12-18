pts = [tuple(map(int, line.split(','))) for line in open("input").read().split("\n")]
constellations = list(range(len(pts)))

dists = dict()
for i in range(len(pts)):
    for j in range(len(pts)):
        if i == j:
            continue
        x, y, z, w = pts[i]
        x2, y2, z2, w2 = pts[j]
        dists[(i, j)] = abs(x - x2) + abs(y - y2) + abs(z - z2) + abs(w - w2)

for i in range(len(pts)):
    if constellations[i] < i:
        continue
    q = [i]
    explored = {i}
    while q:
        j = q.pop()
        constellations[j] = i
        for k in range(len(pts)):
            if j == k:
                continue
            if dists[(j, k)] <= 3 and k not in explored:
                explored.add(k)
                q.append(k)

print(len(set(constellations)))