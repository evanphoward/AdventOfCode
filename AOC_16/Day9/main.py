def decompress(s, p1):
    if not "(" in s:
        return len(s)

    first_paren = s.index("(")
    if first_paren == 0:
        close_paren = s.index(")")
        marker = s[1:close_paren].split("x")
        length = int(marker[0])
        num = int(marker[1])
        if p1:
            return (len(s[close_paren+1:close_paren+1+length]) * num) + decompress(s[close_paren+1+length:], p1)
        else:
            return (decompress(s[close_paren+1:close_paren+1+length], p1) * num) + decompress(s[close_paren+1+length:], p1)
    else:
        return len(s[:first_paren]) + decompress(s[first_paren:], p1)
        

print("Part 1:", decompress(open("input").readline(), True))
print("Part 2:", decompress(open("input").readline(), False))