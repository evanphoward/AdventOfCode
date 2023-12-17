inp = open("input").read().split("\n")
bots = []
for bot in inp:
    pos, r = bot.split(", ")
    pos = tuple(map(int, pos[5:-1].split(",")))
    r = int(r[2:])
    bots.append((r, pos))
bots.sort(reverse=True)
best_bot = bots[0]

ans = 0
for bot in bots:
    pos = bot[1]
    dist = abs(best_bot[1][0] - pos[0]) + abs(best_bot[1][1] - pos[1]) + abs(best_bot[1][2] - pos[2])
    if dist <= best_bot[0]:
        ans += 1
print(ans)