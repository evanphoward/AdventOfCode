RIP = 0
REGISTERS = {'a': 0, 'b': 0}
PROG = [[line.strip().split()[0], line.strip().replace(",","").split()[1:]] for line in open("input").readlines()]


def value(vl):
    try:
        return int(vl)
    except ValueError:
        return REGISTERS[vl]


def step(insn, args):
    global RIP, REGISTERS, PROG
    if insn == "hlf":
        REGISTERS[args[0]] = REGISTERS[args[0]] // 2
    elif insn == "tpl":
        REGISTERS[args[0]] = REGISTERS[args[0]] * 3
    elif insn == "inc":
        REGISTERS[args[0]] += 1
    elif insn == "jmp":
        RIP += (value(args[0]) - 1)
    elif insn == "jie":
        if value(args[0]) % 2 == 0:
            RIP += (value(args[1]) - 1)
    elif insn == "jio":
        if value(args[0]) == 1:
            RIP += (value(args[1]) - 1)
    RIP += 1


while RIP < len(PROG):
    step(PROG[RIP][0], PROG[RIP][1])
print("Part 1:", REGISTERS['b'])

RIP = 0
REGISTERS = {'a': 1, 'b': 0}
while RIP < len(PROG):
    step(PROG[RIP][0], PROG[RIP][1])
print("Part 2:", REGISTERS['b'])
