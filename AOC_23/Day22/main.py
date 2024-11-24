from MiscFiles.library import *

def get_points_from_pos(init_pos, final_pos):
    points = set()
    if init_pos[0] != final_pos[0]:
        for i in range(init_pos[0], final_pos[0] + 1):
            points.add((i, init_pos[1], init_pos[2]))
    elif init_pos[1] != final_pos[1]:
        for i in range(init_pos[1], final_pos[1] + 1):
            points.add((init_pos[0], i, init_pos[2]))
    elif init_pos[2] != final_pos[2]:
        for i in range(init_pos[2], final_pos[2] + 1):
            points.add((init_pos[0], init_pos[1], i))
    else:
        points.add((init_pos))
    return points

class Brick:
    def __init__(self, i, points):
        self.points = points
        self.i = i

    def drop(self, settled_blocks):
        while True:
            new_points = {(x[0], x[1], x[2] - 1) for x in self.points}
            if any(x[2] == 0 for x in new_points) or new_points.intersection(settled_blocks):
                break
            self.points = new_points

    def supported(self, all_bricks):
        supported_by = set()
        for brick in all_bricks:
            if brick == self:
                continue
            below_pts = {(x[0], x[1], x[2] - 1) for x in self.points}
            if below_pts.intersection(brick.points):
                supported_by.add(brick)
        return supported_by

    def __lt__(self, other):
        return min(x[2] for x in self.points) < min(x[2] for x in other.points)


bricks = []
for i, line in enumerate(get_input(2023, 22).split("\n")):
    init_pos, final_pos = line.split("~")
    init_pos = tuple(map(int, init_pos.split(",")))
    final_pos = tuple(map(int, final_pos.split(",")))
    bricks.append(Brick(i, get_points_from_pos(init_pos, final_pos)))
bricks.sort()

settled_pts = set()
for brick in bricks:
    brick.drop(settled_pts)
    settled_pts = settled_pts.union(brick.points)

ans = set()
graph = defaultdict(set)
for brick in bricks:
    supported_by = brick.supported(bricks)
    for x in supported_by:
        graph[x].add(brick)
    if len(supported_by) == 1:
        ans.add(list(supported_by)[0])
print("Part 1:", len(bricks) - len(ans))

ans = 0
for brick in bricks:
    indeg = defaultdict(int)
    for t_brick in bricks:
        for in_brick in graph[t_brick]:
            indeg[in_brick] += 1
    q = [brick]
    count = -1
    while len(q) > 0:
        count += 1
        x = q.pop()
        for i in graph[x]:
            indeg[i] -= 1
            if indeg[i] == 0:
                q.append(i)

    ans += count
print("Part 2:", ans)