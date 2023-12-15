def process(inp, ins):
    op, arg1, arg2, out = ins
    inp = list(inp)
    if op == "addr":
        inp[out] = inp[arg1] + inp[arg2]
    elif op == "addi":
        inp[out] = inp[arg1] + arg2
    elif op == "mulr":
        inp[out] = inp[arg1] * inp[arg2]
    elif op == "muli":
        inp[out] = inp[arg1] * arg2
    elif op == "banr":
        inp[out] = inp[arg1] & inp[arg2]
    elif op == "bani":
        inp[out] = inp[arg1] & arg2
    elif op == "borr":
        inp[out] = inp[arg1] | inp[arg2]
    elif op == "bori":
        inp[out] = inp[arg1] | arg2
    elif op == "setr":
        inp[out] = inp[arg1]
    elif op == "seti":
        inp[out] = arg1
    elif op == "gtir":
        inp[out] = int(arg1 > inp[arg2])
    elif op == "gtri":
        inp[out] = int(inp[arg1] > arg2)
    elif op == "gtrr":
        inp[out] = int(inp[arg1] > inp[arg2])
    elif op == "eqir":
        inp[out] = int(arg1 == inp[arg2])
    elif op == "eqri":
        inp[out] = int(inp[arg1] == arg2)
    elif op == "eqrr":
        inp[out] = int(inp[arg1] == inp[arg2])
    else:
        assert False
    return inp


def run(regs, inp):
    ip_index, prog = int(inp[0].split()[1]), inp[1:]
    prog = [[line.split()[0]] + list(map(int, line.split()[1:])) for line in prog]
    ip = 0
    while ip < len(prog):
        # Based on looking at the raw program, this converts the loop that sum up all factors of a number and adds that
        # sum to regs[0] corresponding to instructions 3 through 15 to python
        if ip == 3 and regs[5] != 0:
            for i in range(1, regs[5] + 1):
                if regs[5] % i == 0:
                    regs[0] += i
            regs[1] = regs[5]
            ip = 16
            regs[ip_index] = 16
        regs = process(regs, prog[ip])
        ip = regs[ip_index]
        ip += 1
        regs[ip_index] = ip
    return regs[0]


print("Part 1:", run([0, 0, 0, 0, 0, 0], open("input").read().split("\n")))
print("Part 2:", run([1, 0, 0, 0, 0, 0], open("input").read().split("\n")))
