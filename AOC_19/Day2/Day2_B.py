input = [int(i) for i in open("input").readline().split(",")]
i, j, k = 0, 0, 0
while input[0] != 19690720:
    j += 1
    i = 0
    if j == 100:
        k += 1
        j = 0
    input = [int(i) for i in open("input").readline().split(",")]
    input[1] = j
    input[2] = k
    while input[i] != 99:
        if input[i] == 1:
            input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
        elif input[i] == 2:
            input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
        i += 4
print(100 * j + k)
