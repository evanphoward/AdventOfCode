import functools


@functools.lru_cache(maxsize=None)
def num_arrangements(springs, groups, spring_index, group_index, current_block):
    if spring_index == len(springs):
        if group_index == len(groups) and current_block == 0:
            return 1
        elif group_index == len(groups) - 1 and current_block == groups[group_index]:
            return 1
        else:
            return 0
    total_arrange = 0
    current_spring = springs[spring_index]
    if current_spring == "?":
        if current_block == 0:
            total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index, 0)
        if group_index < len(groups) and groups[group_index] == current_block:
            total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index + 1, 0)
        total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index, current_block + 1)
    elif current_spring == ".":
        if current_block == 0:
            total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index, 0)
        elif group_index < len(groups) and groups[group_index] == current_block:
            total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index + 1, 0)
    else:
        total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index, current_block + 1)
    return total_arrange


inp = open("input").read().split("\n")
p1, p2 = 0, 0
for line in inp:
    s, g = line.split()
    g = tuple([int(x) for x in g.split(",")])
    p1 += num_arrangements(s, g, 0, 0, 0)
    p2 += num_arrangements("?".join([s] * 5), g * 5, 0, 0, 0)

print("Part 1:", p1)
print("Part 2:", p2)
