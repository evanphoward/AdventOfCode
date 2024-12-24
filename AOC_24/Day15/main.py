from MiscFiles.library import *

ans = 0

grid, moves = get_input(2024, 15).split("\n\n")

moves_dirs = {'>': DIRS[1], '^': DIRS[0], 'v': DIRS[2], '<': DIRS[3]}
moves = [moves_dirs[x] for x in list(''.join(moves.split('\n')))]
grid, nr, nc = get_grid(grid)

boxes_p1, boxes_p2 = [], []
grid_p2 = dict()
for r in range(nr):
    for c in range(nc):
        if grid[(r,c)] == 'O':
            grid[(r, c)] = '.'
            boxes_p1.append([(r, c), (r, c)])
            boxes_p2.append([(r, 2 * c), (r, 2 * c + 1)])
        elif grid[(r, c)] == '@':
            grid[(r, c)] = '.'
            starting_pos = (r, c)
        grid_p2[(r, 2 * c)] = grid_p2[(r, 2 * c + 1)] = grid[(r, c)]
nc *= 2

def get_box(r, c):
    global boxes
    for i, box in enumerate(boxes):
        if (r, c) == box[0] or (r, c) == box[1]:
            return i
    return None

def move_into(r, c, dr, dc):
    global grid, boxes
    box_index = get_box(r, c)
    if box_index is None:
        if grid[(r, c)] == '.':
            return []
        else:
            return None
    left_pos, right_pos = boxes[box_index]
    new_left = (left_pos[0] + dr, left_pos[1] + dc)
    new_right = (right_pos[0] + dr, right_pos[1] + dc)

    update_left = move_into(new_left[0], new_left[1], dr, dc) if dc != 1 else []
    update_right = move_into(new_right[0], new_right[1], dr, dc) if dc != -1 else []
    if update_left is not None and update_right is not None:
        updates = update_left + update_right + [(box_index, (new_left, new_right))]
        return updates
    else:
        return None


def simulate(p2):
    global grid, boxes
    rr, rc = starting_pos
    boxes = boxes_p2 if p2 else boxes_p1
    grid = grid_p2 if p2 else grid
    if p2:
        rc *= 2
    for dr, dc in moves:
        updates = move_into(rr + dr, rc + dc, dr, dc)
        if updates is not None:
            for box_index, update in updates:
                boxes[box_index] = update
            rr += dr
            rc += dc
    return sum((100 * box[0][0]) + box[0][1] for box in boxes)



print("Part 1:", simulate(False))
print("Part 2:", simulate(True))
