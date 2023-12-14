patterns = open("input").read().split("\n\n")
for i, pattern in enumerate(patterns):
    pattern = pattern.split("\n")
    grid = dict()
    for r, row in enumerate(pattern):
        for c, cell in enumerate(row):
            grid[(r, c)] = cell
    rows = [tuple(grid[(r, c)] for c in range(len(pattern[0]))) for r in range(len(pattern))]
    cols = [tuple(grid[(r, c)] for r in range(len(pattern))) for c in range(len(pattern[0]))]
    patterns[i] = (rows, cols)

cols1, rows1, cols2, rows2 = 0, 0, 0, 0


def find_reflect(lines):
    found_lines = []
    for i in range(1, len(lines)):
        differences = 0
        for j in range(min(i, len(lines) - i)):
            if lines[i - j - 1] != lines[i + j]:
                for k in range(len(lines[0])):
                    if lines[i - j - 1][k] != lines[i + j][k]:
                        differences += 1
                    if differences > 1:
                        break
        if differences < 2:
            found_lines.append((differences, i))
    return found_lines


found = False
for p_rows, p_cols in patterns:
    reflect = find_reflect(p_rows)
    if reflect:
        for part, line in reflect:
            if part == 0:
                rows1 += line
            else:
                rows2 += line
    reflect = find_reflect(p_cols)
    if reflect:
        for part, line in reflect:
            if part == 0:
                cols1 += line
            else:
                cols2 += line


print("Part 1:", cols1 + (100 * rows1))
print("Part 2:", cols2 + (100 * rows2))
