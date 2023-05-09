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


def fill_table(t):
    global valve_rates, valve_edges, non_zero_valves
    q = deque()
    best = defaultdict(lambda: -1)

    def add(i, open_valves, t_left, p):
        if t_left >= 0 and (best[(i, open_valves, t_left)] < p):
            best[(i, open_valves, t_left)] = p
            q.append((i, open_valves, t_left, p))

    add(valve_ids['AA'], 0, t, 0)
    while q:
        cur_valve, open_valves, t_left, p = q.popleft()
        for valve in non_zero_valves:
            move_cost = valve_edges[cur_valve][valve]
            if move_cost <= t_left and open_valves & (1 << valve) == 0:
                new_valves = open_valves | (1 << valve)
                new_t_left = t_left - valve_edges[cur_valve][valve] - 1
                new_p = p + (new_t_left * valve_rates[valve])
                if new_t_left >= 0 and (best[(valve, new_valves, new_t_left)] < new_p):
                    best[(valve, new_valves, new_t_left)] = new_p
                    q.append((valve, new_valves, new_t_left, new_p))
    return best


best_p1 = fill_table(30)
print(max(best_p1.values()))

best_p2 = fill_table(26)
valves_to_pressure = [0] * (1 << max(non_zero_valves))
for (valve, open_valves, t), p in best_p2.items():
    valves_to_pressure[open_valves] = max(valves_to_pressure[open_valves], p)

ans = 0
for valve_perm in range(len(valves_to_pressure)):
    valves_comp = ((1 << len(non_zero_valves)) - 1) ^ valve_perm
    ans = max(ans, valves_to_pressure[valves_comp])
    valve_perm2 = valve_perm
    while valve_perm2 > 0:
        ans = max(ans, valves_to_pressure[valves_comp] + valves_to_pressure[valve_perm2])
        valve_perm2 = (valve_perm2 - 1) & valve_perm

print(ans)
