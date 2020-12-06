from AOC_19.IntComputer import IntProcess


robot = IntProcess(open("input"))
panels = {}
x = y = 0
dx = 0
dy = 1
total_painted = set()
while robot.ip != -1:
    if (x, y) not in panels.keys():
        panels[(x, y)] = 0
    color = panels[(x, y)]
    paint, turn = robot.run([color])
    panels[(x, y)] = paint
    if paint == 1:
        total_painted.add((x, y))
    if dx == 0:
        dx = 1 if (dy == 1 and turn == 1) or (dy == -1 and turn == 0) else -1
        dy = 0
    else:
        dy = 1 if (dx == 1 and turn == 0) or (dx == -1 and turn == 1) else -1
        dx = 0
    x += dx
    y += dy

print("Part 1:", len(total_painted))


robot = IntProcess(open("input"))
panels = {(0, 0) : 1}
x = y = 0
dx = 0
dy = 1
while robot.ip != -1:
    if (x, y) not in panels.keys():
        panels[(x, y)] = 0
    color = panels[(x, y)]
    paint, turn = robot.run([color])
    panels[(x, y)] = paint
    if dx == 0:
        dx = 1 if (dy == 1 and turn == 1) or (dy == -1 and turn == 0) else -1
        dy = 0
    else:
        dy = 1 if (dx == 1 and turn == 0) or (dx == -1 and turn == 1) else -1
        dx = 0
    x += dx
    y += dy

print("Part 2:")
for y in reversed(range(min([x[0][1] for x in panels.items()]), max([x[0][1] for x in panels.items()]) + 1)):
    row = ""
    for x in range(min([x[0][0] for x in panels.items()]), max([x[0][0] for x in panels.items()]) + 1):
        if (x, y) not in panels:
            row = row + " "
            continue
        row = row + ("#" if panels[(x, y)] == 1 else " ")
    print(row)
