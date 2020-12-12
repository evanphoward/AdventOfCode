heading = 0
x1 = y1 = 0
x2 = y2 = 0
wx = 10
wy = 1
cardinal = {"E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0, 1)}
directions = list(cardinal.values())
for line in open("input").readlines():
    move = line[0]
    amount = int(line[1:])
    if move == "L":
        for i in range(int(amount/90)):
            tmp = wx
            wx = -wy
            wy = tmp
            heading -= 1
            if heading < 0:
                heading = 3
    elif move == "R":
        for i in range(int(amount / 90)):
            tmp = wy
            wy = -wx
            wx = tmp
            heading += 1
            if heading > 3:
                heading = 0
    elif move == "F":
        dx, dy = directions[heading]
        x1 += dx * amount
        y1 += dy * amount
        x2 += wx * amount
        y2 += wy * amount
    else:
        y1 += cardinal[move][1] * amount
        wy += cardinal[move][1] * amount
        x1 += cardinal[move][0] * amount
        wx += cardinal[move][0] * amount

print("Part 1:", abs(x1) + abs(y1))
print("Part 2:", abs(x2) + abs(y2))
