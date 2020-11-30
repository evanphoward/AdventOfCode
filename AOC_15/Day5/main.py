import re

nice_1 = 0
nice_2 = 0
for word in open("input").readlines():
    if re.search("[aeiou].*[aeiou].*[aeiou]", word) is not None:
        if re.search(r"(.)\1", word) is not None:
            if re.search("ab|cd|pq|xy", word) is None:
                nice_1 += 1
    if re.search(r"(..).*\1", word) is not None:
        if re.search(r"(.).\1", word) is not None:
            nice_2 += 1

print("Part 1:", nice_1, "\nPart 2:", nice_2)
