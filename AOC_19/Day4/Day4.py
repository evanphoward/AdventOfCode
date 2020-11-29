def check(password):
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
total = 0
for num in range(min, max + 1):
    if check(str(num)):
        total += 1
print(total)
