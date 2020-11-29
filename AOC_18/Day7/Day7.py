steps = {chr(x): set() for x in range(65, 91)}
for line in open('input').readlines():
    line = line.split()
    steps[line[7]].add(line[1])

order = []
for i in range(26):
    for step in steps:
        if not steps[step] and step not in order:
            order = order + [step]
            for step_change in steps:
                steps[step_change] -= {step}
            break
print("".join(order))
