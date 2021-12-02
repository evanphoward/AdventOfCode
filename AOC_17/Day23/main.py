def value(vl):
    try:
        return int(vl)
    except ValueError:
        return registers[vl]


def compute(line):
    global registers, mul
    if line[0] == "set":
        registers[line[1]] = value(line[2])
    elif line[0] == "sub":
        registers[line[1]] -= value(line[2])
    elif line[0] == "mul":
        mul += 1
        registers[line[1]] *= value(line[2])
    elif line[0] == "jnz":
        if value(line[1]) != 0:
            return value(line[2])
    return 1


mul = rip = 0
registers = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
prog = [line.strip().split() for line in open("input").readlines()]

while rip < len(prog):
    rip += compute(prog[rip])

print("Part 1:", mul)

# Code checks every seventeenth number for primality in certain range
# Just gotta stare at the "assembly"!
h = 0
for x in range(107900, 124900 + 1, 17):
    for i in range(2, x):
        if x % i == 0:
            h += 1
            break
print("Part 2:", h)
