INGREDIENTS = [(int(line[2]), int(line[4]), int(line[6]), int(line[8])) for line in [line.strip().replace(",", "").split() for line in open("input").readlines()]]
CALORIES = [int(line[10]) for line in [line.strip().replace(",", "").split() for line in open("input").readlines()]]
MAX_CALORIES = max(CALORIES) * 100


def value(cookie):
    global INGREDIENTS
    attributes = [sum(cookie[j] * INGREDIENTS[j][i] for j in range(len(cookie))) for i in range(4)]
    ans = 1
    for attr in attributes:
        if attr < 0:
            ans = 0
        ans *= attr
    return ans


# Dynamic programming
# Array of every possible calorie value
# Each element is a list of the highest valued cookies that equal that amount
# We iterate over each cookie with 1..100 ingredients
# Final array contains best cookie of each calorie amount with 100 ingredients -- kind of
prev_cookies = [[] for _ in range(MAX_CALORIES + 1)]
prev_cookies[0] = [[0] * len(INGREDIENTS)]
for _ in range(100):
    new_cookies = [[] for _ in range(MAX_CALORIES + 1)]
    new_cookies[0] = [[0] * len(INGREDIENTS)]
    for cals in range(1, MAX_CALORIES + 1):
        best_ing = []
        best_vl = 0
        for j in range(len(INGREDIENTS)):
            if cals - CALORIES[j] < 0:
                continue
            for i, cookie in enumerate(prev_cookies[cals - CALORIES[j]]):
                new_cookie = cookie.copy()
                new_cookie[j] += 1
                new_value = value(new_cookie)
                if new_value > best_vl:
                    best_vl = new_value
                    best_ing = [(cals - CALORIES[j], i, j)]
                elif new_value == best_vl:
                    best_ing.append((cals - CALORIES[j], i, j))
        res = []
        for i, j, k in best_ing:
            res.append(prev_cookies[i][j].copy())
            res[-1][k] += 1
        de_duplicate = []
        [de_duplicate.append(cookie) for cookie in res if cookie not in de_duplicate]
        new_cookies[cals] = de_duplicate
    prev_cookies = new_cookies


print("Part 1:", max(value(prev_cookies[cals][0]) if len(prev_cookies[cals]) > 0 else 0 for cals in range(MAX_CALORIES + 1)))
print("Part 2:", value(prev_cookies[500][0]))
