import itertools
from AOC_19.IntComputer import IntProcess

droid = IntProcess(open("input"))
# I played the game manually to pick up all the items and reach the pressure floor and recorded the inputs here
inp = [110, 111, 114, 116, 104, 10, 116, 97, 107, 101, 32, 97, 115, 116, 114, 111, 110, 97, 117, 116, 32, 105, 99, 101, 32, 99, 114, 101, 97, 109, 10, 115, 111, 117, 116, 104, 10, 119, 101, 115, 116, 10, 116, 97, 107, 101, 32, 109, 111, 117, 115, 101, 10, 110, 111, 114, 116, 104, 10, 116, 97, 107, 101, 32, 111, 114, 110, 97, 109, 101, 110, 116, 10, 119, 101, 115, 116, 10, 110, 111, 114, 116, 104, 10, 116, 97, 107, 101, 32, 101, 97, 115, 116, 101, 114, 32, 101, 103, 103, 10, 110, 111, 114, 116, 104, 10, 119, 101, 115, 116, 10, 110, 111, 114, 116, 104, 10, 116, 97, 107, 101, 32, 119, 114, 101, 97, 116, 104, 10, 115, 111, 117, 116, 104, 10, 101, 97, 115, 116, 10, 115, 111, 117, 116, 104, 10, 101, 97, 115, 116, 10, 116, 97, 107, 101, 32, 104, 121, 112, 101, 114, 99, 117, 98, 101, 10, 110, 111, 114, 116, 104, 10, 101, 97, 115, 116, 10, 116, 97, 107, 101, 32, 112, 114, 105, 109, 101, 32, 110, 117, 109, 98, 101, 114, 10, 119, 101, 115, 116, 10, 115, 111, 117, 116, 104, 10, 119, 101, 115, 116, 10, 115, 111, 117, 116, 104, 10, 119, 101, 115, 116, 10, 119, 101, 115, 116, 10]
out = droid.run(inp)
items = ["ornament", "hypercube", "prime number", "astronaut ice cream", "mouse", "wreath", "easter egg"]
for hold_item in itertools.product([False, True], repeat=7):
    inp = ""
    for i in range(7):
        inp = inp + ("take " if hold_item[i] else "drop ") + items[i] + "\n"
    inp = inp + "north\n"
    inp = [ord(x) for x in inp]
    out = droid.run(inp)
    if droid.ip == -1:
        break

print(''.join(chr(x) for x in out))