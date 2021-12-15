import heapq
STARTING_POS = (0, 0)
WIDTH = len(open("input").readlines())
GOAL = (WIDTH - 1, WIDTH - 1)


def parse_grid(p1):
    grid = dict()
    inp = open("input").readlines()
    for r, row in enumerate(inp):
        for c, cell in enumerate(row.strip()):
            grid[r, c] = int(cell)
    if p1:
        return grid
    grid_2 = dict()
    for r1 in range(5):
        for c1 in range(5):
            for r2 in range(WIDTH):
                for c2 in range(WIDTH):
                    grid_2[(r1 * WIDTH) + r2, (c1 * WIDTH) + c2] = (grid[r2, c2] + r1 + c1)
                    while grid_2[(r1 * WIDTH) + r2, (c1 * WIDTH) + c2] > 9:
                        grid_2[(r1 * WIDTH) + r2, (c1 * WIDTH) + c2] -= 9
    return grid_2


def dijkstra(maze, goal):
    heap = [(0, STARTING_POS)]
    distances = {pos: -1 for pos in maze}
    distances[STARTING_POS] = 0
    visited = set()
    while heap:
        risk, pos = heapq.heappop(heap)
        if pos in visited:
            continue
        if pos == goal:
            return risk
        visited.add(pos)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos not in maze or new_pos in visited:
                continue
            if distances[new_pos] == -1 or risk + maze[new_pos] < distances[new_pos]:
                distances[new_pos] = risk + maze[new_pos]
            heapq.heappush(heap, (distances[new_pos], new_pos))
    return -1


print("Part 1:", dijkstra(parse_grid(True), (WIDTH - 1, WIDTH - 1)))
print("Part 2:", dijkstra(parse_grid(False), (WIDTH * 5 - 1, WIDTH * 5 - 1)))
