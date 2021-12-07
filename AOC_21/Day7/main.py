pos = list(map(int, open("input").readline().split(",")))
print("Part 1:", min(sum(abs(pos[j] - i) for j in range(len(pos))) for i in range(len(pos))))
print("Part 2:", min(sum(((abs(pos[j] - i) * (abs(pos[j] - i) + 1)) // 2) for j in range(len(pos))) for i in range(len(pos))))
