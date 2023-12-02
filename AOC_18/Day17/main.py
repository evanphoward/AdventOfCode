s = open("input").read().strip()
s = s.split("\n")

walls = set()
min_y, max_y = 0, 0
for wall in s:
    if wall[0] == "x":
        wall = wall.split(", y=")
        wall_x = int(wall[0][2:])
        wall_ys = map(int, wall[1].split(".."))
        min_y = min(min_y, wall_ys[0])
        max_y = max(max_y, wall_ys[1])
        for y in range(wall_ys[0], wall_ys[1] + 1):
            walls.add((wall_x, y))
    else:
        wall = wall.split(", x=")
        wall_y = int(wall[0][2:])
        wall_xs = map(int, wall[1].split(".."))
        for x in range(wall_xs[0], wall_xs[1] + 1):
            walls.add((x, wall_y))


def simulate_water(p1):
    obstacles = walls.copy()
    off_map = set()
    while True:
        if (500, 0) in obstacles:
            return len(obstacles) - len(walls) + len(off_map)
        water_x = 500
        water_y = 0
        while True:
            if water_y == max_y or (water_x, water_y + 1) in off_map:
                print(water_x, water_y)
                off_map.add((water_x, water_y))
                break
            if (water_x, water_y + 1) not in obstacles:
                water_y += 1
                continue
            elif (water_x - 1, water_y) not in obstacles:
                while (water_x - 1, water_y) not in obstacles and (water_x, water_y + 1) in obstacles:
                    water_x -= 1
                if (water_x, water_y + 1) in off_map:
                    obstacles.add((water_x, water_y))
                    break
                if (water_x, water_y + 1) not in obstacles:
                    continue
            elif (water_x + 1, water_y) not in obstacles:
                while (water_x + 1, water_y) not in obstacles and (water_x, water_y + 1) in obstacles:
                    water_x += 1
                if (water_x, water_y + 1) in off_map:
                    obstacles.add((water_x, water_y))
                    break
                if (water_x, water_y + 1) not in obstacles:
                    continue
            print(water_x, water_y)
            obstacles.add((water_x, water_y))
            break


print("Part 1:", simulate_water(True))
# print("Part 2:", simulate_water(False))
