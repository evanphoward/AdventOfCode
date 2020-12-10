# I did not write most of this file! Credit must go to reddit user /u/i_have_no_biscuits.
# I spent many hours on this and as I understand this code, I will move on

def key_to_key(source):
    sx, sy = source
    visited = set([(sx,sy)])
    queue = [(sx, sy, 0, "")]
    routeinfo = {}

    for (x, y, dist, route) in queue:
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
key_pos = dict()
maps = dict()
x = y = 0
for line in open("input").readlines():
    for ch in line.strip():
        if ch == "@" or (ch.isalpha() and ch.islower()):
            key_pos[ch] = (x, y)
        maze[(x, y)] = ch
        x += 1
    x = 0
    y += 1

for key, mappings in key_pos.items():
    maps[key] = key_to_key(key_pos[key])

info = {('@', frozenset()): 0}
keys = set([k for k in key_pos.keys() if k != '@'])
for _ in range(len(keys)):
    nextinfo = {}
    for item in info:
        curloc, curkeys, curdist = item[0], item[1], info[item]
        for newkey in keys:
            if newkey not in curkeys:
                dist, route = maps[curloc][newkey]
                reachable = all((c in curkeys or c.lower() in curkeys) for c in route)

                if reachable:
                    newdist = curdist + dist
                    newkeys = curkeys.union(set((newkey)))

                    if (newkey, newkeys) not in nextinfo or newdist < nextinfo[(newkey, newkeys)]:
                        nextinfo[(newkey,newkeys)] = newdist
    info = nextinfo

print("Part 1:", min(info.values()))

start_x, start_y = key_pos['@']
maze[(start_x, start_y)] = '#'
maze[(start_x + 1, start_y)] = '#'
maze[(start_x - 1, start_y)] = '#'
maze[(start_x, start_y + 1)] = '#'
maze[(start_x, start_y - 1)] = '#'
maze[(start_x + 1, start_y + 1)] = '1'
maze[(start_x + 1, start_y - 1)] = '2'
maze[(start_x - 1, start_y + 1)] = '3'
maze[(start_x - 1, start_y - 1)] = '4'

for key, mappings in key_pos.items():
    if key != '@':
        maps[key] = key_to_key(key_pos[key])
maps['1'] = key_to_key((start_x + 1, start_y + 1))
maps['2'] = key_to_key((start_x + 1, start_y - 1))
maps['3'] = key_to_key((start_x - 1, start_y + 1))
maps['4'] = key_to_key((start_x - 1, start_y - 1))

info = {(('1','2','3','4'), frozenset()): 0}

for _ in range(len(keys)):
    nextinfo = {}
    for item in info:
        curlocs, curkeys, curdist = item[0], item[1], info[item]

        for newkey in keys:
            if newkey not in curkeys:
                for robot in range(4):
                    if newkey in maps[curlocs[robot]]:
                        dist, route = maps[curlocs[robot]][newkey]
                        reachable = all((c in curkeys or c.lower() in curkeys) for c in route)

                        if reachable:
                            newdist = curdist + dist
                            newkeys = frozenset(curkeys | set((newkey,)))
                            newlocs = list(curlocs)
                            newlocs[robot] = newkey
                            newlocs = tuple(newlocs)

                            if (newlocs, newkeys) not in nextinfo or newdist < nextinfo[(newlocs, newkeys)]:
                                nextinfo[(newlocs, newkeys)] = newdist
    info = nextinfo

print("Part 2:", min(info.values()))
