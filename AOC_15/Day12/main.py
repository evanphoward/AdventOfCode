import json


def has_red(obj):
    return "red" in obj.values()


def get_nums(js, p1):
    if isinstance(js, int):
        return js
    if isinstance(js, list):
        return sum(get_nums(elt, p1) for elt in js)
    if isinstance(js, dict):
        if p1 or not has_red(js):
            return sum(get_nums(elt, p1) for elt in js.values())
    return 0


js = json.loads(open("input.json").readline())
print("Part 1:", get_nums(js, True))
print("Part 2:", get_nums(js, False))