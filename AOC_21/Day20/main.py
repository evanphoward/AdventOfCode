def step(grid, empty=False):
    new_grid = dict()
    min_r, max_r = min(cell[0] for cell in grid) - 1, max(cell[0] for cell in grid) + 2
    min_c, max_c = min(cell[1] for cell in grid) - 1, max(cell[1] for cell in grid) + 2
    for r in range(min_r, max_r):
        for c in range(min_c, max_c):
            bin_string = ''.join(str(int(grid[r + dr, c + dc]))
                                 if (r + dr, c + dc) in grid else
                                 str(int(empty))
                                 for dr in range(-1, 2) for dc in range(-1, 2))
            new_grid[r, c] = rules[int(bin_string, 2)] == "#"
    return new_grid


rules, image_string = open("input").read().split("\n\n")
image = {(r, c): cell == "#" for r, row in enumerate(image_string.split("\n")) for c, cell in enumerate(row)}
for i in range(50):
    image = step(image, i % 2 == 1)
    if i == 2:
        print("Part 1:", sum(image.values()))
print("Part 2:", sum(image.values()))
