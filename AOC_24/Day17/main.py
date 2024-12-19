from MiscFiles.library import *

def get_value(operand, combo, registers):
    if combo:
        if 0 <= operand <= 3:
            return operand
        if 4 <= operand <= 6:
            return registers[operand - 4]
        if operand >= 7:
            assert False
    else:
        return operand

def run_program(a):
    registers = [a, 0, 0]
    ip = 0
    out = []
    while ip < len(program):
        if program[ip] == 0:
            registers[0] //= (2 ** get_value(program[ip + 1], True, registers))
        elif program[ip] == 1:
            registers[1] ^= get_value(program[ip + 1], False, registers)
        elif program[ip] == 2:
            registers[1] = get_value(program[ip + 1], True, registers) % 8
        elif program[ip] == 3:
            if registers[0] != 0:
                ip = (get_value(program[ip + 1], False, registers)) - 2
        elif program[ip] == 4:
            registers[1] ^= registers[2]
        elif program[ip] == 5:
            out.append(get_value(program[ip + 1], True, registers) % 8)
        elif program[ip] == 6:
            registers[1] = registers[0] // (2 ** get_value(program[ip + 1], True, registers))
        elif program[ip] == 7:
            registers[2] = registers[0] // (2 ** get_value(program[ip + 1], True, registers))
        ip += 2
    return out

def find_a(a, i):
    if run_program(a) == program:
        print("Part 2:", a)
    if run_program(a) == program[-i:] or not i:
        for n in range(8):
            find_a(8 * a + n, i + 1)


inp = get_input(2024, 17).split("\n\n")
program = list(map(int,inp[1].split()[1].split(',')))
p1_a = int(inp[0].split('\n')[0].split()[-1])

print("Part 1:", ','.join(map(str,run_program(p1_a))))
find_a(0, 0)
