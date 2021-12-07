reindeer = [(int(line[3]), int(line[6]), int(line[13])) for line in [line.strip().split() for line in open("input").readlines()]]
reindeer_states = [[True, attr[1], 0, 0] for attr in reindeer]
for _ in range(2503):
    for i in range(len(reindeer_states)):
        if reindeer_states[i][0]:
            reindeer_states[i][2] += reindeer[i][0]
        reindeer_states[i][1] -= 1
        if reindeer_states[i][1] == 0:
            reindeer_states[i][1] = reindeer[i][2] if reindeer_states[i][0] else reindeer[i][1]
            reindeer_states[i][0] = not reindeer_states[i][0]
    max_reindeer = [0]
    for i in range(1, len(reindeer_states)):
        if reindeer_states[i][2] > reindeer_states[max_reindeer[0]][2]:
            max_reindeer = [i]
        elif reindeer_states[i][2] == reindeer_states[max_reindeer[0]][2]:
            max_reindeer.append(i)
    for i in max_reindeer:
        reindeer_states[i][3] += 1


print("Part 1:", max(r[2] for r in reindeer_states))
print("Part 2:", max(r[3] for r in reindeer_states))
