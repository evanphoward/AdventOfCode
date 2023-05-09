from functools import lru_cache
from math import prod

inp = open("input").read().strip().split("\n")

blueprints = []
for x in inp:
    x = x.split()
    o = int(x[6])
    c = int(x[12])
    ob = (int(x[18]), int(x[21]))
    g = (int(x[27]), int(x[30]))
    blueprints.append((o, c, ob, g))


@lru_cache(maxsize=None)
def num_geodes(o_cost, c_cost, ob_cost, g_cost, t_left, ore_robots, clay_robots, ob_robots, g_robots, ore, clay, ob,
               geodes):
    if t_left == 0:
        return geodes
    if ore >= g_cost[0] and ob >= g_cost[1]:
        return num_geodes(o_cost, c_cost, ob_cost, g_cost, t_left - 1, ore_robots, clay_robots, ob_robots,
                          g_robots + 1, ore - g_cost[0] + ore_robots, clay + clay_robots, ob - g_cost[1] + ob_robots,
                          geodes + g_robots)
    if ob_robots < g_cost[1] and ore >= ob_cost[0] and clay >= ob_cost[1]:
        return num_geodes(o_cost, c_cost, ob_cost, g_cost, t_left - 1, ore_robots, clay_robots, ob_robots + 1, g_robots,
                       ore - ob_cost[0] + ore_robots, clay - ob_cost[1] + clay_robots, ob + ob_robots,
                       geodes + g_robots)
    options = []
    if clay_robots < ob_cost[1] and ore >= c_cost:
        options.append(num_geodes(o_cost, c_cost, ob_cost, g_cost, t_left - 1, ore_robots, clay_robots + 1, ob_robots, g_robots,
                       ore - c_cost + ore_robots, clay + clay_robots, ob + ob_robots, geodes + g_robots))
    if ore_robots < max(c_cost, ob_cost[0], g_cost[0]) and ore >= o_cost:
        options.append(num_geodes(o_cost, c_cost, ob_cost, g_cost, t_left - 1, ore_robots + 1, clay_robots, ob_robots, g_robots,
                       ore - o_cost + ore_robots, clay + clay_robots, ob + ob_robots, geodes + g_robots))
    options.append(num_geodes(o_cost, c_cost, ob_cost, g_cost, t_left - 1, ore_robots, clay_robots, ob_robots, g_robots,
                   ore + ore_robots, clay + clay_robots, ob + ob_robots, geodes + g_robots))

    return max(options)


print("Part 1:", sum([(i + 1) * num_geodes(o, c, ob, g, 24, 1, 0, 0, 0, 0, 0, 0, 0) for i, (o, c, ob, g) in enumerate(blueprints)]))
print("Part 2:", prod(num_geodes(o, c, ob, g, 32, 1, 0, 0, 0, 0, 0, 0, 0) for (o, c, ob, g) in blueprints[:3]))
