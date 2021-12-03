def gen_string(inp, bit):
    i = 0
    while len(inp) > 1:
        if sum(line[i] == '1' for line in inp) >= len(inp) / 2:
            inp = list(filter(lambda x: x[i] == bit, inp))
        else:
            inp = list(filter(lambda x: x[i] != bit, inp))
        i += 1
    return inp[0]


inp = [line.strip() for line in open("input").readlines()]
bits = len(inp[0])
freq = [0] * bits

for i in range(bits):
    freq[i] = sum(line[i] == "1" for line in inp)
gamma = ''.join(['1' if freq[i] > len(inp) / 2 else '0' for i in range(bits)])
epsilon = ''.join(['0' if gamma[i] == '1' else '1' for i in range(bits)])

print("Part 1:", int(epsilon, 2) * int(gamma, 2))
print("Part 2:", int(gen_string(inp, '1'), 2) * int(gen_string(inp, '0'), 2))
