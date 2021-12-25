inp = open("input").read().split("\n")
num_rows = len(inp)
num_cols = len(inp[0])
east = {(r, c) for r, row in enumerate(inp) for c, cell in enumerate(row) if cell == ">"}
south = {(r, c) for r, row in enumerate(inp) for c, cell in enumerate(row) if cell == "v"}

step = 0
moved = -1
while moved != 0:
    moved = 0
    to_move = set()
    for r, c in east:
        check_c = 0 if c == num_cols - 1 else c + 1
        if (r, check_c) not in east and (r, check_c) not in south:
            to_move.add((r, c))
    moved += len(to_move)
    for r, c in to_move:
        east.remove((r, c))
        if c == num_cols - 1:
            east.add((r, 0))
        else:
            east.add((r, c + 1))

    to_move = set()
    for r, c in south:
        check_r = 0 if r == num_rows - 1 else r + 1
        if (check_r, c) not in east and (check_r, c) not in south:
            to_move.add((r, c))
    moved += len(to_move)
    for r, c in to_move:
        south.remove((r, c))
        if r == num_rows - 1:
            south.add((0, c))
        else:
            south.add((r + 1, c))
    moved += len(to_move)
    step += 1
print(step)
