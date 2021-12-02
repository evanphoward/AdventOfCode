inp = [line.replace(".", "").replace(":", "").strip().split() for line in open("input").readlines()]
num_steps = int(inp[1][5])

t_fun = dict()
i = 3
while i < len(inp):
    state = inp[i][2]
    t_fun[state] = dict()
    t_fun[state][False] = (inp[i + 2][4] == '1', inp[i + 3][6], inp[i + 4][4])
    t_fun[state][True] = (inp[i + 6][4] == '1', inp[i + 7][6], inp[i + 8][4])
    i += 10

rip = 0
tape = [False]
state = inp[0][3]

for _ in range(num_steps):
    sym, move, state = t_fun[state][tape[rip]]
    tape[rip] = sym
    rip += 1 if move == "right" else -1
    if rip == -1:
        rip += 1
        tape.insert(0, False)
    elif rip == len(tape):
        tape.append(False)

print(sum(tape))
