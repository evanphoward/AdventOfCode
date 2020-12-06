lines = [line for line in open("input").readlines()]
total = 0
groups = [set()]
groups_2 = [list()]
groups_3 = [0]
i = 0
for line in lines:
    if line == "\n":
        total += len(groups[i])
        groups.append(set())
        groups_2.append(list())
        groups_3.append(0)
        i += 1
    else:
        groups_3[i] += 1
    for char in line.strip():
        groups[i].add(char)
        groups_2[i].append(char)


print(sum([len(group) for group in groups]))
total = 0
for i in range(len(groups)):
    for char in groups[i]:
        if sum(x == char for x in groups_2[i]) == groups_3[i]:
            total += 1

print(total)