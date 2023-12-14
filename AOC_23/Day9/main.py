def get_next_value(seq, p2):
    diffs = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    sub_nxt = get_next_value(diffs, p2) if any(x != 0 for x in diffs) else 0
    return seq[0] - sub_nxt if p2 else seq[-1] + sub_nxt


inp = [[int(x) for x in line.split()] for line in open("input").read().split("\n")]
print("Part 1:", sum(get_next_value(line, False) for line in inp))
print("Part 2:", sum(get_next_value(line, True) for line in inp))
