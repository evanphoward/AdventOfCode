bounds = open("input").readline().replace(",","").split()
min_x, max_x = map(int, bounds[2][2:].split(".."))
min_y, max_y = map(int, bounds[3][2:].split(".."))
highest = []
for vel_x in range(max_x + 1):
    for vel_y in range(min_y, 300):
        x = y = highest_y = 0
        dx, dy = vel_x, vel_y
        while x <= max_x and y >= min_y:
            x += dx
            y += dy
            dx += 1 if dx < 0 else -1 if dx > 0 else 0
            dy -= 1
            highest_y = y if dy >= 0 else highest_y
            if min_y <= y <= max_y and min_x <= x <= max_x:
                highest.append(highest_y)
                break

print("Part 1:", max(highest))
print("Part 2:", len(highest))
