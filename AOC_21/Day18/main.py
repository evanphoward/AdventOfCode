import math


def parse_string(num_string):
    try:
        return int(num_string[0]), num_string[2:]
    except ValueError:
        left, remaining = parse_string(num_string[1:])
        right, remaining = parse_string(remaining)
        num = [left, right]
        return num, remaining[1:]


def get_order(num, count=0):
    if isinstance(num, int):
        return count, count + 1
    left, new_count = get_order(num[0], count)
    right, new_count = get_order(num[1], new_count)
    return [left, right], new_count


def is_exploded(num, depth=0, path=[]):
    if isinstance(num, int):
        return False
    if depth == 4:
        return path
    left_path = is_exploded(num[0], depth + 1, path + [0])
    if left_path:
        return left_path
    right_path = is_exploded(num[1], depth + 1, path + [1])
    if right_path:
        return right_path
    return False


def do_explode(num, explode_path):
    def do_explode_helper(sub_num, orders, path=[]):
        if path == explode_path:
            return 0
        if isinstance(orders, int):
            if orders == index[0] - 1:
                return sub_num + pair[0]
            if orders == index[1] + 1:
                return sub_num + pair[1]
            return sub_num
        return [do_explode_helper(sub_num[0], orders[0], path + [0]), do_explode_helper(sub_num[1], orders[1], path + [1])]
    index = get_order(num)[0]
    pair = num
    for branch in explode_path:
        index = index[branch]
        pair = pair[branch]
    return do_explode_helper(num, get_order(num)[0])


def split(num):
    if isinstance(num, int):
        if num >= 10:
            return True, [math.floor(num / 2), math.ceil(num / 2)]
        return False, num
    left_split = split(num[0])
    if left_split[0]:
        return True, [left_split[1], num[1]]
    right_split = split(num[1])
    if right_split[0]:
        return True, [num[0], right_split[1]]
    return False, num


def reduce(num):
    exploded = is_exploded(num)
    if exploded:
        return reduce(do_explode(num, exploded))
    is_split, num = split(num)
    if is_split:
        return reduce(num)
    return num


def add(num1, num2):
    return reduce([num1, num2])


def magnitude(num):
    if isinstance(num, int):
        return num
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


numbers = [parse_string(num_string)[0] for num_string in open("input").read().split("\n")]
mags = []
ans = numbers[0]
for i in range(len(numbers)):
    if i > 0:
        ans = add(ans, numbers[i])
    for j in range(len(numbers)):
        if i == j:
            continue
        mags.append(magnitude(add(numbers[i], numbers[j])))
print("Part 1:", magnitude(ans))
print("Part 2:", max(mags))
