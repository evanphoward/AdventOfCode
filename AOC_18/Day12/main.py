from collections import defaultdict
initial_state, rules = open("input").read().split("\n\n")
rules = [rule.split(" => ") for rule in rules.split("\n")]
rules = {rule[0]: rule[1] for rule in rules}

pots = defaultdict(bool)
for i, pot in enumerate(initial_state.split()[2]):
    pots[i] = pot == "#"

prev_sum = sum(pot_num if pot_val else 0 for pot_num, pot_val in pots.items())
prev_delta = -1
for i in range(10000):
    new_pots = defaultdict(bool)
    for j in range(min(pots.keys()) - 2, max(pots.keys()) + 3):
        pattern = ''.join("#" if pots[k] else "." for k in range(j - 2, j + 3))
        new_pots[j] = rules[pattern] == "#"
    pots = new_pots

    if i == 19:
        print("Part 1:", sum(pot_num if pot_val else 0 for pot_num, pot_val in pots.items()))

    pot_sum = sum(pot_num if pot_val else 0 for pot_num, pot_val in pots.items())
    delta = pot_sum - prev_sum
    if delta == prev_delta:
        print("Part 2:", pot_sum + (delta * (50000000000 - i - 1)))
        break
    prev_sum = pot_sum
    prev_delta = delta
    
