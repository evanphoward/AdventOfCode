s = open("input").read().strip()
s = s.split("\n")

walls = set()
max_y = 0
for wall in s:
    wall = wall.split(" -> ")
    for i in range(1, len(wall)):
        x, y = wall[i].split(",")
        x = int(x)
        y = int(y)
        prev_x, prev_y = wall[i - 1].split(",")
        prev_x = int(prev_x)
        prev_y = int(prev_y)
        if y > max_y or prev_y > max_y:
            max_y = max(y, prev_y)
        if x == prev_x:
            for ty in range(min(y, prev_y), max(y, prev_y) + 1):
                walls.add((x, ty))
        else:
            for tx in range(min(x, prev_x), max(x, prev_x) + 1):
                walls.add((tx, y))
max_y += 2


def simulate_sand(p1):
    obstacles = walls.copy()
    while True:
        if not p1 and (500, 0) in obstacles:
            return len(obstacles) - len(walls)
        sand_x = 500
        sand_y = 0
        while True:
            if sand_y + 1 == max_y:
                if p1:
                    return len(obstacles) - len(walls)
                else:
                    obstacles.add((sand_x, sand_y))
                    break
            if (sand_x, sand_y + 1) not in obstacles:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in obstacles:
                sand_y += 1
                sand_x -= 1
            elif (sand_x + 1, sand_y + 1) not in obstacles:
                sand_y += 1
                sand_x += 1
            else:
                obstacles.add((sand_x, sand_y))
                break


print("Part 1:", simulate_sand(True))
print("Part 2:", simulate_sand(False))
