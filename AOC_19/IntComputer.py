class IntProcess:
    def __init__(self, program):
        self.prog = [int(i) for i in program.readline().split(",")]
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
        lengths = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
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

            length = lengths[opcode]
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