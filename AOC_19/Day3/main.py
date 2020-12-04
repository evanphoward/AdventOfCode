def calc_points(path):
    x = y = step = 0
    ordering = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    points = {}
    for segment in path:
        direction = ordering[segment[0]]
        for i in range(int(segment[1:])):
            x += direction[0]
            y += direction[1]
            step += 1
            if (x, y) not in points:
                points[(x, y)] = step
    return points


directions = open("input")

points_a = calc_points(directions.readline().split(","))
points_b = calc_points(directions.readline().split(","))

intersections = [point for point in points_a if point in points_b]

print("Part 1:", min(abs(x)+abs(y) for (x, y) in intersections))
print("Part 2:", min(points_a[pt] + points_b[pt] for pt in intersections))
