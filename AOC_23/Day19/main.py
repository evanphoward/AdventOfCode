workflowsi, partsi = open("input").read().split("\n\n")
workflows = dict()
for w in workflowsi.split("\n"):
    label = w.split("{")[0]
    rules = w.split("{")[1][:-1].split(",")
    workflows[label] = rules

parts = set()
for p in partsi.split("\n"):
    parts.add(tuple(int(x[2:]) for x in p[1:-1].split(",")))

ans = 0
for part in parts:
    x, m, a, s = part
    cur = "in"

    while cur not in ('A', 'R'):
        for rule in workflows[cur]:
            if ":" not in rule:
                cur = rule
                break
            else:
                rule = rule.split(":")
                if eval(rule[0]):
                    cur = rule[1]
                    break
    if cur == 'A':
        ans += sum(part)
print("Part 1:", ans)

def num_possible(label, ranges):
    if label == "A":
        return len(ranges['x']) * len(ranges['m']) * len(ranges['a']) * len(ranges['s'])
    if label == "R":
        return 0
    ans = 0
    for rule in workflows[label]:
        if ":" not in rule:
           ans += num_possible(rule, ranges)
        else:
            rule = rule.split(":")
            valid = set(range(1, int(rule[0][2:]))) if rule[0][1] == "<" else set(range(int(rule[0][2:]) + 1, 4001))

            new_ranges = ranges.copy()
            new_ranges[rule[0][0]] = new_ranges[rule[0][0]].intersection(valid)
            ans += num_possible(rule[1], new_ranges)

            ranges[rule[0][0]] = ranges[rule[0][0]].intersection(set(range(1, 4001)).difference(valid))
    return ans

print("Part 2:", num_possible("in", {"x": set(range(1, 4001)), "m": set(range(1, 4001)), "a": set(range(1, 4001)), "s": set(range(1, 4001))}))