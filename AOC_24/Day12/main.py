from MiscFiles.library import *

ans = 0

g = nx.Graph()
grid, nr, nc = get_grid(get_input(2024, 12))

for r in range(nr):
    for c in range(nc):
        g.add_node((r, c))
        for dr, dc in DIRS:
            new_pos = r + dr, c + dc
            if new_pos not in grid:
                continue
            if grid[new_pos] == grid[(r, c)]:
                g.add_edge((r, c), new_pos)


regions = nx.connected_components(g)
prices_p1 = []
prices_p2 = []
for region in regions:
    sides = 0

    # Get all top sides
    for r in range(nr):
        c = 0
        while c < nc:
            if (r, c) in region and ((r - 1, c) not in grid or (r - 1, c) not in region):
                sides += 1
                while (r, c) in region and ((r - 1, c) not in grid or (r - 1, c) not in region):
                    c += 1
            else:
                c += 1

    # Get all bottom sides
    for r in range(nr - 1, -1, -1):
        c = 0
        while c < nc:
            if (r, c) in region and ((r + 1, c) not in grid or (r + 1, c) not in region):
                sides += 1
                while (r, c) in region and ((r + 1, c) not in grid or (r + 1, c) not in region):
                    c += 1
            else:
                c += 1

    # Get all left sides
    for c in range(nc):
        r = 0
        while r < nr:
            if (r, c) in region and ((r, c - 1) not in grid or (r, c - 1) not in region):
                sides += 1
                while (r, c) in region and ((r, c - 1) not in grid or (r, c - 1) not in region):
                    r += 1
            else:
                r += 1

    # Get all right sides
    for c in range(nc - 1, -1, -1):
        r = 0
        while r < nr:
            if (r, c) in region and ((r, c + 1) not in grid or (r, c + 1) not in region):
                sides += 1
                while (r, c) in region and ((r, c + 1) not in grid or (r, c + 1) not in region):
                    r += 1
            else:
                r += 1


    area = len(region)
    perimeter = sum([(r + dr, c + dc) not in region for dr, dc in DIRS for r, c in region])
    prices_p1.append(area * perimeter)
    prices_p2.append(area * sides)

print("Part 1:", sum(prices_p1))
print("Part 2:", sum(prices_p2))
