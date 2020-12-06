groups = [list()]
group_count = [0]
i = 0
for line in open("input").readlines():
    if line == "\n":
        groups.append(list())
        group_count.append(0)
        i += 1
    else:
        group_count[i] += 1
        for char in line.strip():
            groups[i].append(char)

print("Part 1:", sum([len(set(group)) for group in groups]))
print("Part 2:", sum(sum(sum(x == char for x in groups[i]) == group_count[i] for char in set(groups[i])) for i in range(len(groups))))
