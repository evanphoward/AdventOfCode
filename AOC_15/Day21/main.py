import itertools
shop = ((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0),
        (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5),
        (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3))
boss_hp, boss_dmg, boss_arm = tuple(int(line.split()[-1]) for line in open("input").read().split("\n"))


def get_stats(loadout):
    stats = [0, 0, 0]
    for item in loadout:
        for i in range(3):
            stats[i] += shop[item][i]
    return tuple(stats)


def wins(loadout):
    gold, dmg, arm = get_stats(loadout)
    if gold == 26:
        print()
    boss_dmg_per_turn = max(boss_dmg - arm, 1)
    dmg_per_turn = max(dmg - boss_arm, 1)
    return gold, (100 // boss_dmg_per_turn) > (boss_hp // dmg_per_turn)


gold_values = []
for weapon in range(5):
    for armor in list(range(5, 10)) + [()]:
        for rings in list(itertools.permutations(range(10, 16), 2)) + list(itertools.permutations(range(10, 16), 1)) + [()]:
            test_loadout = [weapon]
            if armor:
                test_loadout.append(armor)
            if rings:
                test_loadout.extend(list(rings))
            gold_values.append(wins(test_loadout))

print("Part 1:", min(gold_value[0] for gold_value in gold_values if gold_value[1]))
print("Part 2:", max(gold_value[0] for gold_value in gold_values if not gold_value[1]))



