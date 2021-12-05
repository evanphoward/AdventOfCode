def fill_pipes(p1):
    seen_twice = set()
    seen = set()
    for pipe in inp:
        x1, y1 = pipe[0][0], pipe[0][1]
        x2, y2 = pipe[1][0], pipe[1][1]
        steps = max(abs(x2 - x1), abs(y2 - y1))
        dx = (x2 - x1) // steps
        dy = (y2 - y1) // steps
        if p1 and (dx != 0 and dy != 0):
            continue
        for i in range(steps + 1):
            new_pos = (x1 + (i * dx), y1 + (i * dy))
            if new_pos in seen:
                seen_twice.add(new_pos)
            seen.add(new_pos)
    return len(seen_twice)


inp = [[[int(x) for x in pos.split(",")] for pos in line.strip().split(" -> ")] for line in open("input").readlines()]
print("Part 1:", fill_pipes(True))
print("Part 2:", fill_pipes(False))
