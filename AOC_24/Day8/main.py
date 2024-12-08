from MiscFiles.library import *

ans = 0

grid, nr, nc = get_grid(get_input(2024, 8))

ants = dict()
for r in range(nr):
    for c in range(nc):
        if grid[(r, c)] != '.':
            ants[(r, c)] = grid[(r, c)]


antinodes_1, antinodes_2 = set(), set()
for r in range(nr):
    for c in range(nc):
        for i, (ar1, ac1) in enumerate(list(ants.keys())):
            for j, (ar2, ac2) in enumerate(list(ants.keys())):
                if i == j or grid[(ar1, ac1)] != grid[(ar2, ac2)]:
                    continue
                try:
                    if (ar1 - r) / (ar2 - r) == (ac1 - c) / (ac2 - c):
                        if (ar1 - r) == 2 * (ar2 - r):
                            antinodes_1.add((r, c))
                        antinodes_2.add((r, c))
                except ZeroDivisionError:
                    try:
                        if  (ar2 - r) / (ar1 - r) ==  (ac2 - c) / (ac1 - c):
                            antinodes_2.add((r, c))
                    except ZeroDivisionError:
                        continue


print("Part 1:", len(antinodes_1))
print("Part 2:", len(antinodes_2))
