import math
from functools import reduce

lr, nodes_raw = open("input").read().split("\n\n")

nodes = dict()

for node in nodes_raw.split("\n"):
    node = node.split()
    root = node[0]
    left = node[2][1:-1]
    right = node[3][:-1]
    nodes[root] = (left, right)

def steps_to_z(cur):
    steps = 0
    while not cur.endswith('Z'):
        cur = nodes[cur][0 if lr[steps % len(lr)] == 'L' else 1]
        steps += 1
    return steps

print("Part 1:", steps_to_z('AAA'))
print("Part 2:", reduce(lambda x, y: (x*y)//math.gcd(x, y), [steps_to_z(node) for node in filter(lambda x: x.endswith('A'), list(nodes.keys()))]))

