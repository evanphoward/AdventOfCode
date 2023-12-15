import hashlib

puz_input = open("input").read().strip()
i = 0
while hashlib.md5(str(puz_input+str(i)).encode('utf-8')).hexdigest()[:5] != "00000":
    i += 1
print("Part 1:", i)
while hashlib.md5(str(puz_input+str(i)).encode('utf-8')).hexdigest()[:6] != "000000":
    i += 1
print("Part 2:", i)
