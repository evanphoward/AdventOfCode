inp = open("input").read().split("\n")
grid = dict()
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[r, c] = cell
nr = len(inp)
nc = len(inp[0])
assert nr == nc
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def simulate(start_r, start_c, start_direction):
    beams = [(start_r, start_c, start_direction)]
    energized = set()
    seen = set()
    while beams:
        r, c, direction = beams.pop()
        if (r, c) not in grid or (r, c, direction) in seen:
            continue
        seen.add((r, c, direction))
        energized.add((r, c))
        if grid[(r, c)] == "/":
            direction = (direction + (-1 if direction % 2 == 0 else 1)) % 4
        elif grid[(r, c)] == "\\":
            direction = (direction + (1 if direction % 2 == 0 else -1)) % 4
        elif grid[(r, c)] == "|" and direction in (0, 2):
            beams.append((r - 1, c, 3))
            beams.append((r + 1, c, 1))
            continue
        elif grid[(r, c)] == "-" and direction in (1, 3):
            beams.append((r, c + 1, 0))
            beams.append((r, c - 1, 2))
            continue
        dr, dc = DIRECTIONS[direction]
        r += dr
        c += dc
        beams.append((r, c, direction))
    return len(energized)


print("Part 1:", simulate(0, 0, 0))
print("Part 2:", max([max(simulate(i, 0, 0), simulate(0, i, 1), simulate(i, nc - 1, 2), simulate(nr - 1, i, 3)) for i in range(nr)]))
