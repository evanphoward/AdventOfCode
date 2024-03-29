bingo = list(map(int, open("input").readline().strip().split(",")))
boards = [[list(map(int, line.strip().split())) for line in board.split("\n")] for board in open("input").read().split("\n\n")[1:]]
board_checks = [[[False] * 5 for _ in range(5)] for _ in range(len(boards))]

num_to_pos = dict()
for j, board in enumerate(boards):
    for r in range(5):
        for c in range(5):
            if board[r][c] not in num_to_pos:
                num_to_pos[board[r][c]] = []
            num_to_pos[board[r][c]].append((j, r, c))

winners = set()
scores = []
for i in range(len(bingo)):
    next_num = bingo[i]
    for j, r, c in num_to_pos[next_num]:
        board_checks[j][r][c] = True
    for j in range(len(boards)):
        if j not in winners and (any(all(board_checks[j][r]) for r in range(5)) or any(all(board_checks[j][r][c] for r in range(5)) for c in range(5))):
            winners.add(j)
            scores.append(sum(boards[j][r][c] if not board_checks[j][r][c] else 0 for r in range(5) for c in range(5)) * next_num)

print("Part 1:", scores[0])
print("Part 2:", scores[-1])

