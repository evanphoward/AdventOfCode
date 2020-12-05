class IntProcess:
    def __init__(self):
        self.prog = [int(i) for i in open("input").readline().split(",")]
        for i in range(10000000):
            self.prog.append(0)
        self.ip = 0
        self.rb = 0

    def value(self, mode, params, index):
        if mode[index] == 0:
            return self.prog[params[index]]
        if mode[index] == 1:
            return params[index]
        if mode[index] == 2:
            return self.prog[self.rb + params[index]]
        return self.prog[params[index]] if mode[index] == 0 else params[index]

    def do_op(self, opcode, mode, params):
        first_value = self.value(mode, params, 0)
        if len(params) > 2:
            second_value = self.value(mode, params, 1)
        if opcode == 1:
            self.prog[params[2] + (mode[2] // 2 * self.rb)] = first_value + second_value
        elif opcode == 2:
            self.prog[params[2] + (mode[2] // 2 * self.rb)] = first_value * second_value
        elif opcode == 3:
            self.prog[params[0] + (mode[0] // 2 * self.rb)] = int(input("In?"))
        elif opcode == 4:
            print(first_value)
        elif opcode == 5:
            if first_value != 0:
                self.ip = self.value(mode, params, 1)
        elif opcode == 6:
            if first_value == 0:
                self.ip = self.value(mode, params, 1)
        elif opcode == 7:
            self.prog[params[2] + (mode[2] // 2 * self.rb)] = int(first_value < second_value)
        elif opcode == 8:
            self.prog[params[2] + (mode[2] // 2 * self.rb)] = int(first_value == second_value)
        elif opcode == 9:
            self.rb += first_value

    def run(self, inp=False):
        inp_i = 0
        out = list()
        while True:
            params = list()

            rev = str(self.prog[self.ip])[::-1]
            if len(rev) == 1:
                rev = rev[0] + "0"
            opcode = int(rev[1] + rev[0])
            mode = [int(i) for i in rev[2:]]

            if opcode == 99:
                self.ip = -1
                return out

            length = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}[opcode]
            while len(mode) < length:
                mode.append(0)
            for j in range(1, length + 1):
                params.append(self.prog[self.ip + j])
            self.ip += length + 1

            if inp and opcode == 3:
                if inp_i == len(inp):
                    self.ip -= 2
                    return out
                else:
                    self.prog[params[0] + (mode[0] // 2 * self.rb)] = inp[inp_i]
                    inp_i += 1
                    continue
            if opcode == 4:
                out.append(self.value(mode, params, 0))
                continue

            self.do_op(opcode, mode, params)


robot = IntProcess()
panels = {}
x = y = 0
dx = 0
dy = 1
total_painted = set()
while robot.ip != -1:
    if (x, y) not in panels.keys():
        panels[(x, y)] = 0
    color = panels[(x, y)]
    paint, turn = robot.run([color])
    panels[(x, y)] = paint
    if paint == 1:
        total_painted.add((x, y))
    if dx == 0:
        dx = 1 if (dy == 1 and turn == 1) or (dy == -1 and turn == 0) else -1
        dy = 0
    else:
        dy = 1 if (dx == 1 and turn == 0) or (dx == -1 and turn == 1) else -1
        dx = 0
    x += dx
    y += dy

print("Part 1:", len(total_painted))


robot = IntProcess()
panels = {(0, 0) : 1}
x = y = 0
dx = 0
dy = 1
while robot.ip != -1:
    if (x, y) not in panels.keys():
        panels[(x, y)] = 0
    color = panels[(x, y)]
    paint, turn = robot.run([color])
    panels[(x, y)] = paint
    if dx == 0:
        dx = 1 if (dy == 1 and turn == 1) or (dy == -1 and turn == 0) else -1
        dy = 0
    else:
        dy = 1 if (dx == 1 and turn == 0) or (dx == -1 and turn == 1) else -1
        dx = 0
    x += dx
    y += dy

print("Part 2:")
for y in reversed(range(min([x[0][1] for x in panels.items()]), max([x[0][1] for x in panels.items()]) + 1)):
    row = ""
    for x in range(min([x[0][0] for x in panels.items()]), max([x[0][0] for x in panels.items()]) + 1):
        if (x, y) not in panels:
            row = row + " "
            continue
        row = row + ("#" if panels[(x, y)] == 1 else " ")
    print(row)
