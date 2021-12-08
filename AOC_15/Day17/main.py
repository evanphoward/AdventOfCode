sizes = list(map(int, open("input").readlines()))

# Dynamic programming
# D[i] is a list of all sets of unique containers whose capacities add up to i
D = [[] for _ in range(151)]
D[0] = [set()]
for i in range(1, len(D)):
    for j, size in enumerate(sizes):
        if i - size < 0:
            continue
        for bucket_set in D[i - size]:
            if j in bucket_set:
                continue
            new_set = bucket_set.union({j})
            if new_set not in D[i]:
                D[i].append(new_set)

min_num = min(len(D[150][i]) for i in range(len(D[150])))
print("Part 1:", len(D[150]))
print("Part 2:", sum(len(D[150][i]) == min_num for i in range(len(D[150]))))

