inp = open("input").read().split("\n")

walls = set()
min_y, max_y = 1000, 0
min_x, max_x = 500, 500
for wall in inp:
    if wall[0] == "x":
        wall = wall.split(", y=")
        wall_x = int(wall[0][2:])
        wall_ys = [int(x) for x in wall[1].split("..")]
        min_y = min(min_y, wall_ys[0])
        max_y = max(max_y, wall_ys[1])
        min_x = min(min_x, wall_x)
        max_x = max(max_x, wall_x)
        for y in range(wall_ys[0], wall_ys[1] + 1):
            walls.add((wall_x, y))
    else:
        wall = wall.split(", x=")
        wall_y = int(wall[0][2:])
        wall_xs = [int(x) for x in wall[1].split("..")]
        min_x = min(min_x, wall_xs[0])
        max_x = max(max_x, wall_xs[1])
        min_y = min(min_y, wall_y)
        max_y = max(max_y, wall_y)
        for x in range(wall_xs[0], wall_xs[1] + 1):
            walls.add((x, wall_y))
flow = {(500, 0)}
water = set()
all_things = flow | walls
obstacles = walls.copy()

while True:
    new_water, new_flow = water.copy(), set()
    for x, y in flow:
        if (x, y) not in new_water:
            new_flow.add((x, y))
        if y == max_y:
            continue
        i = 1
        while (x, y + i) not in all_things and y + i <= max_y:
            new_flow.add((x, y + i))
            i += 1
        if (x, y + 1) in walls or (x, y + 1) in water:
            if (x + 1, y) not in all_things:
                new_flow.add((x + 1, y))
            if (x - 1, y) not in all_things:
                new_flow.add((x - 1, y))
        if (x - 1, y) in walls and (x, y + 1) in obstacles:
            i = 1
            while (x + i, y) in flow and (x + i, y + 1) in obstacles:
                i += 1
            if (x + i, y) in walls:
                while i > 0:
                    new_water.add((x + i - 1, y))
                    if (x + i - 1, y) in new_flow:
                        new_flow.remove((x + i - 1, y))
                    i -= 1

    if flow == new_flow and water == new_water:
        break
    flow = new_flow
    water = new_water
    all_things = (flow | water | walls)
    obstacles = (water | walls)


print("Part 1:", len(water) + len(flow) - min_y)
print("Part 2:", len(water))



