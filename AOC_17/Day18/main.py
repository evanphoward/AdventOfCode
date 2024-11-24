from MiscFiles.library import *

class Program:
    def __init__(self, id=None):
        self.registers = defaultdict(int)
        self.id = id
        if id:
            self.registers['p'] = id
        self.pos = 0
        self.last_sound = -1
        self.num_sent = 0

    def value(self, vl):
        try:
            return int(vl)
        except ValueError:
            return self.registers[vl]

    def step(self):
        global buffers, inp
        if self.pos < 0 or self.pos >= len(inp):
            return
        x = inp[self.pos].split()
        instruction = x[0]
        if instruction == 'snd':
            self.num_sent += 1
            self.last_sound = self.value(x[1])
            if self.id is not None:
                buffers[(self.id + 1) % 2].append(self.last_sound)
        elif instruction == 'set':
            self.registers[x[1]] = self.value(x[2])
        elif instruction == 'add':
            self.registers[x[1]] += self.value(x[2])
        elif instruction == 'mul':
            self.registers[x[1]] *= self.value(x[2])
        elif instruction == 'mod':
            self.registers[x[1]] %= self.value(x[2])
        elif instruction == 'rcv':
            if self.id is not None:
                if len(buffers[self.id]) > 0:
                    self.registers[x[1]] = buffers[self.id].popleft()
                else:
                    self.pos -= 1
            else:
                return self.last_sound
        elif instruction == 'jgz':
            if (self.value(x[1])) > 0:
                self.pos += self.value(x[2]) - 1
        self.pos += 1


inp = get_input(2017, 18).split("\n")
program = Program()
while True:
    last_sound = program.step()
    if last_sound:
        print("Part 1:", last_sound)
        break

program_0 = Program(0)
program_1 = Program(1)
buffers = [deque(), deque()]
prev_pos = (-1, -1)
while (program_0.pos, program_1.pos) != prev_pos:
    prev_pos = (program_0.pos, program_1.pos)
    program_0.step()
    program_1.step()

print("Part 2:", program_1.num_sent)