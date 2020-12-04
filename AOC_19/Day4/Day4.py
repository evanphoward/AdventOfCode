def check_1(password):
    double = False
    for i in range(1, len(password)):
        if password[i] < password[i - 1]:
            double = False
            break
        if password[i] == password[i - 1]:
                double = True
    return double


def check_2(password):
    double = False
    for i in range(1, len(password)):
        if password[i] < password[i - 1]:
            double = False
            break
        if password[i] == password[i - 1] and password[i] != password[i - 2]:
            if i == len(password) - 1 or password[i] != password[i + 1]:
                double = True
    return double


min = 134792
max = 675810
total_1 = 0
total_2 = 0
for num in range(min, max + 1):
    if check_1(str(num)):
        total_1 += 1
    if check_2(str(num)):
        total_2 += 1
print("Part 1:", total_1)
print("Part 2:", total_2)
