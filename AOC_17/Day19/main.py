from MiscFiles.library import *


def step(pos, dir):
    global letters_seen, grid, steps
    r, c = pos
    dr, dc = DIRS[dir]
    r += dr
    c += dc
    steps += 1
    if (r, c) not in grid or grid[r, c] == ' ':
        steps -= 1
        return False, False
    if grid[r, c].isalpha():
        letters_seen += grid[r, c]
    if grid[r, c] == '+':
        if dir == 0 or dir == 2:
            if (r, c + 1) in grid and grid[(r, c + 1)] != ' ':
                dir = 1
            else:
                dir = 3
        elif dir == 1 or dir == 3:
            if (r + 1, c) in grid and grid[(r + 1, c)] != ' ':
                dir = 0
            else:
                dir = 2
    return (r, c), dir


grid, nr, nc = get_grid(get_input(2017, 19))
STARTING_POS = (-1, -1)
for c in range(nc):
    if grid[0, c] == '|':
        STARTING_POS = (-1, c)

letters_seen = ''
steps = 0
pos = STARTING_POS
dir = 0
while pos:
    pos, dir = step(pos, dir)

print("Part 1:", letters_seen)
print("Part 2:", steps)
