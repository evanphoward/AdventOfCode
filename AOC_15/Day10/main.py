inp = "1113122113"
for i in range(50):
    out = ""
    num = inp[0]
    inp = inp[1:] + " "
    times = 1
    for actual in inp:
        if actual != num:
            out += str(times) + num
            times = 1
            num = actual
        else:
            times += 1
    inp = out
    if i == 39:
        print("Part 1:", len(inp))
print("Part 2:", len(inp))
