from MiscFiles.library import *

def one_dance(programs):
    for x in inp:
        if x[0] == 's':
            num = int(x[1:])
            new_head = (LENGTH - num) % 16
            programs = programs[new_head:] + programs[:new_head]
        elif x[0] == 'x':
            fst, snd = map(int, x[1:].split('/'))
            tmp = programs[fst]
            programs[fst] = programs[snd]
            programs[snd] = tmp
        elif x[0] == 'p':
            for i in range(LENGTH):
                if programs[i] == x[1]:
                    fst = i
                if programs[i] == x[3]:
                    snd = i
            tmp = programs[fst]
            programs[fst] = programs[snd]
            programs[snd] = tmp
    return programs

LENGTH = 16
inp = get_input(2017, 16).split(",")
programs = [chr(ord('a') + i) for i in range(16)]
prev = dict()
head = programs[0]
for i in range(1, 10000000000):
    programs = one_dance(programs)
    frozen_programs = ''.join(programs)
    if i == 1:
        print("Part 1:", ''.join(programs))
    if frozen_programs in prev:
        if (1000000000 - i) % (i - prev[frozen_programs]) == 0:
            print("Part 2:", frozen_programs)
            break
    prev[frozen_programs] = i
