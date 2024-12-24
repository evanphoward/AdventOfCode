from MiscFiles.library import *

ans = 0

# Lots of different ways to do this, this is probably one of the more inefficient ways.
# But it's the first one I came up with!
def robots_cc(robots):
    g = nx.Graph()
    pos = set((x, y) for x, y, _, _ in robots)
    for p1 in pos:
        x1, y1 = p1
        g.add_node(p1)
        for p2 in pos:
            x2, y2 = p2
            if abs(x2 - x1) + abs(y2 - y1) <= 2:
                g.add_edge(p1, p2)
    return len(list(nx.connected_components(g)))

inp = get_input(2024, 14).split("\n")
width = 101
height = 103
robots = []

for line in inp:
    x, y, vx, vy = map(int, re.match('p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line).groups())
    robots.append([x, y, vx, vy])

for seconds in range(100000):
    for i in range(len(robots)):
        x, y, vx, vy = robots[i]
        x += vx
        y += vy
        if x < 0:
            x += width
        if x >= width:
            x -= width
        if y < 0:
            y += height
        if y >= height:
            y -= height
        robots[i] = [x, y, vx, vy]
    if seconds == 99:
        quadrants = defaultdict(int)
        for r in robots:
            x, y, _, _ = r
            left = x < width // 2
            bottom = y < height // 2
            if x == width // 2 or y == height // 2:
                continue
            if left and not bottom:
                quadrants[0] += 1
            if left and bottom:
                quadrants[1] += 1
            if not left and not bottom:
                quadrants[2] += 1
            if not left and bottom:
                quadrants[3] += 1
        ans = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
        print("Part 1:", ans)
    if robots_cc(robots) < 200:
        print("Part 2:", seconds + 1)
        break
