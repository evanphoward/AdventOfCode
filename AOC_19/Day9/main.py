prog_mast = [int(i) for i in open("input").readline().split(",")]
for i in range(10000000):
    prog_mast.append(0)
lengths = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}


def value(prog, mode, params, index, rb):
    if mode[index] == 0:
        return prog[params[index]]
    if mode[index] == 1:
        return params[index]
    if mode[index] == 2:
        return prog[rb + params[index]]
    return prog[params[index]] if mode[index] == 0 else params[index]


def do_op(prog, opcode, mode, params, index, rb):
    first_value = value(prog, mode, params, 0, rb)
    if len(params) > 2:
        second_value = value(prog, mode, params, 1, rb)
    if opcode == 1:
        prog[params[2] + (mode[2] // 2 * rb)] = first_value + second_value
    elif opcode == 2:
        prog[params[2] + (mode[2] // 2 * rb)] = first_value * second_value
    elif opcode == 3:
        prog[params[0] + (mode[0] // 2 * rb)] = int(input("In?"))
    elif opcode == 4:
        print(first_value)
    elif opcode == 5:
        if first_value != 0:
            index = value(prog, mode, params, 1, rb)
    elif opcode == 6:
        if first_value == 0:
            index = value(prog, mode, params, 1, rb)
    elif opcode == 7:
        prog[params[2] + (mode[2] // 2 * rb)] = first_value < second_value
    elif opcode == 8:
        prog[params[2] + (mode[2] // 2 * rb)] = first_value == second_value
    elif opcode == 9:
        rb += first_value

    return index, rb


def run(prog, i, inp):
    inp_i = 0
    out = list()
    rb = 0
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
                prog[params[0] + (mode[0] // 2 * rb)] = inp[inp_i]
                inp_i += 1
                continue
        if opcode == 4:
            out.append(value(prog, mode, params, 0, rb))
            continue

        i, rb = do_op(prog, opcode, mode, params, i, rb)


print("Part 1:", run(prog_mast, 0, [1])[1][0])
print("Part 2:", run(prog_mast, 0, [2])[1][0])
