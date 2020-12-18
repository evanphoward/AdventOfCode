from collections import deque


def matching_paren(expression, i):
    out = 0
    while out != 1:
        if expression[i] == "(":
            out -= 1
        if expression[i] == ")":
            out += 1
        i += 1
    return i - 1


def evaluate(expression, p2=False):
    stack = deque()
    i = 0
    while i < len(expression):
        val = expression[i]
        if val.isdigit():
            stack.append(int(val))
            i += 1
        elif val in "*+":
            stack.append(val)
            i += 1
        else:
            right_paren = matching_paren(expression, i + 1)
            stack.append(evaluate(expression[i+1:right_paren], p2))
            i = right_paren + 1

    if p2:
        value = stack.popleft()
        plus_stack = deque()
        while stack:
            op = stack.popleft()
            if op == "+":
                value += stack.popleft()
            else:
                plus_stack.append(value)
                plus_stack.append("*")
                value = stack.popleft()
        plus_stack.append(value)
        stack = plus_stack

    value = stack.popleft()
    while stack:
        op = stack.popleft()
        if op == "+":
            value += stack.popleft()
        else:
            value *= stack.popleft()
    return value


print(sum(evaluate([ch for ch in line.strip() if ch != " "]) for line in open("input").readlines()))
print(sum(evaluate([ch for ch in line.strip() if ch != " "], True) for line in open("input").readlines()))
