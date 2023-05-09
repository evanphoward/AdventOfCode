inp = open("rocks").read().strip()

rocks = inp.split("\n\n")
for i in range(len(rocks)):
    rock = rocks[i].split("\n")
    rock = [[x == '#' for x in line] for line in rock]
    rocks[i] = rock
jet = [1 if x == ">" else -1 for x in open("input").read().strip()]


def top_rows(rcks, top):
    rows_to_scan = 4
    rcks = set(r for r in rcks if r[1] > top - rows_to_scan - 1)
    ret = ""
    for y in range(top - rows_to_scan - 1, top):
        for x in range(7):
            if (x, y) in rcks or y < 0:
                ret += "#"
            else:
                ret += "."
    return ret


width = 7
stopped_rocks = set()
tallest_y = -1
jet_i = 0
heights = []
steps = dict()
i = 0
while i < 1000000000000:
    dropped_rock = rocks[i % len(rocks)]
    step = (jet_i % len(jet), i % len(rocks), top_rows(stopped_rocks, tallest_y - 1))
    if i >= 2022 and step in steps:
        old_i, old_y = steps[step]
        dy = tallest_y - old_y
        di = i - old_i
        num_cycles = (1000000000000 - i) // di
        tallest_y += dy * num_cycles
        new_rocks = set()
        for r in stopped_rocks:
            new_rocks.add((r[0], r[1] + (dy * num_cycles)))
        stopped_rocks = new_rocks
        i += di * num_cycles
    steps[step] = (i, tallest_y)
    r_height, r_width = len(dropped_rock), len(dropped_rock[0])
    x = 2
    y = tallest_y + 3 + r_height

    while True:
        jet_x = x + jet[jet_i % len(jet)]
        jet_i += 1
        invalid = False
        for tx in range(jet_x, jet_x + r_width):
            for ty in range(y, y - r_height, -1):
                if dropped_rock[y - ty][tx - jet_x] and (tx < 0 or tx > 6 or (tx, ty) in stopped_rocks):
                    invalid = True
        if not invalid:
            x = jet_x
        if y == 0:
            break
        new_y = y - 1
        invalid = False
        for tx in range(x, x + r_width):
            for ty in range(new_y, new_y - r_height, -1):
                if dropped_rock[new_y - ty][tx - x] and (tx < 0 or tx > 6 or (tx, ty) in stopped_rocks):
                    invalid = True
        if invalid:
            break
        y = new_y
    if y > tallest_y:
        tallest_y = y

    for tx in range(x, x + r_width):
        for ty in range(y, y - r_height, -1):
            if dropped_rock[y - ty][tx - x]:
                stopped_rocks.add((tx, ty))
    heights.append((i % len(rocks), tallest_y))

    i += 1
    if i == 2022:
        print("Part 1:", tallest_y + 1)

print("Part 2:", tallest_y + 1)
