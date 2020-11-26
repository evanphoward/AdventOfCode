x = 0
y = 0
total_1 = 1
visited = {(0, 0)}
for dir in open("input").readline():
    if dir == "^":
        y += 1
    if dir == ">":
        x += 1
    if dir == "v":
        y -= 1
    if dir == "<":
        x -= 1
    if (x, y) not in visited:
        visited.add((x, y))
        total_1 += 1

rob_x = 0
rob_y = 0
x = 0
y = 0
total_2 = 1
visited = {(0, 0)}
santa_turn = True
for dir in open("input").readline():
    if santa_turn:
        if dir == "^":
            y += 1
        if dir == ">":
            x += 1
        if dir == "v":
            y -= 1
        if dir == "<":
            x -= 1
        if (x, y) not in visited:
            visited.add((x, y))
            total_2 += 1
    else:
        if dir == "^":
            rob_y += 1
        if dir == ">":
            rob_x += 1
        if dir == "v":
            rob_y -= 1
        if dir == "<":
            rob_x -= 1
        if (rob_x, rob_y) not in visited:
            visited.add((rob_x, rob_y))
            total_2 += 1
    santa_turn = False if santa_turn else True


print("Part 1:", total_1, "\nPart 2:", total_2)
