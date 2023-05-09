from collections import deque
from collections import defaultdict

inp = open("input").read().strip().split("\n")
valve_rates = dict()
valve_neighbors = dict()
valve_edges = [[len(inp) + 1] * len(inp) for _ in range(len(inp))]
N = 0
valve_ids = dict()
for x in inp:
    x = x.split()
    valve = x[1]
    if valve not in valve_ids:
        valve_ids[valve] = N
        N += 1
    valve_rates[valve_ids[valve]] = int(x[4][5:-1])
    for neighbor in x[9:]:
        if neighbor.endswith(","):
            neighbor = neighbor[:-1]
        if neighbor not in valve_ids:
            valve_ids[neighbor] = N
            N += 1
        valve_edges[valve_ids[valve]][valve_ids[neighbor]] = min(valve_edges[valve_ids[valve]][valve_ids[neighbor]], 1)

for i in range(N):
    for j in range(N):
        for k in range(N):
            valve_edges[j][k] = min(valve_edges[j][k], valve_edges[j][i] + valve_edges[i][k])

non_zero_valves = [valve_ids['AA']] + [valve for (valve, rate) in valve_rates.items() if rate > 0]
num_non_zero = len(non_zero_valves)


def run(time):
    queue = deque()
    best = defaultdict(lambda: -1)

    aa = non_zero_valves.index(valve_ids['AA'])

    def add(i, added, v, t):
        if t >= 0 and (best[(i, added, t)] < v):
            best[(i, added, t)] = v
            queue.append((i, added, v, t))

    add(aa, 0, 0, time)
    while queue:
        i, added, v, t = queue.popleft()
        if (added & (1 << i)) == 0 and t >= 1:
            flow_here = (t - 1) * valve_rates[non_zero_valves[i]]
            add(i, added | (1 << i), v + flow_here, t - 1)

        for j in range(num_non_zero):
            t_move = valve_edges[non_zero_valves[i]][non_zero_valves[j]]
            if t_move <= t:
                add(j, added, v, t - t_move)

    return best


print("Part 1:", max(run(30).values()))

best2 = run(26)
# best => (end_node, mask_turned, time_left) => max_flow
table = [0] * (1 << num_non_zero)
for (i, added, t), vmax in best2.items():
    table[added] = max(table[added], vmax)

ret = 0
for mask in range(1 << num_non_zero):
    mask3 = ((1 << num_non_zero) - 1) ^ mask
    ret = max(ret, table[mask3])
    mask2 = mask
    while mask2 > 0:
        ret = max(ret, table[mask3] + table[mask2])
        mask2 = (mask2 - 1) & mask

print("Part 2:", ret)

