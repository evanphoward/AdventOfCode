from collections import defaultdict, Counter

p1_initial, p2_initial = [int(line[-1]) for line in open("input").read().split("\n")]
scores = [0, 0]
die = 1
pos = [p1_initial, p2_initial]
rolls, turn = 0, False
while scores[0] < 1000 and scores[1] < 1000:
    pos[turn] = (pos[turn] + 3 * die + 2) % 10 + 1
    scores[turn] += pos[turn]
    die = (die + 2) % 100 + 1
    rolls += 3
    turn = not turn
print("Part 1:", min(scores) * rolls)

moves = Counter(i + j + k for i in range(1, 4) for j in range(1, 4) for k in range(1, 4))
universes = {((0, 0), (p1_initial, p2_initial)): 1}
total = [0, 0]
turn = False
while universes:
    new_universes = defaultdict(int)
    for (scores, pos), count in universes.items():
        for move, freq in moves.items():
            new_pos = list(pos)
            new_scores = list(scores)
            new_pos[turn] = (pos[turn] + move - 1) % 10 + 1
            new_scores[turn] = scores[turn] + new_pos[turn]
            if new_scores[turn] >= 21:
                total[turn] += count * freq
                continue
            new_universes[(tuple(new_scores), tuple(new_pos))] += count * freq
    universes = new_universes
    turn = not turn

print("Part 2:", max(total))
