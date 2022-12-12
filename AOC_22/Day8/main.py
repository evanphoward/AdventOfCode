grid = dict()
inp = open("input").read().strip().split("\n")
for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[r, c] = int(cell)

rows = len(inp)
cols = len(inp[0])
highest_score = 0
num_visible = 0
for r in range(rows):
    for c in range(cols):
        score = 1
        visible = False
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            trees_seen = 0
            tr, tc = r + dr, c + dc
            while 0 <= tr < rows and 0 <= tc < cols:
                trees_seen += 1
                if grid[tr, tc] >= grid[r, c]:
                    break
                tr += dr
                tc += dc
            if tr in (-1, rows) or tc in (-1, cols):
                visible = True
            score *= trees_seen

        highest_score = max(score, highest_score)
        num_visible += visible

print("Part 1:", num_visible)
print("Part 2:", highest_score)
