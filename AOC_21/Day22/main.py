inp = open("input").read().split("\n")
instructions = []
for line in inp:
    instruc, coords = line.split()
    coords = tuple(tuple(map(int, l[2:].split(".."))) for l in coords.split(","))
    instructions.append((instruc, coords))

cubes = set()
for instruc, coords in instructions:
    # print(len(cubes), instruc, coords)
    x_bounds, y_bounds, z_bounds = coords
    if x_bounds[0] > 50:
        continue
    if x_bounds[1] < -50:
        continue
    if y_bounds[0] > 50:
        continue
    if y_bounds[1] < -50:
        continue
    if z_bounds[0] > 50:
        continue
    if z_bounds[1] < -50:
        continue
    if instruc == "on":
        for x in range(max(x_bounds[0], -50), min(x_bounds[1] + 1, 51)):
            for y in range(max(y_bounds[0], -50), min(y_bounds[1] + 1, 51)):
                for z in range(max(z_bounds[0], -50), min(z_bounds[1] + 1, 51)):
                    cubes.add((x, y, z))
    else:
        remove = set()
        for cube in cubes:
            if x_bounds[0] <= cube[0] <= x_bounds[1]:
                if y_bounds[0] <= cube[1] <= y_bounds[1]:
                    if z_bounds[0] <= cube[2] <= z_bounds[1]:
                        remove.add(cube)
        cubes = cubes.difference(remove)
print(len(cubes))


def overlap(cube1, cube2):
    for dim in range(3):
        if cube1[dim][0] > cube2[dim][1] or cube1[dim][1] < cube2[dim][0]:
            return None
    return tuple((max(cube2[dim][0],cube1[dim][0]), min(cube2[dim][1],cube1[dim][1])) for dim in range(3))


def split_cube(cube1, cube2):
    over = overlap(cube1, cube2)
    if not over:
        return [cube1]
    new_cuboids = []
    new_cuboids.append((cube1[0], cube1[1], (cube1[2][0], over[2][0] - 1)))
    new_cuboids.append((cube1[0], cube1[1], (over[2][1] + 1, cube1[2][1])))
    new_cuboids.append(((cube1[0][0], over[0][0] - 1), cube1[1], over[2]))
    new_cuboids.append(((over[0][1] + 1, cube1[0][1]), cube1[1], over[2]))
    new_cuboids.append((over[0], (cube1[1][0], over[1][0] - 1), over[2]))
    new_cuboids.append((over[0], (over[1][1] + 1, cube1[1][1]), over[2]))
    return [(x, y, z) for x, y, z in new_cuboids if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]]


cubes = []
for instruc, coords in instructions:
    cubes = [item for sublist in [split_cube(cube, coords) for cube in cubes] for item in sublist]
    if instruc == "on":
        cubes.append(coords)

total = 0
for cube in cubes:
    total += max(max(-50, cube[0][1]) - min(50, cube[0][0]), 0) * max(max(-50, cube[1][1]) - min(50, cube[1][0]), 0) * max(max(-50, cube[2][1]) - min(50, cube[2][0]), 0)
print(total)
print(sum((cube[0][1] - cube[0][0] + 1) * (cube[1][1] - cube[1][0] + 1) * (cube[2][1] - cube[2][0] + 1) for cube in cubes))