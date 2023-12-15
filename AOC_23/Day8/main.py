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

cur = 'AAA'
ans = 0
while cur != 'ZZZ':
    if lr[ans % len(lr)] == 'L':
        cur = nodes[cur][0]
    else:
        cur = nodes[cur][1]
    ans += 1

print("Part 1:", ans)

ans = []
cur = list(filter(lambda x: x.endswith('A'), list(nodes.keys())))
for c in cur:
    ans_c = 0
    while not c.endswith('Z'):
        if lr[ans_c % len(lr)] == 'L':
            c = nodes[c][0]
        else:
            c = nodes[c][1]
        ans_c += 1
    ans.append(ans_c)

print("Part 2:", reduce(lambda x, y: (x*y)//math.gcd(x, y), ans))

