totals = [0, 0, 0, 0, 0]
slope = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
lines = [line.strip() for line in open("input").readlines()]

i = 0
for right, down in slope:
    y = 0
    pos = 0
    while y < len(lines):
        if lines[y][pos % len(lines[y])] == "#":
            totals[i] += 1
        pos += right
        y += down
    i += 1

print("Part 1:", totals[1])
print("Part 2:", totals[0]*totals[1]*totals[2]*totals[3]*totals[4])
