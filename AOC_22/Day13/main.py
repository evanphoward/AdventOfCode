inp = open("input").read().strip().split("\n\n")


def parse(p):
    if len(p) == 0:
        return []
    if p[0] == '[':
        ret = []
        list_els = p[1:-1]
        if len(list_els) == 0:
            return []
        if len(list_els) == 1:
            return [int(list_els)]
        depth = 0
        i = 0
        j = 0
        while j < len(list_els):
            if list_els[j] == '[':
                depth += 1
            elif list_els[j] == ']':
                depth -= 1
            elif list_els[j] == ',' and depth == 0:
                ret.append(parse(list_els[i:j]))
                i = j + 1
            if j == len(list_els) - 1:
                ret.append(parse(list_els[i:j + 1]))
            j += 1
        return ret
    else:
        return int(p)


def comp(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            comp_vl = comp(left[i], right[i])
            if comp_vl != 0:
                return comp_vl
        return len(left) - len(right)
    else:
        if isinstance(left, int):
            return comp([left], right)
        else:
            return comp(left, [right])


pairs = []
right_order = []
all_keys = []
for pair in inp:
    p1, p2 = pair.split("\n")
    pairs.append((parse(p1), parse(p2)))
    all_keys.append(parse(p1))
    all_keys.append(parse(p2))

for i, (p1, p2) in enumerate(pairs):
    if comp(p1, p2) <= 0:
        right_order.append(i + 1)
print("Part 1:", sum(right_order))

all_keys = sorted(all_keys + [[[6]], [[2]]], cmp=comp)
print(all_keys)

ans = 1
for i in range(len(all_keys)):
    if all_keys[i] in ([[2]], [[6]]):
        ans *= i + 1
print("Part 2:", ans)
