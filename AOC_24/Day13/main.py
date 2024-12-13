from MiscFiles.library import *


inp = get_input(2024, 13).split("\n\n")
p1, p2 = 0, 0

for machine in inp:
    machine = machine.split('\n')
    a_x, a_y = map(int, re.match('Button A: X\+(\d+), Y\+(\d+)', machine[0]).groups())
    b_x, b_y = map(int, re.match('Button B: X\+(\d+), Y\+(\d+)', machine[1]).groups())
    prize_x, prize_y = map(int, re.match('Prize: X=(\d+), Y=(\d+)', machine[2]).groups())

    opt_p1 = z3.Optimize()
    opt_p2 = z3.Optimize()
    a = z3.Int('a')
    b = z3.Int('b')
    objective = 3 * a + b

    opt_p1.add(a * a_x + b * b_x == prize_x)
    opt_p1.add(a * a_y + b * b_y == prize_y)
    opt_p1.minimize(objective)

    opt_p2.add(a * a_x + b * b_x == (prize_x + 10000000000000))
    opt_p2.add(a * a_y + b * b_y == (prize_y + 10000000000000))
    opt_p2.minimize(objective)

    if opt_p1.check() == z3.sat:
        model = opt_p1.model()
        p1 += 3 * (model[a].as_long()) + (model[b].as_long())
    if opt_p2.check() == z3.sat:
        model = opt_p2.model()
        p2 += 3 * (model[a].as_long()) + (model[b].as_long())

print("Part 1:", p1)
print("Part 2:", p2)
