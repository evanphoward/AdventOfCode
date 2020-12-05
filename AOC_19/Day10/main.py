import math

lines = open("input").readlines()
WIDTH = len(lines[0].strip())
HEIGHT = len(lines)

asteroids = {}
best_loc = (0, 0)
for x in range(WIDTH):
    for y in range(HEIGHT):
        asteroids[(x, y)] = lines[y][x] == '#'
        if asteroids[(x, y)]:
            best_loc = (x, y)


def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)


def asteroids_visible(x, y):
    global asteroids
    amt = 0
    for dx in range(-x, WIDTH - x):
        for dy in range(-y, HEIGHT - y):
            if abs(gcf(dy, dx)) != 1:
                continue
            cur_x = x + dx
            cur_y = y + dy
            while 0 <= cur_x < WIDTH and 0 <= cur_y < HEIGHT:
                if asteroids[(cur_x, cur_y)]:
                    amt += 1
                    break
                cur_x += dx
                cur_y += dy
    return amt


def asteroids_angle(x, y):
    global asteroids
    seen_asteroids = {}
    for dx in range(-x, WIDTH - x):
        for dy in range(-y, HEIGHT - y):
            if abs(gcf(dy, dx)) != 1:
                continue
            cur_x = x + dx
            cur_y = y + dy
            while 0 <= cur_x < WIDTH and 0 <= cur_y < HEIGHT:
                if asteroids[(cur_x, cur_y)]:
                    if dx == 0:
                        angle = 0 if dy < 0 else math.pi
                    else:
                        angle = math.atan(dy / dx) + math.pi
                        if dx < 0:
                            angle += math.pi
                    seen_asteroids[(cur_x, cur_y)] = angle
                    break
                cur_x += dx
                cur_y += dy
    return seen_asteroids


for x in range(WIDTH):
    for y in range(HEIGHT):
        if asteroids[(x, y)]:
            if asteroids_visible(x, y) > asteroids_visible(best_loc[0], best_loc[1]):
                best_loc = (x, y)

print("Part 1:", asteroids_visible(best_loc[0], best_loc[1]))
angles = asteroids_angle(best_loc[0], best_loc[1])
angles = sorted(angles.items(), key=lambda item: item[1])
print("Part 2:", angles[199][0][0]*100 + angles[199][0][1])
