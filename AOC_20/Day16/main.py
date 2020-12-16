import re
import math

rules = list()
tickets = list()
my_ticket = False
for line in open("input").readlines():
    ints = [int(x) for x in re.findall(r"\d+", line)]
    if len(ints) == 4:
        rules.append(ints)
    elif len(ints) > 4:
        if not my_ticket:
            my_ticket = ints
        else:
            tickets.append(ints)

total = 0
n = len(rules)
rule_pos = [[True for i in range(n)] for j in range(n)]
for ticket in tickets:
    all_valid = True
    for field in ticket:
        valid = False
        for rule in rules:
            if rule[0] <= field <= rule[1] or rule[2] <= field <= rule[3]:
                valid = True
        if not valid:
            all_valid = False
            total += field

    if all_valid:
        for i in range(n):
            for j, rule in enumerate(rules):
                if not (rule[0] <= ticket[i] <= rule[1] or rule[2] <= ticket[i] <= rule[3]):
                    rule_pos[i][j] = False

print("Part 1:", total)
map_rules = [None]*n
used = [False]*n
found = 0
while found < n:
    for i in range(n):
        valid = [j for j in range(n) if rule_pos[i][j] and not used[j]]
        if len(valid) == 1:
            map_rules[i] = valid[0]
            used[valid[0]] = True
            found += 1

print("Part 2:", math.prod([my_ticket[i] for i, j in enumerate(map_rules) if j < 6]))
