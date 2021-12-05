from collections import deque
import itertools

# The first floor contains a strontium generator, a strontium-compatible microchip,
# a plutonium generator, and a plutonium-compatible microchip.
# The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip,
# a curium generator, and a curium-compatible microchip.
# The third floor contains a thulium-compatible microchip.
# The fourth floor contains nothing relevant.
# Floors object contains steps taken, elevator pos and list of lists representing objects on each floor
initial_setup_one = (0, 0,
                     [["SG", "SM", "PG", "PM"],
                      ["TG", "RG", "RM", "CG", "CM"],
                      ["TM"],
                      []])
initial_setup_two = (0, 0,
                     [["EG", "EM", "DG", "DM", "SG", "SM", "PG", "PM"],
                      ["TG", "RG", "RM", "CG", "CM"],
                      ["TM"],
                      []])


def is_safe(floor):
    has_gen = any(item[1] == "G" for item in floor)
    if not has_gen:
        return True
    for item in floor:
        if item[1] == "M" and (item[0] + "G") not in floor:
            return False
    return True


def hashable(elv, floors):
    i_map = dict()
    i = 0
    standardized_floors = []
    for floor in floors:
        curr_floor = []
        for item in floor:
            if item[0] not in i_map:
                i_map[item[0]] = i
                i += 1
            curr_floor.append(str(i_map[item[0]]) + item[1])
        standardized_floors.append(curr_floor)
    floors_tuple = tuple(tuple(sorted(floor)) for floor in standardized_floors)
    return elv, floors_tuple


def bfs(root):
    bfs_q = deque()
    bfs_q.append(root)
    explored = set()
    explored.add(hashable(root[1], root[2]))
    while bfs_q:
        steps, elv, floors = bfs_q.popleft()
        for d_elv in [1, -1]:
            if (elv + d_elv == 4) or (elv + d_elv == -1):
                continue
            for num_objs in range(1, 3):
                for objs in itertools.combinations(floors[elv], num_objs):
                    new_floors = [[obj for obj in floor] for floor in floors]
                    for obj in objs:
                        new_floors[elv].remove(obj)
                        new_floors[elv + d_elv].append(obj)
                    if all(len(floor) == 0 for floor in new_floors[:-1]):
                        return steps + 1
                    if not (is_safe(new_floors[elv + d_elv]) and is_safe(new_floors[elv])) :
                        continue
                    hashed = hashable(elv + d_elv, new_floors)
                    if hashed not in explored:
                        explored.add(hashed)
                        bfs_q.append((steps + 1, elv + d_elv, new_floors))
    return -1


print("Part 1:", bfs(initial_setup_one))
print("Part 2:", bfs(initial_setup_two))


