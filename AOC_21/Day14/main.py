from collections import defaultdict, Counter
inp = open("input").read().split("\n")
start = inp[0]
rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in inp[2:]}

counts = Counter(start)
pattern = defaultdict(int)
for i in range(len(start) - 1):
    pattern[start[i] + start[i + 1]] += 1

for step in range(40):
    new_pattern = defaultdict(int)
    for pair, count in pattern.items():
        new_character = rules[pair]
        new_pattern[pair[0] + new_character] += count
        new_pattern[new_character + pair[1]] += count
        counts[new_character] += count
    pattern = new_pattern
    if step == 9:
        print("Part 1:", max(counts.values()) - min(counts.values()))

print("Part 2:", max(counts.values()) - min(counts.values()))