mapping = {"one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def check_mapping(string, ind, p2):
    if p2:
        if len(string) > ind + 2 and string[ind: ind + 3] in mapping:
            return mapping[string[ind: ind + 3]]
        elif len(string) > ind + 3 and string[ind: ind + 4] in mapping:
            return mapping[string[ind: ind + 4]]
        elif len(string) > ind + 4 and string[ind: ind + 5] in mapping:
            return mapping[string[ind: ind + 5]]
    return string[ind] if string[ind].isdigit() else ""


def get_ans(p2):
    ans = 0
    for x in open("input").read().split("\n"):
        test = ''.join([check_mapping(x, i, p2) for i in range(len(x))])
        ans += int(test[0] + test[-1])
    return ans


print("Part 1:", get_ans(False))
print("Part 2:", get_ans(True))
