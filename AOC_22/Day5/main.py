from __future__ import print_function

stacks, proc = open("input").read().split("\n\n")
stacks = stacks.split("\n")
cont_1 = [[] for _ in range((len(stacks[-1]) + 2) // 4)]
cont_2 = [[] for _ in range((len(stacks[-1]) + 2) // 4)]

for i in range(len(stacks) - 1):
    for j in range(len(stacks[i])):
        if (j - 1) % 4 == 0:
            if stacks[i][j] == ' ':
                continue
            cont_1[(j - 1) // 4] = [stacks[i][j]] + cont_1[(j - 1) // 4]
            cont_2[(j - 1) // 4] = [stacks[i][j]] + cont_2[(j - 1) // 4]

for inst in proc.split("\n"):
    inst = inst.split()
    num = int(inst[1])
    start = int(inst[3]) - 1
    end = int(inst[5]) - 1
    for i in range(num):
        moved = cont_1[start][-1]
        cont_1[start] = cont_1[start][:-1]
        cont_1[end] = cont_1[end] + [moved]
    moved = cont_2[start][-num:]
    cont_2[start] = cont_2[start][:-num]
    cont_2[end] = cont_2[end] + moved

print("Part 1:", end=' ')
for stack in cont_1:
    print(stack[-1], end='')
print()
print("Part 2:", end=' ')
for stack in cont_2:
    print(stack[-1], end='')