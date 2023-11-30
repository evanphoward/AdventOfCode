def get_compact_ranges(y):
    ranges = []
    for (sens_x, sens_y, beac_x, beac_y) in data:
        min_manhattan = abs(sens_x - beac_x) + abs(sens_y - beac_y)

        dist = abs(sens_y - y)
        mult = min_manhattan - dist
        if mult < 0:
            continue

        ranges.append((sens_x - mult, sens_x + mult))

    ranges.sort()

    compact = []
    low_x, high_x = ranges[0]
    for n_low_x, n_high_x in ranges[1:]:
        if n_low_x - 1 <= high_x:
            high_x = max(high_x, n_high_x)
        else:
            compact.append((low_x, high_x))
            low_x, high_x = n_low_x, n_high_x
    compact.append((low_x, high_x))
    return compact


s = open("input").read().strip()
s = s.split("\n")

MAX_COORD = 4000000
data = set()
s_beacons = dict()
beacons = set()
for x in s:
    sens, beac = x.split(": closest beacon is at x=")
    sens = sens[12:].split(", y=")
    sens = (int(sens[0]), int(sens[1]))
    beac = beac.split(", y=")
    beac = (int(beac[0]), int(beac[1]))
    data.add((sens[0], sens[1], beac[0], beac[1]))

part_1_range = get_compact_ranges(2000000)[0]
print("Part 1:", part_1_range[1] - part_1_range[0])

for y in range(0, MAX_COORD + 1):
    compact = get_compact_ranges(y)
    if len(compact) != 1:
        (a, b), (c, d) = compact
        x = b + 1
        print("Part 2:", x * 4000000 + y)
        exit()
