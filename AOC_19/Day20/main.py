# It may work theoretically, but it is too slow for the second part
# Maybe one day I will fix it
import itertools


def display():
    for y in range(max_y + 2):
        row = ""
        for x in range(max_x + 2):
            if (x, y) in maze.keys():
                row = row + maze[(x, y)]
        print(row)


# Create maze dictionary (x, y) -> symbol
maze = dict()
x = y = 0
for line in open("input").readlines():
    for ch in line:
        if ch == "\n":
            continue
        maze[(x, y)] = ch
        x += 1
    x = 0
    y += 1

max_y = max(pos[1] for pos in maze.keys()) - 1
max_x = max(pos[0] for pos in maze.keys()) - 1
display()

# Get position of portal (x, y) -> "AA" where (x,y) is corridor next to portal
# I.E. AA..# it'd be the . next to AA
start = (0, 0)
portal_pos = dict()
for y in range(2, max_y):
    for x in range(2, max_x):
        if maze[(x, y)] == ".":
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if maze[(x + dx, y + dy)].isalpha():
                    first_pos = (x + dx, y + dy)
                    second_pos = (x + dx + dx, y + dy + dy)
                    if first_pos[0] > second_pos[0] or first_pos[1] > second_pos[1]:
                        first_pos = second_pos
                        second_pos = (x + dx, y + dy)
                    portal_pos[(x, y)] = str(maze[first_pos] + maze[second_pos])
                    if portal_pos[(x, y)] == "AA":
                        start = (x, y)

# Map portal coordinates the to corresponding portal coordinates (x, y) -> (x, y)
portal_path = dict()
for portal_1, portal_2 in itertools.permutations(portal_pos.items(), 2):
    if portal_1[1] == portal_2[1]:
        portal_path[portal_1[0]] = portal_2[0]
        portal_path[portal_2[0]] = portal_1[0]


# Dijkstra's
visited = set()
info = {start: 0}
curloc = start
done = False
while not done:
    curdist = info[curloc]
    x, y = curloc
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x = x + dx
        new_y = y + dy
        if (new_x, new_y) not in visited and maze[(new_x, new_y)] != "#":
            newdist = curdist + 1
            if maze[(new_x, new_y)].isalpha():
                if (x, y) in portal_path:
                    newloc = portal_path[(x, y)]
                else:
                    continue
            else:
                newloc = (new_x, new_y)

            if newloc in portal_pos and portal_pos[newloc] == "ZZ":
                print(newdist)
                done = True
                break
            if newloc not in info or newdist < info[newloc]:
                info[newloc] = newdist
    visited.add(curloc)
    curloc = min(info, key=lambda x: float("inf") if x in visited else info[x])

visited = set()
info = {(start, 0): 0}
curloc = start
curlevel = 0
done = False
while not done:
    curdist = info[(curloc, curlevel)]
    x, y = curloc
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x = x + dx
        new_y = y + dy
        newloc = (new_x, new_y)
        if newloc in portal_pos and portal_pos[newloc] == "ZZ" and curlevel == 0:
            print(newdist)
            exit()
        if (newloc, curlevel) not in visited and maze[(new_x, new_y)] != "#":
            newdist = curdist + 1
            newlevel = curlevel
            if maze[(new_x, new_y)].isalpha():
                if (x, y) in portal_path:
                    if x == 2 or x == max_x - 1 or y == 2 or y == max_y - 1:
                        if curlevel == 0:
                            continue
                        newlevel -= 1
                    else:
                        if curlevel > len(portal_pos) / 2:
                            continue
                        newlevel += 1
                    newloc = portal_path[(x, y)]
                else:
                    continue

            if (newloc, newlevel) not in info or newdist < info[(newloc, newlevel)]:
                info[(newloc, newlevel)] = newdist
    visited.add((curloc, curlevel))
    curloc, curlevel = min(info, key=lambda x: float("inf") if x in visited else info[x] + (newlevel + 1) * max_x / 2)
