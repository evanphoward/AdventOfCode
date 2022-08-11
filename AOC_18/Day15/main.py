from collections import deque

class Unit:
    def __init__(self, x, y, elf):
        self.x = x
        self.y = y
        self.elf = elf
        self.hp = 200
        self.attack = 3

    def __repr__(self):
        return ("E" if self.elf else "G") + "(" + str(self.hp) + ") @ " + str(self.x) + "," + str(self.y)

    def move(self):
        global map, pos_to_unit
        bfs_q = deque()
        explored = set()
        bfs_q.append(((self.x, self.y), []))
        explored.add((self.x, self.y))
        while bfs_q:
            pos, path = bfs_q.popleft()
            if pos in pos_to_unit and pos_to_unit[pos].elf != self.elf:
                if len(path) == 1:
                    break
                pos_to_unit.pop((self.x, self.y))
                self.x += path[0][0]
                self.y += path[0][1]
                pos_to_unit[(self.x, self.y)] = self
                if len(path) > 2:
                    return
                else:
                    break
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if map[new_pos] == "#" or (new_pos in pos_to_unit and pos_to_unit[new_pos].elf == self.elf):
                    continue
                if new_pos not in explored:
                    explored.add(new_pos)
                    bfs_q.append((new_pos, path + [(dx, dy)]))

        neighbors = [pos_to_unit[(self.x + dx, self.y + dy)] for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)] if (self.x + dx, self.y + dy) in pos_to_unit and pos_to_unit[(self.x + dx, self.y + dy)].elf != self.elf]
        if len(neighbors) == 0:
            return
        minNeighbor = neighbors[0]
        for neighbor in neighbors:
            if neighbor.hp < minNeighbor.hp:
                minNeighbor = neighbor
        
        minNeighbor.hp -= self.attack
        if minNeighbor.hp <= 0:
            pos_to_unit.pop((minNeighbor.x, minNeighbor.y))

map = dict()
pos_to_unit = dict()
for y, line in enumerate(open("input").read().split("\n")):
    for x, cell in enumerate(line):
        if cell in "GE":
            pos_to_unit[(x, y)] = Unit(x, y, cell == "E")
            cell = "."
        map[(x, y)] = cell

rounds = 0
while any(x.elf for x in pos_to_unit.values()) and any(not x.elf for x in pos_to_unit.values()):
    sorted_units = sorted(pos_to_unit.values(), key=lambda u: (u.y, u.x))
    print(sorted_units)
    for unit in sorted_units:
        unit.move()
    rounds += 1
print("Part 1:", rounds * sum(x.hp for x in pos_to_unit.values()))
    