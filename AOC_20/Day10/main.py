adapters = sorted([int(line.strip()) for line in open("input").readlines()] + [0])
adapters.append(max(adapters) + 3)

ones = sum([1 for i in range(1, len(adapters)) if adapters[i] - adapters[i - 1] == 1])
threes = sum([1 for i in range(1, len(adapters)) if adapters[i] - adapters[i - 1] == 1])
print("Part 1:", ones * threes)

ways = [0]*(len(adapters))
ways[0] = 1
for i in range(1, len(adapters)):
    ways[i] += sum([ways[j] for j in range(0, i) if adapters[i] - adapters[j] <= 3])
print("Part 2:", ways[-1])
