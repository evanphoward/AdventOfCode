from functools import reduce

inp = open("input").read().split("\n\n")
seeds = [int(x) for x in inp[0].split()[1:]]

inp = [[y.split() for y in x.split("\n")][1:] for x in inp[1:]]
maps = ["".join("x + (" + gs + " - " + ss + ") if " + ss + " <= x < " + ss + " + " + l + " else (" for gs, ss, l in map_ranges) + \
                "x" + (")" * len(map_ranges)) for map_ranges in inp]
lookup = lambda x: reduce(lambda value, mapping: eval(mapping, {'x': value}), maps, x)

print("Part 1:", min(map(lookup, seeds)))

def find_min_range(min_value, length, precision):
    locations = {seed: lookup(seed) for seed in range(min_value, min_value + length, precision)}
    min_seed = min(locations, key=locations.get)
    if precision == 1:
        return locations[min_seed]
    new_min = max(min_seed - length // 20, min_value)
    new_length = min(length // 10, min_value + length - new_min)
    return find_min_range(new_min, new_length, precision // 10)


print("Part 2:", min(find_min_range(seeds[i], seeds[i + 1], 1000000) for i in range(0, len(seeds), 2)))