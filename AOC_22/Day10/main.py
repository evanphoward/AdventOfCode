inp = open("input").read().strip().split("\n")

p1_signals = 0
cycle = 1
x_reg = 1
pixels = dict()
for x in inp:
    pixels[(cycle % 40, cycle // 40)] = cycle % 40 in [x_reg, x_reg + 1, x_reg + 2]
    if cycle >= 20 and (cycle - 20) % 40 == 0:
        p1_signals += cycle * x_reg
    x = x.split()
    if x[0] == "addx":
        v = int(x[1])
        cycle += 1
        pixels[(cycle % 40, cycle // 40)] = cycle % 40 in [x_reg, x_reg + 1, x_reg + 2]
        if cycle >= 20 and (cycle - 20) % 40 == 0:
            p1_signals += cycle * x_reg
        x_reg += v
    cycle += 1

print("Part 1:", p1_signals)
print("Part 2:")
for y in range(6):
    for x in range(1, 40):
        print("#" if pixels[(x, y)] else " ", end="")
    print()

