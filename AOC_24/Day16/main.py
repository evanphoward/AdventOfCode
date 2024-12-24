from MiscFiles.library import *

grid, nr, nc = get_grid(get_input(2024, 16))
G = nx.DiGraph()

for r in range(nr):
    for c in range(nc):
        if grid[(r, c)] == 'S':
            grid[(r, c)] = '.'
            STARTING_POS = (r, c, 1)
        elif grid[(r, c)] == 'E':
            grid[(r, c)] = '.'
            for direction in range(4):
                G.add_edge((r, c, direction), "end", weight=0)
        if grid[(r, c)] == '.':
            for direction in range(4):
                G.add_edge((r, c, direction), (r, c, (direction + 1) % 4), weight=1000)
                G.add_edge((r, c, direction), (r, c, (direction - 1) % 4), weight=1000)
                new_pos = (r + DIRS[direction][0], c + DIRS[direction][1])
                if new_pos in grid and grid[new_pos] == '.':
                    G.add_edge((r, c, direction), (new_pos[0], new_pos[1], direction), weight=1)




print("Part 1:", nx.shortest_path_length(G, STARTING_POS, "end", weight="weight"))
good_seats = set()
for path in nx.all_shortest_paths(G, STARTING_POS, "end", weight="weight"):
    for r, c, _ in path[:-1]:
        good_seats.add((r, c))
print("Part 2:", len(good_seats))
