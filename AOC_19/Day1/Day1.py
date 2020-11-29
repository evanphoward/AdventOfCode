total = 0
for mass in open("input").readlines():
    curr_mass = int(mass)
    curr_mass = curr_mass // 3
    curr_mass -= 2
    total += curr_mass
print(total)
