input = open("input").readline()
input = [int(i) for i in input.split(",")]
i = 0
input[1] = 12
input[2] = 2
while input[i] != 99:
    if input[i] == 1:
        input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
    elif input[i] == 2:
        input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
    i += 4
print(input[0])