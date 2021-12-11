from collections import deque

inp = deque(map(int, open("input").readline().split()))
nodes = []
node_parents = []
while inp:
    if node_parents:
        if len(nodes[node_parents[-1]][2]) == nodes[node_parents[-1]][0]:
            finished_parent = node_parents.pop()
            for _ in range(nodes[finished_parent][1]):
                nodes[finished_parent][3].append(inp.popleft())
        else:
            nodes[node_parents[-1]][2].append(len(nodes))
            node_parents.append(len(nodes))
            nodes.append((inp.popleft(), inp.popleft(), [], []))
    else:
        node_parents.append(len(nodes))
        nodes.append((inp.popleft(), inp.popleft(), [], []))

print("Part 1:", sum(sum(x[3]) for x in nodes))


def value(i=0):
    node = nodes[i]
    return sum(node[3]) if node[0] == 0 else sum(value(node[2][child - 1]) for child in node[3] if 0 < child <= node[0])


print("Part 2:", value())
