from MiscFiles.library import *

inp = get_input(2017, 7).split("\n")
ans = 0
discs = dict()

for line in inp:
    line = line.split(' -> ')
    disc = line[0]
    children = []
    if len(line) > 1:
        children = line[1].split(', ')
    disc_name, weight = disc.split(' (')
    weight = int(weight[:-1])
    discs[disc_name] = (weight, children)

parents = dict()
for disc in discs:
    _, children = discs[disc]
    for child in children:
        parents[child] = disc

base = list(set(discs.keys()).difference(set(parents.keys())))[0]
print("Part 1:", base)

@functools.lru_cache(maxsize=None)
def get_weight(disc):
    global discs
    weight, children = discs[disc]
    return weight + sum(get_weight(child) for child in children)

ptr = base
while True:
    weight, children = discs[ptr]
    child_weights = Counter(get_weight(child) for child in children)
    if len(child_weights) == 1:
        print("Part 2:", weight + (good_weight - bad_weight))
        break
    good_weight, bad_weight = list(child_weights.keys())
    for child in children:
        if get_weight(child) == bad_weight:
            ptr = child
