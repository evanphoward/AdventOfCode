import math


class Group:
    def __init__(self, line, infection, boost):
        split = line.split()
        self.num_units = int(split[0])
        self.hp = int(split[4])
        self.dmg = int(split[-6])
        if not infection:
            self.dmg += boost
        self.dmg_type = split[-5]
        self.init = int(split[-1])
        self.immunities = []
        self.weaknesses = []
        self.infection = infection
        self.attacked = False
        self.target = None
        if "(" in line:
            vulnerabilities = line[line.index("(") + 1 : line.index(")")]
            for vuln in vulnerabilities.split(";"):
                vuln = vuln.replace(",", "").split()
                types = vuln[2:]
                if vuln[0] == "weak":
                    self.weaknesses = types
                else:
                    self.immunities = types


    def attack(self, damage):
        self.num_units -= math.floor(damage / self.hp)
        self.num_units = max(self.num_units, 0)
        self.attacked = False


    def damage_taken(self, other):
        base_dmg = other.dmg * other.num_units
        if other.dmg_type in self.weaknesses:
            return 2 * base_dmg
        if other.dmg_type in self.immunities:
            return 0
        return base_dmg



def run(boost):
    MAX_ROUNDS = 2000
    groups = []

    is_infection = False
    for line in open("input").read().split("\n")[1:]:
        if line == "" or line == "Infection:":
            is_infection = True
            continue
        groups.append(Group(line, is_infection, boost))


    round = 0
    while any(g.infection and g.num_units > 0 for g in groups) and any(not g.infection and g.num_units > 0 for g in groups) and round < MAX_ROUNDS:
        for group in sorted(groups, key=lambda g: (g.num_units * g.dmg, g.init), reverse=True):
            if group.num_units <= 0:
                continue
            possible_targets = [g for g in groups if g.infection != group.infection and g.num_units > 0 and not g.attacked]
            if len(possible_targets) > 0:
                best_target = max(possible_targets, key=lambda g: (g.damage_taken(group), g.num_units * g.dmg, g.init))
                if best_target.damage_taken(group) > 0:
                    group.target = best_target
                    group.target.attacked = True

        groups.sort(key=lambda g: g.init, reverse=True)
        for group in groups:
            if group.target is not None:
                group.target.attack(group.target.damage_taken(group))
                group.target = None
        round += 1

    return sum(g.num_units for g in groups), sum(g.num_units for g in groups if g.infection)



print("Part 1:", run(0)[0])

lower, upper = 0, 100
while lower <= upper:
    mid = (lower + upper) // 2
    results = run((lower + upper) // 2)[1]
    if results > 0:
        lower = mid + 1
    elif results == 0:
        upper = mid - 1

assert run(lower)[1] == 0 and run(upper)[1] > 0
print("Part 2:", run(lower)[0])
