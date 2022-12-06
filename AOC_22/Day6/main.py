inp = open("input").read().strip()

p1 = True
for i in range(3, len(inp)):
    if p1 and len({inp[i], inp[i - 1], inp[i - 2], inp[i - 3]}) == 4:
        p1 = False
        print("Part 1:", i + 1)
    if i >= 13:
        if len({inp[i], inp[i - 1], inp[i - 2], inp[i - 3], inp[i - 4], inp[i - 5], inp[i - 6], inp[i - 7], inp[i - 8],
                inp[i - 9], inp[i - 10], inp[i - 11], inp[i - 12], inp[i - 13]}) == 14:
            print("Part 2:", i + 1)
            break
