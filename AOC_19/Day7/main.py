import itertools

prog_mast = [int(i) for i in open("input").readline().split(",")]
lengths = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}


def value(prog, mode, params, index):
    return prog[params[index]] if mode[index] == 0 else params[index]


def do_op(prog, opcode, mode, params, index):
    if opcode == 1:
        prog[params[2]] = value(prog, mode, params, 0) + value(prog, mode, params, 1)
    elif opcode == 2:
        prog[params[2]] = value(prog, mode, params, 0) * value(prog, mode, params, 1)
    elif opcode == 3:
        prog[params[0]] = int(input("In?"))
    elif opcode == 4:
        print(value(prog, mode, params, 0))
    elif opcode == 5:
        if value(prog, mode, params, 0) != 0:
            index = value(prog, mode, params, 1)
    elif opcode == 6:
        if value(prog, mode, params, 0) == 0:
            index = value(prog, mode, params, 1)
    elif opcode == 7:
        prog[params[2]] = value(prog, mode, params, 0) < value(prog, mode, params, 1)
    elif opcode == 8:
        prog[params[2]] = value(prog, mode, params, 0) == value(prog, mode, params, 1)

    return index


def run(prog, i, inp):
    inp_i = 0
    out = list()
    while True:
        params = list()
        mode = list()

        rev = str(prog[i])[::-1]
        if len(rev) == 1:
            rev = rev[0] + "0"
        opcode = int(rev[1] + rev[0])
        mode = [int(i) for i in rev[2:]]

        if opcode == 99:
            return (prog, -1), out

        length = lengths[opcode]
        while len(mode) < length:
            mode.append(0)
        for j in range(1, length + 1):
            params.append(prog[i + j])
        i += length + 1

        if opcode == 3:
            if inp_i == len(inp):
                return (prog, i - length - 1), out
            else:
                prog[params[0]] = inp[inp_i]
                inp_i += 1
                continue
        if opcode == 4:
            out.append(value(prog, mode, params, 0))
            continue

        i = do_op(prog, opcode, mode, params, i)


outputs_1 = list()
for perm in list(itertools.permutations([0, 1, 2, 3, 4])):
    out = [0]
    for i in range(0, 5):
        mem, out = run(prog_mast.copy(), 0, [perm[i]] + out)
    outputs_1.append(out[0])


outputs_2 = list()
for perm in list(itertools.permutations([5, 6, 7, 8, 9])):
    mem = [(prog_mast.copy(), 0), (prog_mast.copy(), 0), (prog_mast.copy(), 0), (prog_mast.copy(), 0),
           (prog_mast.copy(), 0)]
    out = [0]
    for i in range(0, 5):
        mem[i], out = run(mem[i][0], mem[i][1], [perm[i]] + out)
    while mem[4][1] != -1:
        for i in range(0, 5):
            mem[i], out = run(mem[i][0], mem[i][1], out)
            if len(out) == 0:
                print("Here")
    outputs_2.append(out[0])

print("Part 1:", max(outputs_1))
print("Part 2:", max(outputs_2))
