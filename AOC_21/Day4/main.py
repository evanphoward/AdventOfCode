bingo = [int(x) for x in open("input").readline().strip().split(",")]
boards = []
board_checks = []
curr_board = []
for line in open("input").readlines()[2:]:
    if line == "\n":
        boards.append(curr_board)
        board_checks.append([[False] * 5 for _ in range(5)])
        curr_board = []
    else:
        curr_board.append([int(x) for x in line.strip().split()])

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

