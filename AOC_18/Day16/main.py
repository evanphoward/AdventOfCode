def process(inp, ins):
    op, arg1, arg2, out = ins
    inp = list(inp)
    # addr
    if op == 0:
        inp[out] = inp[arg1] + inp[arg2]
    # addi
    elif op == 1:
        inp[out] = inp[arg1] + arg2
    # mulr
    elif op == 2:
        inp[out] = inp[arg1] * inp[arg2]
    # muli
    elif op == 3:
        inp[out] = inp[arg1] * arg2
    # banr
    elif op == 4:
        inp[out] = inp[arg1] & inp[arg2]
    # bani
    elif op == 5:
        inp[out] = inp[arg1] & arg2
    # borr
    elif op == 6:
        inp[out] = inp[arg1] | inp[arg2]
    # bori
    elif op == 7:
        inp[out] = inp[arg1] | arg2
    # setr
    elif op == 8:
        inp[out] = inp[arg1]
    # seti
    elif op == 9:
        inp[out] = arg1
    # gtir
    elif op == 10:
        inp[out] = int(arg1 > inp[arg2])
    # gtri
    elif op == 11:
        inp[out] = int(inp[arg1] > arg2)
    # gtrr
    elif op == 12:
        inp[out] = int(inp[arg1] > inp[arg2])
    # eqir
    elif op == 13:
        inp[out] = int(arg1 == inp[arg2])
    # eqri
    elif op == 14:
        inp[out] = int(inp[arg1] == arg2)
    # eqrr
    elif op == 15:
        inp[out] = int(inp[arg1] == inp[arg2])
    else:
        assert False
    return inp


raw_samples, prog = open("input").read().strip().split("\n\n\n\n")
prog = [map(int, line.split()) for line in prog.strip().split("\n")]

samples = []
for sample in raw_samples.split("\n\n"):
    i, op, o = sample.split("\n")
    i = eval(i[8:])
    o = eval(o[8:])
    op = map(int, op.split())
    samples.append((i, op, o))


ans = 0
options = {i: set(range(16)) for i in range(16)}
for i, ins, o in samples:
    matches = set()
    for opcode in range(16):
        dummy_op, arg1, arg2, out = ins
        if process(i, (opcode, arg1, arg2, out)) == o:
            matches.add(opcode)
    options[ins[0]] &= matches
    if len(matches) >= 3:
        ans += 1
print("Part 1:", ans)

opcode_assn = dict()
while len(opcode_assn) < 16:
    for i in range(16):
        if len(options[i]) == 1:
            assn = list(options[i])[0]
            opcode_assn[i] = assn
            for j in range(16):
                if i == j or assn not in options[j]:
                    continue
                options[j].remove(assn)

regs = [0, 0, 0, 0]
for line in prog:
    dummy_op, arg1, arg2, out = line
    regs = process(regs, (opcode_assn[dummy_op], arg1, arg2, out))
print("Part 2:", regs[0])
