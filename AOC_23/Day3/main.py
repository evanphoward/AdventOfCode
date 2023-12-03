inp = open("input").read().split("\n")
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
            while cur_c > 1 and grid[(r, cur_c - 1)].isdigit():
                cur_c -= 1
            num = ""
            init_c = cur_c
            while cur_c < len(inp[0]) and grid[(r, cur_c)].isdigit():
                num += grid[(r, cur_c)]
                cur_c += 1
            part = False
            if init_c != 0 and grid[(r, init_c - 1)] != ".":
                part = True
            if cur_c < len(inp[0]) - 1 and grid[(r, cur_c)] != ".":
                part = True
            for col in range(init_c, cur_c):
                marked[(r, col)] = int(num)
            for col in range(init_c - 1, cur_c + 1):
                if col < 0 or col >= len(inp[0]):
                    continue
                if r > 0 and grid[(r - 1, col)] != ".":
                    part = True
                if r < len(inp) - 1 and grid[(r + 1, col)] != ".":
                    part = True
            if part:
                ans += int(num)

print("Part 1:", ans)

ans = 0
for r in range(len(inp)):
    for c in range(len(inp[0])):
        if grid[(r, c)] == "*":
            adj = set((marked[(r + dr, c + dc)] if (r + dr, c + dc) in marked else 1) for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
            if len(adj) == 3:
                adj = list(adj)
                ans += adj[0] * adj[1] * adj[2]

print("Part 2:", ans)
