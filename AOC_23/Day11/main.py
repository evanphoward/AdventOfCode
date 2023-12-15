import itertools

grid = dict()
inp = open("input").read().split("\n")
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[r, c] = cell

num_rows, num_cols = len(inp), len(inp[0])
empty_rows = set(r for r in range(num_rows) if all(grid[r, i] == "." for i in range(num_cols)))
empty_cols = set(c for c in range(num_cols) if all(grid[i, c] == "." for i in range(num_rows)))
galaxies = set((r, c) for r in range(num_rows) for c in range(num_cols) if grid[(r, c)] == "#")


def calc_sum(p2):
    ans = 0
    for pair in itertools.combinations(galaxies, 2):
        ans += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        for r in range(min(pair[0][0], pair[1][0]) + 1, max(pair[0][0], pair[1][0])):
            if r in empty_rows:
                ans += (1000000 - 1) if p2 else 1
        for c in range(min(pair[0][1], pair[1][1]) + 1, max(pair[0][1], pair[1][1])):
            if c in empty_cols:
                ans += (1000000 - 1) if p2 else 1
    return ans


print("Part 1:", calc_sum(False))
print("Part 2:", calc_sum(True))
