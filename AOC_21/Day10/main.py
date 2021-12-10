from collections import deque
inp = [line for line in open("input").read().split("\n")]
closer = {"(": ")", "{": "}", "<": ">", "[": "]"}
closer_scores_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
closer_scores_2 = {")": 1, "]": 2, "}": 3, ">": 4}


def get_score(chunk, p1=False):
    stack = deque()
    for ch in chunk:
        if ch in ["(", "{", "<", "["]:
            stack.append(ch)
        else:
            opener = stack.pop()
            if p1 and closer[opener] != ch:
                return closer_scores_1[ch]
    if p1:
        return 0
    ans = ''.join([closer[opener] for opener in stack])[::-1]
    score = 0
    for ch in ans:
        score *= 5
        score += closer_scores_2[ch]
    return score


print("Part 1:", sum(get_score(line, True) for line in open("input").read().split("\n")))
incomplete = [line for line in open("input").read().split("\n") if get_score(line, True) == 0]
scores = sorted(list(map(get_score, incomplete)))
print("Part 2:", scores[len(scores) // 2])


