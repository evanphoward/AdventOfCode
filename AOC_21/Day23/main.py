import heapq
dest_map = {"A": 0, "B": 1, "C": 2, "D": 3}
energy_map = {"A": 1, "B": 10, "C": 100, "D": 1000}
hallway_pos_map = [0, 1, 3, 5, 7, 9, 10]
room_pos = [2, 4, 6, 8]
hallway_room_map = {0: (1, 2), 1: (2, 3), 2: (3, 4), 3: (4, 5)}
# #D#C#B#A#
# #D#B#A#C#
# init_rooms = (("A", "B"), ("D", "C"), ("C", "B"), ("A", "D"))
init_rooms = (("B", "A"), ("C", "D"), ("A", "B"), ("C", "D"))
# init_rooms = (("B", "D", "D", "A"), ("C", "B", "C", "D"), ("A", "A", "B", "B"), ("C", "C", "A", "D"))
init_hallways = ('.', '.', '.', '.', '.', '.', '.')
goal_rooms = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"))


# def heuristic(rooms, hallways):
#     total = 0
#     for i, spot in enumerate(hallways):
#         if spot != ".":
#             total += abs(hallway_pos_map[i] - room_pos[dest_map[spot]]) * energy_map[spot]
#     for i, room in enumerate(rooms):
#         for spot in room:
#             if spot != ".":
#                 total += abs(room_pos[i] - room_pos[dest_map[spot]]) * energy_map[spot]
#     return total


q = [(0, init_rooms, init_hallways, [])]
explored = set()
while q:
    energy, rooms, hallways, path = heapq.heappop(q)
    if (rooms, hallways) in explored:
        continue
    if rooms == goal_rooms:
        print(path)
        print(energy)
    for i in range(len(hallways)):
        if hallways[i] == ".":
            continue
        dest_move = dest_map[hallways[i]]
        if rooms[dest_move][-1] != ".":
            continue
        if hallway_pos_map[i] < room_pos[dest_move]:
            if any(p != "." for p in hallways[i + 1:hallway_room_map[dest_move][0] + 1]):
                continue
        else:
            if any(p != "." for p in hallways[hallway_room_map[dest_move][1]:i]):
                continue
        for j in range(len(rooms[dest_move])):
            if all(p != "." for p in rooms[dest_move][:j]):
                energy_used = (abs(hallway_pos_map[i] - room_pos[dest_move]) + (len(rooms[dest_move]) - j)) * energy_map[hallways[i]]
                new_rooms = tuple(room if k != dest_move else tuple(list(rooms[dest_move][:j]) + [hallways[i]] + ["." for _ in range(len(rooms[dest_move]) - j - 1)]) for k, room in enumerate(rooms))
                new_hallways = tuple(spot1 if w != i else "." for w, spot1 in enumerate(hallways))
                heapq.heappush(q, (energy + energy_used, new_rooms, new_hallways, path + [new_rooms, new_hallways]))
                break
    for i in range(len(rooms)):
        for k in range(len(rooms[i])):
            if all(p == "." for p in rooms[i][k + 1:]) and rooms[i][k] != ".":
                for j in range(len(hallways)):
                    if hallways[j] != ".":
                        continue
                    if hallway_pos_map[j] < room_pos[i]:
                        if any(p != "." for p in hallways[j + 1:hallway_room_map[i][0] + 1]):
                            continue
                    else:
                        if any(p != "." for p in hallways[hallway_room_map[i][1]:j]):
                            continue
                    energy_used = (abs(hallway_pos_map[j] - room_pos[i]) + (len(rooms[i]) - k)) * energy_map[rooms[i][k]]
                    new_rooms = tuple(room if w != i else tuple(list(rooms[i][:k]) + ["." for _ in range(len(rooms[i]) - k)]) for w, room in enumerate(rooms))
                    new_hallways = tuple(spot if w != j else rooms[i][k] for w, spot in enumerate(hallways))
                    heapq.heappush(q, (energy + energy_used, new_rooms, new_hallways, path + [new_rooms, new_hallways]))
                break
    explored.add((rooms, hallways))
