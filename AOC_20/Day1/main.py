entries = [int(i) for i in open("input").readlines()]

for i in range(len(entries)):
    for j in range(i, len(entries)):
        if entries[i] + entries[j] == 2020:
            print("Part 1:", entries[i]*entries[j])
        for k in range(j, len(entries)):
            if entries[i] + entries[j] + entries[k] == 2020:
                print("Part 2:", entries[i]*entries[j]*entries[k])
