prog = [int(i) for i in open("input").readline().split(",")]


def value(mode, params, index):
    global prog
    return prog[params[index]] if mode[index] == 0 else params[index]


def do_op(opcode, mode, params, index):
    global prog
    if opcode == 1:
        prog[params[2]] = value(mode, params, 0) + value(mode, params, 1)
    elif opcode == 2:
        prog[params[2]] = value(mode, params, 0) * value(mode, params, 1)
    elif opcode == 3:
        prog[params[0]] = int(input("In?"))
    elif opcode == 4:
        print(value(mode, params, 0))
    elif opcode == 5:
        if value(mode, params, 0) != 0:
            index = value(mode, params, 1)
    elif opcode == 6:
        if value(mode, params, 0) == 0:
            index = value(mode, params, 1)
    elif opcode == 7:
        prog[params[2]] = value(mode, params, 0) < value(mode, params, 1)
    elif opcode == 8:
        prog[params[2]] = value(mode, params, 0) == value(mode, params, 1)

    return index


i = 0
lengths = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}
while True:
    params = list()
    mode = list()

    rev = str(prog[i])[::-1]
    if len(rev) == 1:
        rev = rev[0] + "0"
    opcode = int(rev[1] + rev[0])
    mode = [int(i) for i in rev[2:]]

    if opcode == 99:
        break

    length = lengths[opcode]
    while len(mode) < length:
        mode.append(0)
    for j in range(1, length + 1):
        params.append(prog[i + j])
    i += length + 1

    i = do_op(opcode, mode, params, i)
