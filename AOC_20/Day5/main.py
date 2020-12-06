seats = [int(str(''.join(['1' if ch in {"R", "B"} else '0' for ch in line.strip()])), 2) for line in open("input").readlines()]

print("Part 1:", max(seats))
for i in range(min(seats), max(seats) + 1):
    if i not in seats:
        print("Part 2:", i)
        break
