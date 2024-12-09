from MiscFiles.library import *


inp = list(map(int, get_input(2024, 9).split("\n")[0]))
space = []
id = 0
lens = dict()
blanks = []
id_starts = []

for i in range(len(inp)):
    if i % 2 == 0:
        disk_len = inp[i]
        lens[id] = disk_len
        id_starts.append(len(space))
        for i in range(disk_len):
            space.append(id)
        id += 1
    else:
        free_len = inp[i]
        blanks.append([free_len, len(space)])
        for i in range(free_len):
            space.append(-1)


def defrag_p1(space):
    space = space.copy()
    smallest_blank = inp[0]
    while smallest_blank < len(space):
        if space[-1] != -1:
            space[smallest_blank] = space[-1]
            while space[smallest_blank] != -1:
                smallest_blank += 1
                if smallest_blank == len(space):
                    break
        space = space[:-1]
    return space

def defrag_p2(space):
    space = space.copy()
    for id in range(len(lens) - 1, 0, -1):
        for i, (avail, start) in enumerate(blanks):
            if start >= id_starts[id] or avail < lens[id]:
                continue
            for j in range(lens[id]):
                space[start + j] = id
                space[id_starts[id] + j] = -1
            blanks[i][0] -= lens[id]
            blanks[i][1] += lens[id]
            break
    return space


def checksum(space):
    ans = 0
    for i, id in enumerate(space):
        if id == -1:
            continue
        ans += (i * id)
    return ans

print("Part 1:", checksum(defrag_p1(space)))
print("Part 2:", checksum(defrag_p2(space)))
