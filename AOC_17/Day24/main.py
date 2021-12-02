def next_cmpts(cmpts, port):
    ans = []
    for i in range(len(cmpts)):
        if port in cmpts[i]:
            ans.append(i)
    return ans


def gen(bridge, cmpts):
    prev_port = bridge[-1]
    valid_cmpts = next_cmpts(cmpts, prev_port)
    if len(valid_cmpts) == 0:
        return [bridge]
    ans = [bridge] if len(bridge) > 1 else []
    for i in valid_cmpts:
        new_cmpts = cmpts.copy()
        next_cmpt = new_cmpts.pop(i)

        next_port = next_cmpt[0] if prev_port == next_cmpt[1] else next_cmpt[1]

        ans.extend(gen(bridge + [next_port], new_cmpts))
    return ans


inp = [[int(x) for x in line.strip().split("/")] for line in open("input")]
bridges = gen([0], inp)
print("Part 1:", max(sum(bridge[:-1]) * 2 + bridge[-1] for bridge in bridges))

max_length = max(len(bridge) for bridge in bridges)
print("Part 2:", max(sum(bridge[:-1]) * 2 + bridge[-1] if len(bridge) == max_length else 0 for bridge in bridges))
