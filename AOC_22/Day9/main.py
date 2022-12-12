def tail_pos(num_knots):
    deltas = {"R": (1, 0), "U": (0, 1), "D": (0, -1), "L": (-1, 0)}
    pos = {(0, 0)}
    knots = [[0, 0] for _ in range(num_knots)]
    for x in open("input").read().strip().split("\n"):
        d, dist = x.split()
        dist = int(dist)
        dx, dy = deltas[d]

        for _ in range(dist):
            knots[0][0] += dx
            knots[0][1] += dy
            for i in range(1, len(knots)):
                if abs(knots[i - 1][0] - knots[i][0]) > 1 or abs(knots[i - 1][1] - knots[i][1]) > 1:
                    kdx = knots[i - 1][0] - knots[i][0]
                    kdy = knots[i - 1][1] - knots[i][1]
                    if abs(kdx) > 1:
                        knots[i][0] += (kdx - 1) if kdx > 1 else (kdx + 1)
                    else:
                        knots[i][0] += kdx
                    if abs(kdy) > 1:
                        knots[i][1] += (kdy - 1) if kdy > 1 else (kdy + 1)
                    else:
                        knots[i][1] += kdy
                    if i == len(knots) - 1:
                        pos.add((knots[i][0], knots[i][1]))
    return len(pos)


print("Part 1:", tail_pos(2))
print("Part 2:", tail_pos(10))
