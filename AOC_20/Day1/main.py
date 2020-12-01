entries = list()
for line in open("input").readlines():
    entries.append(int(line))

for i in range(len(entries)):
    for j in range(len(entries)):
        if i != j:
            if entries[i] + entries[j] == 2020:
                print("Part 1:", entries[i]*entries[j])

for i in range(len(entries)):
    for j in range(len(entries)):
        for k in range(len(entries)):
            if i != j and i != k and j != k:
                if entries[i] + entries[j] + entries[k] == 2020:
                    print("Part 2:", entries[i]*entries[j]*entries[k])
