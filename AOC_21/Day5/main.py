def fill_pipes(p1):
    lines = [[0] * 1000 for _ in range(1000)]
    for pipe in inp:
        x1, y1 = pipe[0][0], pipe[0][1]
        x2, y2 = pipe[1][0], pipe[1][1]
        steps = max(abs(x2 - x1), abs(y2 - y1))
        dx = (x2 - x1) // steps
        dy = (y2 - y1) // steps
        if p1 and (dx != 0 and dy != 0):
            continue
        for i in range(steps + 1):
            lines[x1 + (i * dx)][y1 + (i * dy)] += 1
    return lines


inp = [[[int(x) for x in pos.split(",")] for pos in line.strip().split(" -> ")] for line in open("input").readlines()]
print("Part 1:", sum(sum(p >= 2 for p in row) for row in fill_pipes(True)))
print("Part 2:", sum(sum(p >= 2 for p in row) for row in fill_pipes(False)))
