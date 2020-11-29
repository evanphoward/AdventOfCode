def react(polymer):
    i = 1
    while i < len(polymer):
        if abs(ord(polymer[i])-ord(polymer[i-1])) == 32:
            polymer = polymer[:i-1] + polymer[i+1:]
            i -= 2
        i += 1
    return len(polymer), polymer.strip()


poly = react(open('input').readline())[1]
print("Part 1:", len(poly))
print("Part 2:", sorted([(react(poly.replace(chr(i), '').replace(str.upper(chr(i)), '')), chr(i)) for i in range(97, 123)])[0][0][0])
