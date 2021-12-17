def step(x, y, dx, dy):
    x += dx
    y += dy
    if dx < 0:
        dx += 1
    elif dx > 0:
        dx -= 1
    dy -= 1
    return x, y, dx, dy


bounds = [bound[2:] for i, bound in enumerate(open("input").readline().replace(",", "").split()) if i in (2, 3)]
min_x, max_x = map(int, bounds[0].split(".."))
min_y, max_y = map(int, bounds[1].split(".."))
highest = []
for vel_x in range(max_x + 1):
    for vel_y in range(min_y, 300):
        x = y = highest_y = 0
        dx, dy = vel_x, vel_y
        while x <= max_x and y >= min_y:
            x += dx
            y += dy
            if dx < 0:
                dx += 1
            elif dx > 0:
                dx -= 1
            dy -= 1
            highest_y = max(y, highest_y)
            if min_y <= y <= max_y and min_x <= x <= max_x:
                highest.append(highest_y)
                break
print("Part 1:", max(highest))
print("Part 2:", len(highest))
