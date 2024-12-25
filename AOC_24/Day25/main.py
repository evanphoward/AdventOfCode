from MiscFiles.library import *

inp = get_input(2024, 25).split("\n\n")
keys = []
locks = []

for thing in inp:
    grid, nr, nc = get_grid(thing)
    if grid[(0, 0)] == '.':
        new_key = []
        for c in range(nc):
            for r in range(nr):
                if grid[(nr - r - 1, c)] == '.':
                    new_key.append(r)
                    break
        keys.append(new_key)
    else:
        new_key = []
        for c in range(nc):
            for r in range(nr):
                if grid[(r, c)] == '.':
                    new_key.append(r)
                    break
        locks.append(new_key)

ans = 0
for key in keys:
    for lock in locks:
        ans += all(key[i] + lock[i] <= 7 for i in range(len(lock)))

print(ans)
