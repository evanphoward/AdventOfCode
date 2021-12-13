points = [(int(line[10:line.index(",")]), int(line[line.index(",") + 2:line.index(">")]),
           int(line[line.index(">")+12:line.index(">")+14]), int(line[line.index(">")+16:line.index(">")+18]))
          for line in open("input").readlines()]
i = 0
while True:
    if all(abs(p[0]) + abs(p[1]) < 350 for p in points):
        print("Part 1:")
        for y in range(min(p[1] for p in points), max(p[1] for p in points) + 1):
            for x in range(min(p[0] for p in points), max(p[0] for p in points) + 1):
                if any((point[0], point[1]) == (x, y) for point in points):
                    print("█", end="")
                else:
                    print(" ", end="")
            print()
        print("Part 2:", i)
        break
    points = [(point[0] + point[2], point[1] + point[3], point[2], point[3]) for point in points]
    i += 1
