def display():
    for y in range(max(pos[1] for pos in maze.keys()) + 1):
        row = ""
        for x in range(max(pos[0] for pos in maze.keys() if pos[1] == y) + 1):
            row = row + maze[(x, y)]
        print(row)


def portal_to_portal(source):
    sx, sy = source
    visited = set([(sx,sy)])
    queue = [(sx, sy, 0, "")]
    routeinfo = {}

    for (x, y, dist) in queue:
        contents = maze[(x, y)]
        if contents.isalpha() and dist > 0:
            routeinfo[contents] = (dist, route)
            route = route + contents
        visited.add((x,y))

        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            newx, newy = x+d[0], y+d[1]
            if maze[(newx, newy)] != '#' and (newx,newy) not in visited:
                queue.append((newx,newy, dist+1, route))
    return routeinfo


maze = dict()
# Process maze in a smart way
x = y = 0
for line in open("input").readlines():
    for ch in line:
        if ch == "\n":
            continue
        maze[(x, y)] = ch
        x += 1
    x = 0
    y += 1
x = y = 0
portal_pos = dict()
display()

# nodes = {'AA': 0}
# keys = set([k for k in key_pos.keys() if k != '@'])
# while True:
#     nextinfo = {}
#     for item in info:
#         curloc, curkeys, curdist = item[0], item[1], info[item]
#         for newkey in keys:
#             if newkey not in curkeys:
#                 dist, route = maps[curloc][newkey]
#                 reachable = all((c in curkeys or c.lower() in curkeys) for c in route)
#
#                 if reachable:
#                     newdist = curdist + dist
#                     newkeys = curkeys.union(set((newkey)))
#
#                     if (newkey, newkeys) not in nextinfo or newdist < nextinfo[(newkey, newkeys)]:
#                         nextinfo[(newkey,newkeys)] = newdist
#     info = nextinfo