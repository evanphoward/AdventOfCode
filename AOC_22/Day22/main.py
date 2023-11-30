maze_inp, direcs = open("input").read().split("\n\n")
# ONLY PART 2 CODE HERE, PART 1 WAS OVERWRITTEN
# HARDCODED HORROR LIES BEYOND

grid = dict()
ranges_cols = dict()
ranges_rows = dict()
faces = {1: (0, 100), 2: (0, 50), 3: (50, 50), 4: (100, 50), 5: (100, 0), 6: (150, 0)}
faces_pts = dict()
for i, pt in faces.items():
    for r in range(pt[0], pt[0] + 50):
        for c in range(pt[1], pt[1] + 50):
            faces_pts[(r, c)] = i
for r, row in enumerate(maze_inp.split("\n")):
    for c, cell in enumerate(row):
        if cell == " ":
            continue
        grid[r, c] = cell
        if r not in ranges_rows:
            ranges_rows[r] = [c, c]
        if c not in ranges_cols:
            ranges_cols[c] = [r, r]
        if c < ranges_rows[r][0]:
            ranges_rows[r][0] = c
        if c > ranges_rows[r][1]:
            ranges_rows[r][1] = c
        if r < ranges_cols[c][0]:
            ranges_cols[c][0] = r
        if r > ranges_cols[c][1]:
            ranges_cols[c][1] = r

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cr = min(r for (r, c) in grid.keys())
cc = min(c for (r, c) in [(r1, c1) for (r1, c1) in grid.keys() if r1 ==cr])
heading = 1
d_i = 0
move = 0
while d_i < len(direcs):
    if direcs[d_i] == "L" or direcs[d_i] == "R":
        for _ in range(move):
            dr, dc = dirs[heading]
            new_r = cr + dr
            new_c = cc + dc
            face = faces_pts[(cr, cc)]
            if heading == 0 and new_r < ranges_cols[cc][0]:
                if face == 1:
                    new_c = (cc - faces[face][1]) + faces[6][1]
                    new_r = faces[6][0] + 49
                elif face == 2:
                    new_c = faces[6][1]
                    new_r = (cc - faces[face][1]) + faces[6][0]
                    if grid[(new_r, new_c)] != "#":
                        heading = 1
                elif face == 5:
                    new_c = faces[3][1]
                    new_r = (cc - faces[face][1]) + faces[3][0]
                    if grid[(new_r, new_c)] != "#":
                        heading = 1
                else:
                    assert False
                # new_r = ranges_cols[cc][1]
            elif heading == 1 and new_c > ranges_rows[cr][1]:
                if face == 1:
                    new_c = faces[4][1] + 49
                    new_r = faces[4][0] + 49 - (cr - faces[face][0])
                    if grid[(new_r, new_c)] != "#":
                        heading = 3
                elif face == 3:
                    new_c = (cr - faces[face][0]) + faces[1][1]
                    new_r = faces[1][0] + 49
                    if grid[(new_r, new_c)] != "#":
                        heading = 0
                elif face == 4:
                    new_c = faces[1][1] + 49
                    new_r = faces[1][0] + 49 - (cr - faces[face][0])
                    if grid[(new_r, new_c)] != "#":
                        heading = 3
                elif face == 6:
                    new_c = (cr - faces[face][0]) + faces[4][1]
                    new_r = faces[4][0] + 49
                    if grid[(new_r, new_c)] != "#":
                        heading = 0
                else:
                    assert False
                # new_c = ranges_rows[cr][0]
            elif heading == 2 and new_r > ranges_cols[cc][1]:
                if face == 1:
                    new_c = faces[3][1] + 49
                    new_r = (cc - faces[face][1]) + faces[3][0]
                    if grid[(new_r, new_c)] != "#":
                        heading = 3
                elif face == 4:
                    new_c = faces[6][1] + 49
                    new_r = (cc - faces[face][1]) + faces[6][0]
                    if grid[(new_r, new_c)] != "#":
                        heading = 3
                elif face == 6:
                    new_c = (cc - faces[face][1]) + faces[1][1]
                    new_r = faces[1][0]
                else:
                    assert False
                # new_r = ranges_cols[cc][0]
            elif heading == 3 and new_c < ranges_rows[cr][0]:
                if face == 2:
                    new_c = faces[5][1]
                    new_r = faces[5][0] + 49 - (cr - faces[face][0])
                    if grid[(new_r, new_c)] != "#":
                        heading = 1
                elif face == 3:
                    new_c = (cr - faces[face][0]) + faces[5][1]
                    new_r = faces[5][0]
                    if grid[(new_r, new_c)] != "#":
                        heading = 2
                elif face == 5:
                    new_c = faces[2][1]
                    new_r = faces[2][0] + 49 - (cr - faces[face][0])
                    if grid[(new_r, new_c)] != "#":
                        heading = 1
                elif face == 6:
                    new_c = (cr - faces[face][0]) + faces[2][1]
                    new_r = faces[2][0]
                    if grid[(new_r, new_c)] != "#":
                        heading = 2
                else:
                    assert False
                # new_c = ranges_rows[cr][1]
            if grid[(new_r, new_c)] == "#":
                break
            cr = new_r
            cc = new_c
        if direcs[d_i] == "L":
            heading = (heading - 1) % 4
        else:
            heading = (heading + 1) % 4
        move = 0
    else:
        move *= 10
        move += int(direcs[d_i])
    d_i += 1
for _ in range(move):
    dr, dc = dirs[heading]
    new_r = cr + dr
    new_c = cc + dc
    face = faces_pts[(cr, cc)]
    if heading == 0 and new_r < ranges_cols[cc][0]:
        if face == 1:
            new_c = (cc - faces[face][1]) + faces[6][1]
            new_r = faces[6][0] + 49
        elif face == 2:
            new_c = 0
            new_r = (cc - faces[face][1]) + faces[6][0]
            heading = 1
        elif face == 5:
            new_c = faces[3][1]
            new_r = (cc - faces[face][1]) + face[5][0]
            heading = 1
        else:
            assert False
        # new_r = ranges_cols[cc][1]
    elif heading == 1 and new_c > ranges_rows[cr][1]:
        if face == 1:
            new_c = faces[4][1] + 49
            new_r = faces[4][0] + 49 - (cr - faces[face][0])
            heading = 3
        elif face == 3:
            new_c = (cr - faces[face][0]) + faces[1][1]
            new_r = faces[1][0] + 49
            heading = 0
        elif face == 4:
            new_c = faces[1][1] + 49
            new_r = faces[1][0] + 49 - (cr - faces[face][0])
            heading = 3
        elif face == 6:
            new_c = (cr - faces[face][0]) + faces[4][1]
            new_r = faces[4][0] + 49
            heading = 0
        else:
            assert False
        # new_c = ranges_rows[cr][0]
    elif heading == 2 and new_r > ranges_cols[cc][1]:
        if face == 1:
            new_c = faces[3][1] + 49
            new_r = (cc - faces[face][1]) + faces[3][0]
            heading = 3
        elif face == 4:
            new_c = faces[6][1] + 49
            new_r = (cc - faces[face][1]) + faces[6][0]
            heading = 3
        elif face == 6:
            new_c = (cc - faces[face][1]) + faces[1][1]
            new_r = faces[1][0]
        else:
            assert False
        # new_r = ranges_cols[cc][0]
    elif heading == 3 and new_c < ranges_rows[cr][0]:
        if face == 2:
            new_c = faces[5][1]
            new_r = faces[5][0] + 49 - (cr - faces[face][0])
            heading = 1
        elif face == 3:
            new_c = (cr - faces[face][0]) + faces[5][1]
            new_r = faces[5][0]
            heading = 2
        elif face == 5:
            new_c = faces[2][1]
            new_r = faces[2][0] + 49 - (cr - faces[face][0])
            heading = 1
        elif face == 6:
            new_c = (cr - faces[face][0]) + faces[2][1]
            new_r = faces[2][0]
            heading = 2
        else:
            assert False
        # new_c = ranges_rows[cr][1]
    if grid[(new_r, new_c)] == "#":
        break
    cr = new_r
    cc = new_c
cc += 1
cr += 1
print("Part 2:", 1000 * cr + 4 * cc + ((heading - 1) % 4))
