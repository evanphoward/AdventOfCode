import itertools
dirs_1 = set(itertools.permutations([1, 1, 1, 0, 0, 0, -1, -1, -1], 3)).difference({(0, 0, 0)})
dirs_2 = set(itertools.permutations([1, 1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1], 4)).difference({(0, 0, 0, 0)})
cubes_1 = dict()
cubes_2 = dict()
x = y = 0
for line in open("input").readlines():
    for ch in line.strip():
        cubes_1[(x, y, 0)] = ch == "#"
        cubes_2[(x, y, 0, 0)] = ch == "#"
        x += 1
    x = 0
    y += 1
for _ in range(6):
    new_cubes_1 = cubes_1.copy()
    new_cubes_2 = cubes_2.copy()
    combined = set(cubes_1.keys()).union(set(cubes_2.keys()))
    for x in range(min(pos[0] for pos in combined) - 1, max(pos[0] for pos in combined) + 2):
        for y in range(min(pos[1] for pos in combined) - 1, max(pos[1] for pos in combined) + 2):
            for z in range(min(pos[2] for pos in combined) - 1, max(pos[2] for pos in combined) + 2):
                neighbors_1 = sum((x + dx, y + dy, z + dz) in cubes_1.keys() and cubes_1[(x + dx, y + dy, z + dz)] for dx, dy, dz in dirs_1)
                if (x, y, z) in cubes_1.keys() and cubes_1[(x, y, z)]:
                    new_cubes_1[(x, y, z)] = 2 <= neighbors_1 <= 3
                else:
                    new_cubes_1[(x, y, z)] = neighbors_1 == 3
                for w in range(min(pos[3] for pos in cubes_2.keys()) - 1, max(pos[3] for pos in cubes_2.keys()) + 2):
                    neighbors_2 = sum((x + dx, y + dy, z + dz, w + dw) in cubes_2.keys() and cubes_2[(x + dx, y + dy, z + dz, w + dw)] for dx, dy, dz, dw in dirs_2)
                    if (x, y, z, w) in cubes_2.keys() and cubes_2[(x, y, z, w)]:
                        new_cubes_2[(x, y, z, w)] = 2 <= neighbors_2 <= 3
                    else:
                        new_cubes_2[(x, y, z, w)] = neighbors_2 == 3
    cubes_1 = new_cubes_1.copy()
    cubes_2 = new_cubes_2.copy()
print("Part 1:", sum(cubes_1.values()))
print("Part 2:", sum(cubes_2.values()))
