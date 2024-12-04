from MiscFiles.library import *

grid, nr, nc = get_grid(get_input(2024, 4))
p1, p2 = 0, 0

for r in range(nr):
    for c in range(nc):
        if grid[(r, c)] == 'X':
            for dr, dc in DIRS_WITH_CORNERS:
                word = ''
                for i in range(4):
                    word_pos = (r + (dr * i), c + (dc * i))
                    if word_pos in grid:
                        word += grid[word_pos]
                if word == 'XMAS':
                    p1 += 1
        elif grid[(r, c)] == 'A':
            matches = 0
            for dr, dc in CORNERS:
                if (r + dr, c + dc) in grid and (r + (dr * -1), c + (dc * -1)) in grid:
                    if grid[(r + dr, c + dc)] == 'S':
                        if grid[(r + (dr * -1), c + (dc * -1))] == 'M':
                            matches += 1
            if matches == 2:
                p2 += 1

print("Part 1:", p1)
print("Part 2:", p2)