fabric = [[0] * 1000 for i in range(1000)]
for line in open("input").readlines():
    parts = line.split(' ')
    temp = parts[2].split(',')
    row = int(temp[0])
    col = int(temp[1][0:-1])
    temp = parts[3].split('x')
    for r in range(int(temp[0])):
        for c in range(int(temp[1])):
            fabric[row+r][col+c] += 1
sum = 0
for row in range(1000):
    for col in range(1000):
        if fabric[row][col] >= 2:
            sum += 1

print(sum)