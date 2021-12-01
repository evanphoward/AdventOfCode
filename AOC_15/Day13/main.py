import itertools


def max_hpp(ppl_hap):
    max_hap = 0
    num_people = len(ppl_hap.keys())
    for ordering in itertools.permutations(ppl_hap.keys()):
        hap = 0
        for i in range(num_people):
            hap += people_hap[ordering[i]][ordering[(i + 1) % num_people]]
            hap += people_hap[ordering[i]][ordering[(i - 1) % num_people]]
        max_hap = max(hap, max_hap)
    return max_hap


people_hap = dict()

for rules in open("input").readlines():
    rules = rules.split()
    person = rules[0]
    if person not in people_hap:
        people_hap[person] = dict()

    pos = rules[2] == "gain"
    amt = int(rules[3]) * (1 if pos else -1)

    people_hap[person][rules[-1][:-1]] = amt

print("Part 1:", max_hpp(people_hap))

people_hap["Evan"] = dict()
for person in people_hap.keys():
    if person == "Evan":
        continue
    people_hap["Evan"][person] = 0
    people_hap[person]["Evan"] = 0

print("Part 2:", max_hpp(people_hap))

