from MiscFiles.library import *

ans = 0

rules, updates = get_input(2024, 5).split("\n\n")

edges = set()
for rule in rules.split('\n'):
    u, v = rule.split("|")
    edges.add((int(u), int(v)))

valid = []
p1, p2 = 0, 0
for update in updates.split('\n'):
    update = list(map(int, update.split(',')))
    valid_update = True
    any_wrong = True
    update_p2 = update.copy()
    while any_wrong:
        any_wrong = False
        for u, v in edges:
            if u in update_p2 and v in update_p2:
                u_ind = update_p2.index(u)
                v_ind = update_p2.index(v)
                if update_p2.index(u) > update_p2.index(v):
                    valid_update = False
                    any_wrong = True
                    update_p2[u_ind] = v
                    update_p2[v_ind] = u
        if valid_update:
            p1 += int(update[len(update) // 2])
    if not valid_update:
        p2 += int(update_p2[len(update_p2) // 2])


print("Part 1:", p1)
print("Part 2:", p2)