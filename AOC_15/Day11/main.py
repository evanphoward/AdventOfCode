def step(password):
    password = list(password)
    i = len(password) - 1
    while ord(password[i]) == 122:
        password[i] = "a"
        i -= 1
    password[i] = chr(ord(password[i]) + 1)
    return ''.join(password)


def valid(password):
    if "i" in password or "o" in password or "l" in password:
        return False

    is_valid = False
    first = second = False
    for i in range(len(password) - 1):
        if i < len(password) - 2 and ord(password[i + 1]) == ord(password[i]) + 1 and ord(password[i + 2]) == ord(password[i]) + 2:
            is_valid = True
        if password[i] == password[i + 1]:
            if first:
                second = password[i]
            else:
                first = password[i]
    if not all([first, second, is_valid]) or first == second:
        return False

    return True


passwd = "cqjxjnds"
while not valid(passwd):
    passwd = step(passwd)
print("Part 1:", passwd)
passwd = step(passwd)
while not valid(passwd):
    passwd = step(passwd)
print("Part 2:", passwd)
