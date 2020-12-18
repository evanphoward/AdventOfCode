# This can be expressed using really nice math but I feel that it's a bit beyond my level
# So I've just done part 1
LENGTH = 10007


def deal(inc):
    new_deck = [None]*LENGTH
    i, j = 0, 0
    while any(card is None for card in new_deck):
        new_deck[j] = deck[i]
        i += 1
        j += inc
        j = j % LENGTH
    return new_deck


deck = [i for i in range(LENGTH)]
for line in open("input").readlines():
    line = line.strip().split(" ")
    try:
        inc = int(line[-1])
    except ValueError:
        deck.reverse()
        continue
    if line[0] == "cut":
        deck = deck[inc:] + deck[:inc]
    else:
        deck = deal(inc)
print("Part 1:", deck.index(2019))