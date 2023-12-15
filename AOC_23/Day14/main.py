inp = open("input").read().split("\n")
stops = set()
m_rolls = set()
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        if cell == "O":
            m_rolls.add((r, c))
        elif cell == "#":
            stops.add((r, c))
NR, NC = len(inp), len(inp[0])


def cycle(rolls, p1):
    for direction in [True, False]:
        for axis in [True, False]:
            new_rolls = set()
            for i in range(NC if axis else NR):
                last_stop = -1 if direction else (NR if axis else NC)
                num_rocks = 0
                for j in range(NR if axis else NC) if direction else range(NC - 1, -1, -1):
                    if (axis and (j, i) in stops) or (not axis and (i, j) in stops):
                        for k in range(last_stop + 1, last_stop + 1 + num_rocks) if direction else range(last_stop - 1, last_stop - num_rocks - 1, -1):
                            new_rolls.add((k, i) if axis else (i, k))
                        num_rocks = 0
                        last_stop = j
                    elif (axis and (j, i) in rolls) or (not axis and (i, j) in rolls):
                        num_rocks += 1
                for k in range(last_stop + 1, last_stop + 1 + num_rocks) if direction else range(last_stop - 1, last_stop - num_rocks - 1, -1):
                    new_rolls.add((k, i) if axis else (i, k))
            rolls = new_rolls
            if p1:
                return rolls

    return rolls


def weigh(rolls):
    return sum(NR - r for r, _ in rolls)


seen = set()
seen_index = dict()
target = 0

print("Part 1:", weigh(cycle(m_rolls, True)))

for i in range(1000000000):
    hashed_rolls = frozenset(m_rolls)

    if target == 0 and hashed_rolls in seen:
        start = seen_index[hashed_rolls]
        interval = i - seen_index[hashed_rolls]
        target = (1000000000 - start) % interval + start + interval

    if i == target and target:
        print("Part 2:", weigh(m_rolls))
        break

    seen.add(hashed_rolls)
    seen_index[hashed_rolls] = i
    m_rolls = cycle(m_rolls, False)







