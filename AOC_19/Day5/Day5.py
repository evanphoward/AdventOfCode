input = [int(i) for i in open("input").readline().split(",")]

i = 0
mode = 0
while True:
    opcode = str(input[i])[::-1]
    if len(opcode) == 1:
        opcode = opcode[0] + "0"
    instruc = int(opcode[1]+opcode[0])
    opcode = opcode[2:]

    for p in opcode:

    # if input[i] == 1:
    #     input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
    # elif input[i] == 2:
    #     input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
    i += 4
    print(opcode, instruc)
print(input[0])