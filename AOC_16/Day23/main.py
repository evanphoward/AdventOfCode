RIP = 0
REGISTERS = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
PROG = [[line.strip().split()[0], line.strip().split()[1:]] for line in open("instructions").readlines()]


def value(vl):
    try:
        return int(vl)
    except ValueError:
        return REGISTERS[vl]


def step(insn, args):
    global RIP, REGISTERS, PROG
    if insn == "cpy":
        REGISTERS[args[1]] = value(args[0])
    elif insn == "inc":
        REGISTERS[args[0]] += 1
    elif insn == "dec":
        REGISTERS[args[0]] -= 1
    elif insn == "jnz":
        if value(args[0]) != 0:
            RIP += (value(args[1]) - 1)
    elif insn == "tgl":
        insn_index = RIP + value(args[0])
        if 0 <= insn_index < len(PROG):
            if len(PROG[insn_index][1]) == 1:
                PROG[insn_index][0] = "dec" if PROG[insn_index][0] == "inc" else "inc"
            else:
                PROG[insn_index][0] = "cpy" if PROG[insn_index][0] == "jnz" else "jnz"
    RIP += 1


while RIP < len(PROG):
    step(PROG[RIP][0], PROG[RIP][1])
print("Part 1:", REGISTERS['a'])

RIP = 0
REGISTERS = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
PROG = [[line.strip().split()[0], line.strip().split()[1:]] for line in open("instructions").readlines()]
while RIP < len(PROG):
    # Hardcoded optimization based on basic inspection of lines 5-10 of input
    if RIP == 4:
        REGISTERS['a'] += REGISTERS['b'] * REGISTERS['d']
        RIP = 10
    step(PROG[RIP][0], PROG[RIP][1])
print("Part 2:", REGISTERS['a'])

