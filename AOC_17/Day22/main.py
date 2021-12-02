DIRS = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
CHANGES = {".": "W", "W": "#", "#": "F", "F": "."}


def print_board():
    for r in range(len(board)):
        print(''.join("#" if n else "." for n in board[r]))
    print()


def step1():
    global board, heading, xpos, ypos, total

    heading += 1 if board[ypos][xpos] else -1
    heading = heading % 4

    board[ypos][xpos] = not board[ypos][xpos]
    if board[ypos][xpos]:
        total += 1

    xdelta, ydelta = DIRS[heading]
    xpos += xdelta
    ypos += ydelta

    if ypos == -1:
        ypos += 1
        board.insert(0, [False] * len(board[0]))
    elif ypos == len(board):
        board.append([False] * len(board[0]))
    elif xpos == -1:
        xpos += 1
        for i in range(len(board)):
            board[i].insert(0, False)
    elif xpos == len(board[0]):
        for i in range(len(board)):
            board[i].append(False)


def step2():
    global board, heading, xpos, ypos, total

    curr = board[ypos][xpos]
    if curr == ".":
        heading -= 1
    elif curr == "#":
        heading += 1
    elif curr == "F":
        heading += 2
    heading = heading % 4

    board[ypos][xpos] = CHANGES[board[ypos][xpos]]
    if board[ypos][xpos] == "#":
        total += 1

    xdelta, ydelta = DIRS[heading]
    xpos += xdelta
    ypos += ydelta

    if ypos == -1:
        ypos += 1
        board.insert(0, ["."] * len(board[0]))
    elif ypos == len(board):
        board.append(["."] * len(board[0]))
    elif xpos == -1:
        xpos += 1
        for i in range(len(board)):
            board[i].insert(0, ".")
    elif xpos == len(board[0]):
        for i in range(len(board)):
            board[i].append(".")


board = []
for row in open("input"):
    board.append([node == "#" for node in row.strip()])

heading = 0
xpos = ypos = len(board) // 2

total = 0
for _ in range(10000):
    step1()

print("Part 1:", total)

board = []
for row in open("input"):
    board.append([n for n in row.strip()])

heading = 0
xpos = ypos = len(board) // 2

total = 0
for _ in range(10000000):
    step2()

print("Part 2:", total)

