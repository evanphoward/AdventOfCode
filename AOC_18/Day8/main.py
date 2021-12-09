points = [tuple(map(int, line.strip().split(", "))) for line in open("input").readlines()]
max_x = max(point[0] for point in points) + 1
max_y = max(point[1] for point in points) + 1

areas = [0] * len(points)
close_area = 0

for x in range(max_x):
    for y in range(max_y):
        min_distance = min(abs(x - point[0]) + abs(y - point[1]) for point in points)
        closest = [i for i, point in enumerate(points) if abs(x - point[0]) + abs(y - point[1]) == min_distance]
        if len(closest) == 1:
            if x == 0 or x == max_x or y == 0 or y == max_y:
                areas[closest[0]] = -1
            if areas[closest[0]] != -1:
                areas[closest[0]] += 1

        if sum(abs(x - point[0]) + abs(y - point[1]) for point in points) < 10000:
            close_area += 1

print("Part 1:", max(areas))
print("Part 2:", close_area)
