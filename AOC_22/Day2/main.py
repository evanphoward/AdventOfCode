#     Part 1         Part 2
#    X  Y  Z         X  Y  Z
# A  4  8  3      A  3  4  8
# B  1  5  9      B  1  5  9
# C  7  2  6      C  2  6  7
inp = open("input").read().strip().split("\n")

p1, p2 = 0, 0
opp, you = "ABC", "XYZ"
for i in range(len(inp)):
    opp_move, you_move = inp[i].split()
    opp_move = opp.index(opp_move)
    you_move = you.index(you_move)
    p1 += ((you_move - opp_move + 1) % 3) * 3 + 1 + you_move
    p2 += (you_move * 3 + 1) + ((2 + opp_move + you_move) % 3)

print("Part 1:", p1)
print("Part 2:", p2)
