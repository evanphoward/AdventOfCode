from functools import cmp_to_key
from collections import Counter


def get_hand_type(hand, p2):
    hand_count = Counter(hand)

    if p2:
        to_swap = hand_count.most_common()[0][0]
        if to_swap == 0 and len(hand_count) > 1:
            to_swap = hand_count.most_common()[1][0]
        if to_swap != 0:
            hand_count[to_swap] += hand_count[0]
            hand_count[0] = 0

    if 5 in hand_count.values():
        return 0
    if 4 in hand_count.values():
        return 1
    if 3 in hand_count.values():
        return 2 if 2 in hand_count.values() else 3
    if 2 in hand_count.values():
        return 4 if Counter(hand_count.values())[2] == 2 else 5
    return 6


def comp(hand_1, hand_2, p2):
    h1 = get_hand_type(hand_1, p2)
    h2 = get_hand_type(hand_2, p2)
    if h1 > h2:
        return 1
    if h1 < h2:
        return -1
    for i in range(5):
        if hand_1[i] > hand_2[i]:
            return -1
        elif hand_1[i] < hand_2[i]:
            return 1
    return 0


def run(p2):
    mappings = {'J': 0 if p2 else 11, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}
    inp = [(tuple(mappings[y] for y in x.split()[0]), int(x.split()[1])) for x in open("input").read().split("\n")]
    return sum(bid * (i + 1) for i, (_, bid) in enumerate(sorted(inp, key=cmp_to_key(lambda h1, h2: comp(h1[0], h2[0], p2)), reverse=True)))


print("Part 1:", run(False))
print("Part 2:", run(True))
