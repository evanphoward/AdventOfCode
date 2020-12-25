card_loop = 0
value = 1
while value != 8421034:
    value = (value * 7) % 20201227
    card_loop += 1
value = 1
for _ in range(card_loop):
    value = (value * 15993936) % 20201227
print(value)