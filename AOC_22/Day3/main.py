def get_priority(item):
    return ord(item) + (1 - ord('a') if 'a' <= item <= 'z' else 27 - ord('A'))


rucksacks = open("input").read().strip().split("\n")
p1, p2 = 0, 0
for i, items in enumerate(rucksacks):
    overlap = list(set(items[:len(items)//2]).intersection(set(items[len(items)//2:])))[0]
    p1 += get_priority(overlap)
    if i % 3 == 0:
        p2 += get_priority(list(set(rucksacks[i]).intersection(rucksacks[i + 1]).intersection(rucksacks[i + 2]))[0])

print("Part 1:", p1)
print("Part 2:", p2)