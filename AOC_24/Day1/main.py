from MiscFiles.library import *

inp = get_input(2024, 1).split("\n")

left_list, right_list = [], []
for line in inp:
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()
right_list_frequencies = Counter(right_list)

print("Part 1:", sum(abs(left_list[i] - right_list[i]) for i in range(len(inp))))
print("Part 2:", sum(loc_id * right_list_frequencies[loc_id] for loc_id in left_list))
