from collections import Counter
elves = set()
inp = open("input").read().strip().split("\n")
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        if cell == "#":
            elves.add((r, c))
nbrs = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1)]


def step(g, i):
    moves = dict()
    moved = 0
    for r, c in g:
        if sum((r + dr, c + dc) in g for dr, dc in nbrs) == 0:
            moves[(r, c)] = (r, c)
            continue
        moved += 1
        # Conditions to move N, S, W, E
        conditions = [((r - 1, c) not in g and (r - 1, c + 1) not in g and (r - 1, c - 1) not in g),
                      (r + 1, c) not in g and (r + 1, c + 1) not in g and (r + 1, c - 1) not in g,
                      (r, c - 1) not in g and (r + 1, c - 1) not in g and (r - 1, c - 1) not in g,
                      (r, c + 1) not in g and (r + 1, c + 1) not in g and (r - 1, c + 1) not in g]
        moves_to_make = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        if conditions[i % 4]:
            moves[(r, c)] = moves_to_make[i % 4]
        elif conditions[(i % 4 + 1) % 4]:
            moves[(r, c)] = moves_to_make[(i % 4 + 1) % 4]
        elif conditions[(i % 4 + 2) % 4]:
            moves[(r, c)] = moves_to_make[(i % 4 + 2) % 4]
        elif conditions[(i % 4 + 3) % 4]:
            moves[(r, c)] = moves_to_make[(i % 4 + 3) % 4]
        else:
            moves[(r, c)] = (r, c)
    if moved == 0:
        return False
    num_moves = Counter(moves.values())
    for e, move in moves.items():
        if num_moves[move] > 1:
            moves[e] = e
    return set(moves.values())


i = 0
while True:
    elves = step(elves, i)
    i += 1
    if i == 10:
        print("Part 1:", ((max(r for (r, c) in elves) - min(r for (r, c) in elves) + 1) *
                          (max(c for (r, c) in elves) - min(c for (r, c) in elves) + 1)) - len(elves))
    if not elves:
        print("Part 2:", i)
        break
