from collections import defaultdict
initial_state, rules = open("input").read().split("\n\n")
rules = [rule.split(" => ") for rule in rules.split("\n")]
rules = {rule[0]: rule[1] for rule in rules}

pots = defaultdict(bool)
for i, pot in enumerate(initial_state.split()[2]):
    pots[i] = pot == "#"


for _ in range(20):
    new_pots = defaultdict(bool)
    for i in range(min(pots.keys()) - 2, max(pots.keys()) + 3):
        pattern = ''.join("#" if pots[j] else "." for j in range(i - 2, i + 3))
        new_pots[i] = rules[pattern] == "#"
    pots = new_pots

print("Part 1:", sum(pot_num if pot_val else 0 for pot_num, pot_val in pots.items()))
