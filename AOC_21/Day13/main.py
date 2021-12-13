dots, folds = open("input").read().split("\n\n")
grid = {tuple(map(int, dot.split(","))) for dot in dots.split("\n")}
folds = [fold.split()[2].split("=") for fold in folds.split("\n")]


for i, fold in enumerate(folds):
    coord = int(fold[1])
    is_y = fold[0] == "y"
    for dot in list(grid):
        if dot[is_y] > coord:
            grid.remove(dot)
            if is_y:
                grid.add((dot[0], coord - (dot[1] - coord)))
            else:
                grid.add((coord - (dot[0] - coord), dot[1]))
    if i == 0:
        print("Part 1:", len(grid))


print("Part 2:")
for y in range(max(g[1] for g in grid) + 1):
    for x in range(max(g[0] for g in grid) + 1):
        if (x, y) in grid:
            print("#", end="")
        else:
            print(".", end="")
    print()
