from AOC_19.IntComputer import IntProcess
directions = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
nodes = dict()


def fill_maze(cur_node, starting_robot):
    global goal, nodes
    visited = set()
    nodes = {cur_node: [0, starting_robot]}
    while any(node not in visited for node in nodes.keys()):
        for i in range(1, 5):
            cur_robot = nodes[cur_node][1].clone()
            status = cur_robot.run([i])[0]
            new_x = cur_node[0] + directions[i][0]
            new_y = cur_node[1] + directions[i][1]
            if status == 1 or status == 2:
                if (new_x, new_y) in nodes.keys():
                    nodes[(new_x, new_y)][0] = min([nodes[(new_x, new_y)][0], nodes[cur_node][0] + 1])
                else:
                    nodes[(new_x, new_y)] = [nodes[cur_node][0] + 1, cur_robot]
            if status == 2:
                goal = (new_x, new_y)
        visited.add(cur_node)

        min_dist = float('inf')
        for node in nodes.keys():
            if node not in visited and nodes[node][0] < min_dist:
                min_dist = nodes[node][0]
                cur_node = node


fill_maze((0, 0), IntProcess(open("input")))
# For fun: prints the maze
for y in reversed(range(-19, 22)):
    row = ""
    for x in range(-21, 20):
        if (x, y) in nodes.keys():
            if (x, y) == goal:
                row = row + "O"
            elif (x, y) == (0, 0):
                row = row + "D"
            else:
                row = row + "."
        else:
            row = row + "#"
    print(row)
print("Part 1:", nodes[goal][0])
fill_maze(goal, nodes[goal][1])
print("Part 2:", max([node[0] for node in nodes.values()]))


