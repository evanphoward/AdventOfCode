import regex
rules, messages = [line.strip() for line in open("input").read().split("\n\n")]
rules = dict([line.strip().split(": ") for line in rules.split("\n")])


def get_rule(rulenum, p2):
    if p2:
        if rulenum == '8':
            return get_rule('42', p2) + '+'
        elif rulenum == '11':
            return '(' + get_rule('42', p2) + '(?1)*' + get_rule('31', p2) + ')'

    return rules[rulenum][1] if regex.fullmatch('"[ab]"', rules[rulenum]) else \
        "(?:" + '|'.join([''.join(get_rule(num, p2) for num in rule_set.split())
                          for rule_set in rules[rulenum].split(" | ")]) + ")"


full_regex = get_rule('0', False)
print("Part 1:", sum(bool(regex.fullmatch(full_regex, message)) for message in messages.split("\n")))
full_regex = get_rule('0', True)
print("Part 1:", sum(bool(regex.fullmatch(full_regex, message)) for message in messages.split("\n")))

