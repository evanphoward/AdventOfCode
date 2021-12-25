def value(vl):
    try:
        return int(vl)
    except ValueError:
        return registers[vl]


def compute(line, inp_p, inp):
    global registers
    inp_j = 0
    if line[0] == "inp":
        registers[line[1]] = int(inp[inp_p])
        inp_j += 1
    elif line[0] == "add":
        registers[line[1]] += value(line[2])
    elif line[0] == "mul":
        registers[line[1]] *= value(line[2])
    elif line[0] == "div":
        registers[line[1]] = value(line[1]) // value(line[2])
    elif line[0] == "mod":
        registers[line[1]] = value(line[1]) % value(line[2])
    elif line[0] == "eql":
        registers[line[1]] = int(value(line[1]) == value(line[2]))
    return 1, inp_j


prog = [line.strip().split() for line in open("input").readlines()]

# inp[2] + 6 == inp[3]
# inp[5] + 1 == inp[6]

# inp[4] + 5 == inp[7]
# inp[1] - 1 == inp[8]
# inp[10] + 8 == inp[11]
# inp[9] - 2 == inp[12]
# inp[0] - 8 == inp[13]
# 99394899891971
# 92171126131911
valid = []
for model in range(99399899999999, 11111111111111 - 1, -1):
    if "0" in str(model):
        continue
    rip = 0
    inp_p = 0
    registers = {"w": 0, "x": 0, "y": 0, "z": 0}
    while rip < len(prog):
        d_rip, d_inp_p = compute(prog[rip], inp_p, str(model))
        rip += d_rip
        inp_p += d_inp_p
    # print(model, registers["z"])
    if registers["z"] == 0:
        print(model)
        valid += [model]
        print(model)

print("Part 1:", max(valid))