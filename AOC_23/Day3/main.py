from MiscFiles.library import *

inp = get_input(2023,3).split("\n")
ans = 0
grid = {}
marked = {}

for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[(r, c)] = cell

for r in range(len(inp)):
    for c in range(len(inp[0])):
        if (r, c) not in marked and grid[(r, c)].isdigit():
            cur_c = c
            num = ""
            while cur_c < len(inp[0]) and grid[(r, cur_c)].isdigit():
                num += grid[(r, cur_c)]
                cur_c += 1

            part = False
            for dr in [-1, 0, 1]:
                for col in range(c - 1, cur_c + 1):
                    if 0 <= r + dr < len(inp) and 0 <= col < len(inp[0]):
                        if grid[(r + dr, col)].isdigit():
                            marked[(r, col)] = int(num)
                        elif grid[(r + dr, col)] != ".":
                            part = True
            if part:
                ans += int(num)

print("Part 1:", ans)

ans = 0
for r in range(len(inp)):
    for c in range(len(inp[0])):
        if grid[(r, c)] == "*":
            adj = set((marked[(r + dr, c + dc)] if (r + dr, c + dc) in marked else 1) for dr, dc in
                      [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
            if len(adj) == 3:
                adj = list(adj)
                ans += adj[0] * adj[1] * adj[2]

print("Part 2:", ans)
