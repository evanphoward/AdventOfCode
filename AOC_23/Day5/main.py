inp = open("input").read().split("\n\n")
seed_ranges = [int(x) for x in inp[0].split()[1:]]
seeds = set()
for i in range(0, len(seed_ranges), 2):
    seeds.add((seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]))

inp = [[y.split() for y in x.split("\n")][1:] for x in inp[1:]]
maps = []

for i, map_ranges in enumerate(inp):
    cur_map = set()
    for goal_start, source_start, length in map_ranges:
        source_start = int(source_start)
        goal_start = int(goal_start)
        length = int(length)
        cur_map.add((goal_start, source_start, length))
    maps.append(cur_map)


solved = {}
locations = set()
values = seeds
for i, mapping in enumerate(maps):
    new_values = set()
    for value_range_start, value_range_end in values:
        added = False
        for goal_start, source_start, length in mapping:
            offset = goal_start - source_start
            if source_start > value_range_end:
                continue
            elif source_start + length < value_range_start:
                continue
            elif source_start <= value_range_start and source_start + length >= value_range_end:
                added = True
                new_values.add((value_range_start + offset, value_range_end + offset))
            elif value_range_start < source_start and value_range_end <= source_start + length:
                new_values.add((value_range_start, source_start - 1))
                new_values.add((source_start + offset, value_range_end + offset))
            elif source_start < value_range_start and source_start + length <= value_range_end:
                new_values.add((value_range_start + offset, source_start + length + offset))
                new_values.add((source_start + length + 1, value_range_end))
            elif source_start > value_range_start and source_start + length < value_range_end:
                new_values.add((value_range_start, source_start - 1))
                new_values.add((goal_start, goal_start + length))
                new_values.add((source_start + length + 1, value_range_end))
            else:
                print("tricky")
                print(value_range_start, value_range_end, source_start, length)
        if not added:
            new_values.add((value_range_start, value_range_end))
    values = new_values

mins = []
for value in values:
    mins.append(value[0])
print(min(mins))

# for seed in seeds:
#     if (0, seed) in solved:
#         seed = solved[(0, seed)]
#         locations.add(seed)
#         continue
#     to_map = [(0, seed)]
#     for i, mapping in enumerate(maps):
#         if (i + 1, seed) in solved:
#             seed = solved[(i + 1, seed)]
#             break
#         to_map.append((i + 1, seed))
#         new_seed = seed
#         for goal_start, source_start, length in mapping:
#             if source_start <= seed < source_start + length:
#                 seed = (seed - source_start) + goal_start
#                 break
#     for mappee in to_map:
#         solved[mappee] = seed
#     locations.add(seed)
#
# print(min(locations))
