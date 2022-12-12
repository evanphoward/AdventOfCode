class Monkey:
    def __init__(self, items, op, op_num, div_test, true_monkey, false_monkey):
        self.items = items
        self.op = op
        self.op_num = op_num
        self.div_test = div_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect = 0

    def turn(self, p1):
        global monkeys
        for i in self.items:
            self.inspect += 1
            temp_op_num = self.op_num
            if self.op_num == -1:
                temp_op_num = i
            if self.op:
                i *= temp_op_num
            else:
                i += temp_op_num
            i = i % div_factor
            if p1:
                i = i // 3
            if p1:
                p1_monkeys[self.true_monkey if i % self.div_test == 0 else self.false_monkey].items.append(i)
            else:
                monkeys[self.true_monkey if i % self.div_test == 0 else self.false_monkey].items.append(i)
        self.items = []


inp = open("input").read().strip().split("\n\n")
p1_monkeys = []
monkeys = []
div_factor = 1

for monkey in inp:
    monkey = monkey.split("\n")
    t_op_num = monkey[2][25:]
    if t_op_num[0] == 'o':
        t_op_num = -1
    else:
        t_op_num = int(t_op_num)
    div_factor *= int(monkey[3][21:])
    p1_monkeys.append(Monkey([int(x) for x in monkey[1][18:].split(", ")], monkey[2][23] == "*", t_op_num, int(monkey[3][21:]), int(monkey[4][29]), int(monkey[5][30])))
    monkeys.append(Monkey([int(x) for x in monkey[1][18:].split(", ")], monkey[2][23] == "*", t_op_num, int(monkey[3][21:]), int(monkey[4][29]), int(monkey[5][30])))


for _ in range(20):
    for m in p1_monkeys:
        m.turn(True)

inspects = sorted([m.inspect for m in p1_monkeys])
print("Part 1:", inspects[-1] * inspects[-2])

for _ in range(10000):
    for m in monkeys:
        m.turn(False)

inspects = sorted([m.inspect for m in monkeys])
print("Part 2:", inspects[-1] * inspects[-2])




