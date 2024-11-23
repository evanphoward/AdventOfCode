def gen(val, factor, check):
    while True:
        val = (val * factor) % 2147483647
        if check == -1 or val % check == 0:
            yield val


def get_matches(part_two):
    ans = 0
    A = gen(703, 16807, 4 if part_two else -1)
    B = gen(516, 48271, 8 if part_two else -1)
    for _ in range(5000000 if part_two else 40000000):
        if next(A) & 0xFFFF == next(B) & 0xFFFF:
            ans += 1
    return ans

print("Part 1:", get_matches(False))
print("Part 2:", get_matches(True))
