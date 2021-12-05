blacklist_ints = [list(map(int, line.strip().split("-"))) for line in open("input").readlines()]
blacklist_ints.sort(key=lambda x: x[0])

merged = []
for interval in blacklist_ints:
    if len(merged) == 0 or merged[-1][1] < interval[0] - 1:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

print("Part 1:", merged[0][1] + 1)
total = 4294967296
for interval in merged:
    total -= (interval[1] - interval[0] + 1)
print("Part 2:", total)

