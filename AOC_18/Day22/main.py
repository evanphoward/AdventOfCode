import heapq

inp = open("input").read().split("\n")
depth = int(inp[0].split()[1])
tc, tr = tuple(map(int, inp[1].split()[1].split(",")))

DP = {(tr, tc): 0}
def erosion_level(pos):
    if pos in DP:
        return DP[pos]
    r, c = pos
    if r == 0:
        geologic_index = c * 16807
    elif c == 0:
        geologic_index = r * 48271
    else:
        geologic_index = erosion_level((r - 1, c)) * erosion_level((r, c - 1))
    DP[pos] = (geologic_index + depth) % 20183
    return DP[pos]


print("Part 1:", sum(erosion_level((r, c)) % 3 for r in range(tr + 1) for c in range(tc + 1)))

q = [((tr, tc), 0, (0, 0), 2)]
invalid_tools = [0, 2, 1]
explored = set()
while q:
    heuristic, minutes, pos, tool = heapq.heappop(q)
    if pos == (tr, tc) and tool == 2:
        print("Part 2:", minutes)
        break
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_pos = (pos[0] + dr, pos[1] + dc)
        if new_pos[0] < 0 or new_pos[1] < 0:
            continue
        if tool == invalid_tools[erosion_level(new_pos) % 3]:
            continue
        if (new_pos, tool) not in explored:
            explored.add((new_pos, tool))
            heapq.heappush(q, (abs(tr - new_pos[0]) + abs(tc - new_pos[1]) + minutes + 1, minutes + 1, new_pos, tool))
    for new_tool in range(3):
        if tool == new_tool or new_tool == invalid_tools[erosion_level(pos) % 3]:
            continue
        heapq.heappush(q, (abs(tr - pos[0]) + abs(tc - pos[1]) + minutes + 7, minutes + 7, pos, new_tool))