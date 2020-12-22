from collections import deque


def get_decks():
    player_1, player_2 = open("input").read().split("\n\n")
    player_1 = deque([int(x) for x in player_1[10:].split("\n")])
    player_2 = deque([int(x) for x in player_2[10:].split("\n")])
    return player_1, player_2


player_1, player_2 = get_decks()
while player_1 and player_2:
    card_1 = player_1.popleft()
    card_2 = player_2.popleft()
    if card_1 > card_2:
        player_1.append(card_1)
        player_1.append(card_2)
    else:
        player_2.append(card_2)
        player_2.append(card_1)

winner = player_1 if player_1 else player_2
print(sum(i * winner.pop() for i in range(1, len(winner) + 1)))

player_1, player_2 = get_decks()
players_1 = deque()
players_2 = deque()
states_g = deque()
states = set()
i = 1
while True:
    while player_1 and player_2:
        state = (tuple(player_1), tuple(player_2))
        if state in states:
            break
        states.add(state)
        card_1 = player_1.popleft()
        card_2 = player_2.popleft()
        if len(player_1) >= card_1 and len(player_2) >= card_2:
            players_1.append((player_1, card_1))
            players_2.append((player_2, card_2))
            player_1 = deque(list(player_1)[:card_1])
            player_2 = deque(list(player_2)[:card_2])
            states_g.append(states)
            states = set()
        else:
            if card_1 > card_2:
                player_1.append(card_1)
                player_1.append(card_2)
            else:
                player_2.append(card_2)
                player_2.append(card_1)
    if players_1:
        states = states_g.pop()
        p1_won = bool(player_1)
        player_1, card_1 = players_1.pop()
        player_2, card_2 = players_2.pop()
        if p1_won:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)
    else:
        winner = player_1 if player_1 else player_2
        print(sum(i * winner.pop() for i in range(1, len(winner) + 1)))
        break
