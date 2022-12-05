from collections import deque


class Unit:
    def __init__(self, x, y, attack, elf):
        self.x = x
        self.y = y
        self.elf = elf
        self.hp = 200
        self.attack = attack

    def attack_action(self):
        neighbors = [pos_to_unit[(self.x + dx, self.y + dy)] for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)] if
                     (self.x + dx, self.y + dy) in pos_to_unit and pos_to_unit[
                         (self.x + dx, self.y + dy)].elf != self.elf]
        neighbors = sorted(neighbors, key=lambda u: (u.y, u.x))
        if len(neighbors) == 0:
            return False
        min_neighbor = neighbors[0]
        for neighbor in neighbors:
            if neighbor.hp < min_neighbor.hp:
                min_neighbor = neighbor

        min_neighbor.hp -= self.attack
        if min_neighbor.hp <= 0:
            pos_to_unit.pop((min_neighbor.x, min_neighbor.y))

        return True

    def move(self):
        global map, pos_to_unit

        if self.hp <= 0 or self.attack_action():
            return

        goals = set()
        for pos, unit in pos_to_unit.items():
            if unit.elf == self.elf:
                continue
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                pot_goal = (pos[0] + dx, pos[1] + dy)
                if pot_goal in pos_to_unit or map[pot_goal] == '#':
                    continue
                goals.add(pot_goal)

        if len(goals) == 0:
            return

        bfs_q = deque()
        explored = set()
        bfs_q.append(((self.x, self.y), []))
        explored.add((self.x, self.y))
        pot_moves = []

        while bfs_q:
            pos, path = bfs_q.popleft()
            if pos in goals:
                pot_moves.append((pos, len(path), (path[0][0], path[0][1])))
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if map[new_pos] == "#" or new_pos in pos_to_unit:
                    continue
                if new_pos not in explored:
                    explored.add(new_pos)
                    bfs_q.append((new_pos, path + [(dx, dy)]))

        if len(pot_moves) == 0:
            return

        goal, _, move = sorted(pot_moves, key=lambda u: (u[1], u[0][1], u[0][0]))[0]
        pos_to_unit.pop((self.x, self.y))
        self.x += move[0]
        self.y += move[1]
        pos_to_unit[(self.x, self.y)] = self

        self.attack_action()


for a in range(3, 1000):
    map = dict()
    pos_to_unit = dict()
    for y, line in enumerate(open("input").read().split("\n")):
        for x, cell in enumerate(line):
            if cell in "GE":
                pos_to_unit[(x, y)] = Unit(x, y, (a if cell == "E" else 3), cell == "E")
                cell = "."
            map[(x, y)] = cell
    num_elves = sum(u.elf for u in pos_to_unit.values())

    rounds = 0
    while any(x.elf for x in pos_to_unit.values()) and any(not x.elf for x in pos_to_unit.values()):
        sorted_units = sorted(pos_to_unit.values(), key=lambda u: (u.y, u.x))
        for unit in sorted_units:
            if all(x.elf for x in pos_to_unit.values()) or all(not x.elf for x in pos_to_unit.values()):
                break
            unit.move()
        rounds += 1
    if a == 3:
        print("Part 1:", rounds * sum(x.hp for x in pos_to_unit.values()))
    if sum(u.elf for u in pos_to_unit.values()) == num_elves:
        print("Part 2:", rounds * sum(x.hp for x in pos_to_unit.values()))
        break
