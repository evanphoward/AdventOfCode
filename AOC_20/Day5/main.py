import math

seats = list()
for line in open("input").readlines():
    min_r = 0
    max_r = 127
    min_c = 0
    max_c = 7
    for ch in [char for char in line]:
        if ch == "F":
            max_r = (min_r + max_r) // 2
        elif ch == "B":
            min_r = math.ceil((min_r + max_r) / 2)
        elif ch == "R":
            min_c = math.ceil((min_c + max_c) / 2)
        elif ch == "L":
            max_c = (min_c + max_c) // 2
    seats.append(8*min_r+min_c)

print("Part 1:", max(seats))
for i in range(min(seats), max(seats) + 1):
    if i not in seats:
        print("Part 2:", i)
        break
