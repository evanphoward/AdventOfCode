import heapq

grid = dict()
inp = open("input").read().split("\n")
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[(r, c)] = int(cell)
nr = len(inp)
nc = len(inp[0])


def run(p2):
    q = [(0, (0, 0), 0, -1)]
    explored = set()
    while q:
        steps, pos, num_straight, direction = heapq.heappop(q)
        if pos == (nr - 1, nc - 1) and (not p2 or num_straight >= 4):
            return steps
        for i, (dr, dc) in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
            if direction >= 0 and (dr, dc) == [(-1, 0), (1, 0), (0, -1), (0, 1)][direction]:
                continue
            if direction != -1 and p2:
                if num_straight < 4 and i != direction:
                    continue
                if num_straight >= 10 and i == direction:
                    continue
            new_num_straight = 1 if i != direction else num_straight + 1
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos not in grid:
                continue
            if p2 and (new_pos, new_num_straight, i) not in explored:
                explored.add((new_pos, new_num_straight, i))
                heapq.heappush(q, (steps + grid[new_pos], new_pos, new_num_straight, i))
            elif new_pos not in explored:
                explored.add(new_pos)
                heapq.heappush(q, (steps + grid[new_pos], new_pos, new_num_straight, i))
    return -1


print("Part 1:", run(False))
print("Part 2:", run(True))
