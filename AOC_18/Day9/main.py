from collections import deque
inp = open("input").readline().split()
NUM_PLAYERS = int(inp[0])


def play_game(last_marble):
    marbles = deque([0])
    scores = [0] * NUM_PLAYERS
    for marble in range(1, last_marble + 1):
        if marble % 23 != 0:
            marbles.rotate(-1)
            marbles.append(marble)
        else:
            marbles.rotate(7)
            scores[marble % NUM_PLAYERS] += marble + marbles.pop()
            marbles.rotate(-1)
    return max(scores)


print("Part 1:", play_game(int(inp[6])))
print("Part 2:", play_game(int(inp[6]) * 100))
