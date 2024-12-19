from MiscFiles.library import *

towels, designs = get_input(2024, 19).split("\n\n")
towels = towels.split(', ')
designs = designs.split('\n')

@functools.lru_cache(maxsize=None)
def is_possible(design):
    global towels
    if design == '':
        return 1
    possible = 0
    for towel in towels:
        if design.startswith(towel):
            possible += is_possible(design[len(towel):])
    return possible

p1, p2 = 0, 0
for design in designs:
    num_possible = is_possible(design)
    p1 += 1 if num_possible else 0
    p2 += num_possible

print("Part 1:", p1)
print("Part 2:", p2)
