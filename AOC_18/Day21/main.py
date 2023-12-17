# [a, b, c, d, e, ip]
# [0, 1, 2, 3, 4,  5]
# Completely reverse engineered solution unfortunately
d = 0
s = set()
part1 = True
seen_ordered = []
while True:
    b = d | 65536
    d = 9450265
    while True:
        e = b & 0xFF
        d += e
        d &= 16777215
        d *= 65899
        d &= 16777215
        if 256 > b:
            if part1:
                print("Part 1:", d)
                part1 = False
            else:
                if d not in s:
                    seen_ordered.append(d)
                else:
                    print("Part 2:", seen_ordered[-1])
                    exit()
            s.add(d)
            break
        b = b // 256