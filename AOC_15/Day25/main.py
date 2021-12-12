inp = open("input").readline().replace(",", "").replace(".", "").split()
target_pos = (int(inp[15]) - 1, int(inp[17]) - 1)

grid = {(0, 0): 20151125}
r = c = 0
while target_pos not in grid:
    old_pos = (r, c)
    if r == 0:
        r = c + 1
        c = 0
    else:
        r -= 1
        c += 1
    grid[r, c] = (grid[old_pos] * 252533) % 33554393

print("Part 1:", grid[target_pos])
