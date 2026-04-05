prices = [100, 250, 80, 320, 150]

new_prices = map(lambda x: x + x * 10/100, prices)
new_prices = list(new_prices)
print(new_prices)