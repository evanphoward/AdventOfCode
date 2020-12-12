seats_root = dict()
x = y = 0
for line in open("input").readlines():
    for ch in line.strip():
        seats_root[(x, y)] = ch
        x += 1
    max_x = x
    x = 0
    y += 1
max_y = y

seats = seats_root.copy()
new_seats = dict()
while True:
    for x in range(max_x):
        for y in range(max_y):
            change = False
            if seats[(x, y)] == "L":
                change = True
                for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    if 0 <= x + dx < max_x and 0 <= y + dy < max_y:
                        if seats[(x + dx, y + dy)] == "#":
                            change = False
            if seats[(x, y)] == "#":
                num_occupied = 0
                for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    if 0 <= x + dx < max_x and 0 <= y + dy < max_y:
                        if seats[(x + dx, y + dy)] == "#":
                            num_occupied += 1
                if num_occupied >= 4:
                    change = True
            if change:
                new_seats[(x, y)] = "L" if seats[(x, y)] == "#" else "#"
            else:
                new_seats[(x, y)] = seats[(x, y)]
    done = True
    for x in range(max_x):
        for y in range(max_y):
            if seats[(x, y)] != new_seats[(x, y)]:
                done = False
    if done:
        print("Part 1:", sum([x == "#" for x in seats.values()]))
        break
    seats = new_seats.copy()

seats = seats_root.copy()
new_seats = dict()
while True:
    for x in range(max_x):
        for y in range(max_y):
            change = False
            if seats[(x, y)] == "L":
                change = True
                for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    tmp_x = x + dx
                    tmp_y = y + dy
                    while 0 <= tmp_x < max_x and 0 <= tmp_y < max_y and seats[(tmp_x, tmp_y)] == ".":
                        tmp_x += dx
                        tmp_y += dy
                    if 0 <= tmp_x < max_x and 0 <= tmp_y < max_y:
                        if seats[(tmp_x, tmp_y)] == "#":
                            change = False
            if seats[(x, y)] == "#":
                num_occupied = 0
                for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    tmp_x = x + dx
                    tmp_y = y + dy
                    while 0 <= tmp_x < max_x and 0 <= tmp_y < max_y and seats[(tmp_x, tmp_y)] == ".":
                        tmp_x += dx
                        tmp_y += dy
                    if 0 <= tmp_x < max_x and 0 <= tmp_y < max_y:
                        if seats[(tmp_x, tmp_y)] == "#":
                            num_occupied += 1
                if num_occupied >= 5:
                    change = True
            if change:
                new_seats[(x, y)] = "L" if seats[(x, y)] == "#" else "#"
            else:
                new_seats[(x, y)] = seats[(x, y)]
    done = True
    for x in range(max_x):
        for y in range(max_y):
            if seats[(x, y)] != new_seats[(x, y)]:
                done = False
    if done:
        print("Part 2:", sum([x == "#" for x in seats.values()]))
        exit()
    seats = new_seats.copy()

