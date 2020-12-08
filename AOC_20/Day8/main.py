prog = [[line.strip().split(" ")[0], int(line.strip().split(" ")[1])] for line in open("input").readlines()]

ip = 0
acc = 0
seen = set()
while ip <= len(prog):
    if ip in seen:
        print("Part 1:", acc)
        break
    seen.add(ip)
    if prog[ip][0] == "nop":
        ip += 1
        continue
    if prog[ip][0] == "acc":
        acc += prog[ip][1]
        ip += 1
        continue
    if prog[ip][0] == "jmp":
        ip += prog[ip][1]
        continue


for i in [i for i in range(len(prog)) if prog[i][0] == "nop" or prog[i][0] == "jmp"]:
    completed = True
    ip = 0
    seen = set()
    acc = 0
    prog[i][0] = "jmp" if prog[i][0] == "nop" else "nop"
    while ip < len(prog):
        if ip in seen:
            completed = False
            break
        seen.add(ip)
        delta = 1
        if prog[ip][0] == "acc":
            acc += prog[ip][1]
        if prog[ip][0] == "jmp":
            delta = prog[ip][1]
        ip += delta
    if completed:
        print("Part 2:", acc)
        break
    prog[i][0] = "jmp" if prog[i][0] == "nop" else "nop"
