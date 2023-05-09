from functools import lru_cache
inp = open("input").read().strip().split("\n")

monkeys = dict()
edges = dict()
for x in inp:
    x = x.split()
    m = x[0][:-1]
    if len(x) == 2:
        monkeys[m] = int(x[1])
    else:
        monkeys[m] = x[1:]


@lru_cache(maxsize=None)
def get_vl(m, p2):
    vl = monkeys[m]
    if p2 and m == 'humn':
        return -1
    if isinstance(vl, int):
        return vl
    m1, op, m2 = vl
    if get_vl(m1, p2) == -1 or get_vl(m2, p2) == -1:
        return -1
    return int(eval(str(get_vl(m1, p2)) + op + str(get_vl(m2, p2))))


def right_vl(m, rvl):
    if m == 'humn':
        return int(rvl)

    vl = monkeys[m]
    if isinstance(vl, int):
        return vl

    m1, op, m2 = vl
    m1_vl = get_vl(m1, True)
    m2_vl = get_vl(m2, True)
    if m == "root":
        op = "root"

    rvl_m1_vl = {"root": m2_vl, "+": rvl - m2_vl, "-": rvl + m2_vl, "*": rvl / m2_vl, "/": rvl * m2_vl}
    rvl_m2_vl = {"root": m1_vl, "+": rvl - m1_vl, "-": m1_vl - rvl, "*": rvl / m1_vl, "/": m1_vl / rvl}
    return right_vl(m1 if m1_vl == -1 else m2, rvl_m1_vl[op] if m1_vl == -1 else rvl_m2_vl[op])


print("Part 1:", get_vl("root", False))
print("Part 2:", right_vl("root", 1))



