inp = [int(x) for x in open("input").readlines()]
print(sum([inp[i] > inp[i - 1] for i in range(1, len(inp))]))
print(sum([inp[i + 3] > inp[i] for i in range(len(inp) - 3)]))
