total = 0
for mass in open("input").readlines():
    running_total = 0
    curr_mass = int(mass)
    while curr_mass > 0:
        curr_mass = curr_mass // 3
        curr_mass -= 2
        if curr_mass > 0:
            running_total += curr_mass
    total += running_total
print(total)