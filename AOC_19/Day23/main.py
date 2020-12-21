from AOC_19.IntComputer import IntProcess
from collections import deque

cpus = [IntProcess(open("input")) for _ in range(50)]
for i, cpu in enumerate(cpus):
    cpu.run([i])

messages = [deque() for _ in range(50)]
nat = [-1, -1]
first_nat = True
y_values = set()
while True:
    idle = 0
    for i, cpu in enumerate(cpus):
        if messages[i]:
            idle = 0
            x, y = messages[i].popleft()
            out = cpu.run([x, y])
        else:
            idle += 1
            out = cpu.run([-1])
        if out:
            out = [(int(out[i]), int(out[i+1]), int(out[i+2])) for i in range(0, len(out), 3)]
            for message in out:
                if message[0] == 255:
                    if first_nat:
                        print("Part 1:", message[2])
                        first_nat = False
                    nat[0] = message[1]
                    nat[1] = message[2]
                else:
                    messages[message[0]].append((message[1], message[2]))
    if idle == 50:
        if nat[1] in y_values:
            print("Part 2:", nat[1])
            break
        y_values.add(nat[1])
        messages[0].append((nat[0], nat[1]))
