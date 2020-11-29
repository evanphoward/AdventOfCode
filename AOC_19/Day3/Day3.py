ordering = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def add_points(points, direction):
    length = int(direction[1:])
    direction = ordering[direction[0]]
    x, y = points[len(points) - 1]
    for i in range(length):
        x += direction[0]
        y += direction[1]
        points.append((x, y))


points_a = [(0, 0)]
points_b = [(0, 0)]
directions = open("input")

for direction in directions.readline().split(","):
    add_points(points_a, direction)
for direction in directions.readline().split(","):
    add_points(points_b, direction)

intersections = []
for pt in points_a:
    if pt in points_b:
        intersections.append(pt)

print(intersections)