inp = open("input").read().split("\n")
inp = [[[int(y) for y in x.split("|")[0].split(":")[1].split()], [int(y) for y in x.split("|")[1].split()]] for x in inp]
ans = 0

cards = [1 for _ in range(len(inp))]

for i, (winning, have_num) in enumerate(inp):
    matches = sum(num in have_num for num in winning)
    pts = 0 if matches == 0 else 2 ** (matches - 1)
    ans += pts
    for j in range(i + 1, i + matches + 1):
        cards[j] += cards[i]

print("Part 1:", ans)
print("Part 2:", sum(cards))