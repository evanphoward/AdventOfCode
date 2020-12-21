import copy


def step(grid, p2):
    new_grid = copy.deepcopy(grid)
    for d in range(min(grid.keys()), max(grid.keys()) + 1):
        for r in range(R):
            for c in range(C):
                if p2 and r == 2 and c == 2:
                    continue
                neighbors = 0
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= r + dr < R and 0 <= c + dc < C and (not p2 or r + dr != 2 or c + dc != 2):
                        neighbors += grid[d][r + dr][c + dc] == "#"
                    elif p2:
                        new_neighbors = list()
                        if r + dr == 2 and c + dc == 2:
                            new_d = d + 1
                            if r == 1:
                                for i in range(5):
                                    new_neighbors.append((0, i))
                            elif r == 3:
                                for i in range(5):
                                    new_neighbors.append((4, i))
                            elif c == 1:
                                for i in range(5):
                                    new_neighbors.append((i, 0))
                            elif c == 3:
                                for i in range(5):
                                    new_neighbors.append((i, 4))
                        else:
                            new_d = d - 1
                            if r + dr == -1:
                                new_neighbors.append((1, 2))
                            elif r + dr == 5:
                                new_neighbors.append((3, 2))
                            elif c + dc == -1:
                                new_neighbors.append((2, 1))
                            elif c + dc == 5:
                                new_neighbors.append((2, 3))
                        if new_d not in grid:
                            new_grid[new_d] = [["." for _ in range(5)] for _ in range(5)]
                            continue
                        for new_r, new_c in new_neighbors:
                            neighbors += grid[new_d][new_r][new_c] == "#"
                if grid[d][r][c] == "#" and neighbors != 1:
                    new_grid[d][r][c] = "."
                elif grid[d][r][c] == "." and neighbors in [1, 2]:
                    new_grid[d][r][c] = "#"
                else:
                    new_grid[d][r][c] = grid[d][r][c]
    return new_grid


state_1 = {0: [[ch for ch in line.strip()] for line in open("input").readlines()]}
state_2 = {-1: [["." for _ in range(5)] for _ in range(5)], 0: [[ch for ch in line.strip()] for line in open("input").readlines()], 1: [["." for _ in range(5)] for _ in range(5)]}
R = len(state_1[0])
C = len(state_1[0][0])
states = [state_1]
p1 = True
for _ in range(200):
    if p1:
        state_1 = step(state_1, False)
    state_2 = step(state_2, True)
    if p1 and state_1 in states:
        p1 = False
        i = 1
        rating = 0
        for r in range(R):
            for c in range(C):
                if state_1[0][r][c] == "#":
                    rating += i
                i *= 2
        print("Part 1:", rating)
    states.append(state_1)

total = 0
for d in range(min(state_2), max(state_2) + 1):
    for r in range(R):
        for c in range(C):
            if r != 2 or c != 2:
                total += state_2[d][r][c] == "#"
print("Part 2:", total)

