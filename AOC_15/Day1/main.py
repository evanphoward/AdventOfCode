print("Part 1: ", sum([1 if i == "(" else -1 for i in open("input").readline()]))
total = 0
index = 0
for i in open("input").readline():
    total = total + 1 if i == "(" else total - 1
    index += 1
    if total == -1:
        print("Part 2: ", index)
        break
