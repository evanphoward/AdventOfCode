import math


def overlap(cube1, cube2):
    if any(cube1[dim][0] > cube2[dim][1] or cube1[dim][1] < cube2[dim][0] for dim in range(3)):
        return False
    return tuple((max(cube2[dim][0], cube1[dim][0]), min(cube2[dim][1], cube1[dim][1])) for dim in range(3))


def split_cube(cube1, cube2):
    over = overlap(cube1, cube2)
    if not over:
        return [cube1]
    new_cuboids = [(cube1[0], cube1[1], (cube1[2][0], over[2][0] - 1)),
                   (cube1[0], cube1[1], (over[2][1] + 1, cube1[2][1])),
                   ((cube1[0][0], over[0][0] - 1), cube1[1], over[2]),
                   ((over[0][1] + 1, cube1[0][1]), cube1[1], over[2]),
                   (over[0], (cube1[1][0], over[1][0] - 1), over[2]), (over[0], (over[1][1] + 1, cube1[1][1]), over[2])]
    return [(x, y, z) for x, y, z in new_cuboids if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]]


instructions = []
for line in open("input").read().split("\n"):
    instruc, coords = line.split()
    coords = tuple(tuple(map(int, l[2:].split(".."))) for l in coords.split(","))
    instructions.append((instruc, coords))

cubes = []
for instruc, coords in instructions:
    cubes = [item for sublist in [split_cube(cube, coords) for cube in cubes] for item in sublist]
    if instruc == "on":
        cubes.append(coords)

print("Part 1:", sum(math.prod(max(max(-50, c[1]) - min(50, c[0]) + 1, 0) for c in cube) for cube in cubes if all(c[0] <= 50 and c[1] >= -50 for c in cube)))
print("Part 2:", sum(math.prod(c[1] - c[0] + 1 for c in cube) for cube in cubes))