from AOC_19.IntComputer import IntProcess

# Part 1: !(A && B && C) && D
# Jump if any of the three spaces ahead of droid are holes and if the fourth tile isn't a hole
print(IntProcess(open("input")).run([ord(x) for x in "OR A J\nAND B J\nAND C J\nNOT J J\nAND D J\nWALK\n"])[-1])

# Part 2: (!(A && B && C) && D) && (E || H)
# Jump if part one conditions are true and if there is ground five or eight tiles away
print(IntProcess(open("input")).run([ord(x) for x in "OR A J\nAND B J\nAND C J\nNOT J J\nAND D J\nOR E T\nOR H T\nAND T J\nRUN\n"])[-1])
