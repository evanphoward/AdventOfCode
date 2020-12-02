total_1 = 0
total_2 = 0
for line in open("input").readlines():
    line = line.split(" ")
    min, max = [int(i) for i in line[0].split("-")]
    character = line[1][0]
    word = [char for char in line[2]]
    if min <= word.count(character) <= max:
        total_1 += 1
    if bool(word[min-1] == character) != bool(word[max-1] == character):
        total_2 += 1

print("Part 1:", total_1)
print("Part 2:", total_2)
