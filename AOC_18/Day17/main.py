from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

s = open("input").read().strip()
s = s.split("\n")

grid = defaultdict(lambda : '.')
min_y, max_y = 0, 0
for wall in s:
    if wall[0] == "x":
        wall = wall.split(", y=")
        wall_x = int(wall[0][2:])
        wall_ys = [int(x) for x in wall[1].split("..")]
        min_y = min(min_y, wall_ys[0])
        max_y = max(max_y, wall_ys[1])
        for y in range(wall_ys[0], wall_ys[1] + 1):
            grid[(wall_x, y)] = "#"
    else:
        wall = wall.split(", x=")
        wall_y = int(wall[0][2:])
        wall_xs = [int(x) for x in wall[1].split("..")]
        for x in range(wall_xs[0], wall_xs[1] + 1):
            grid[(x, wall_y)] = "#"


SAND = "."
WALL = "#"
WATER = "~"
FLOW = "|"
VOID = " "

def fill(x, y, direction):
    if grid[(x, y)] == FLOW:
        fill(x + direction, y, direction)
        grid[(x, y)] = WATER

def flow(x, y, direction):
    global grid
    if y > max_y:
        return True
    elt = grid[(x, y)]
    if elt != SAND:
        return elt != WALL and elt != WATER

    grid[(x, y)] = FLOW

    leaks = flow(x, y + 1, 0)
    if leaks:
        return True

    leaks_left = direction in (-1, 0) and flow(x - 1, y, -1)
    leaks_right = direction in (0, 1) and flow(x + 1, y, 1)
    leaks = leaks_left or leaks_right
    if leaks:
        return True

    if direction == 0:
        fill(x, y, -1)
        fill(x + 1, y, 1)

    return False


flow(500, 0, 0)
ans = 0
for elt in grid.values():
    if elt not in ("#", "."):
        ans += 1
print(ans - min_y - 1)



