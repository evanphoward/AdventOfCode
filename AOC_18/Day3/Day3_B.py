fabric = [[0] * 1000 for i in range(1000)]
dict = {i : [] for i in range(1000*1000)}
for line in open("input").readlines():
    parts = line.split(' ')
    temp = parts[2].split(',')
    row = int(temp[0])
    col = int(temp[1][0:-1])
    temp = parts[3].split('x')
    for r in range(int(temp[0])):
        for c in range(int(temp[1])):
            fabric[row+r][col+c] += 1
            dict[(row+r)*1000+(col+c)].append(int(parts[0][1:]))

sum = 0
labels = set(range(1265))
for i in range(1000*1000):
    if len(dict[i]) > 1:
        for label in dict[i]:
            labels.discard(label-1)

print(list(labels)[0]+1)