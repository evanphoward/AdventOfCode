dirs = {"e": (2, 0), "w": (-2, 0), "se": (1, -1), "sw": (-1, -1), "ne": (1, 1), "nw": (-1, 1)}
tiles = set()

for line in open("input").readlines():
    line = line.strip()
    x = y = 0
    i = 0
    while i < len(line):
        direc = line[i]
        if line[i] in ["n", "s"]:
            direc = direc + line[i + 1]
            i += 1
        dx, dy = dirs[direc]
        x += dx
        y += dy
        i += 1
    tiles.remove((x, y)) if (x, y) in tiles else tiles.add((x, y))

print("Part 1:", len(tiles))

for _ in range(100):
    new_tiles = set()
    for x in range(min(t[0] for t in tiles) - 1, max(t[0] for t in tiles) + 2):
        for y in range(min(t[1] for t in tiles) - 1, max(t[1] for t in tiles) + 2):
            neighbors = sum((x + dx, y + dy) in tiles for dx, dy in dirs.values())
            if ((x, y) in tiles and 0 < neighbors <= 2) or ((x, y) not in tiles and neighbors == 2):
                new_tiles.add((x, y))
    tiles = new_tiles

print("Part 2:", len(tiles))
