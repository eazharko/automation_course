prices = {
    "keyboard": 100,
    "mouse": 40,
    "monitor": 250,
    "usb": 15
}
max_price = 0

for price in prices.values():
    if price > max_price:
        max_price = price

for item, price in prices.items():
    if price == max_price:
        print(f"{item}: {price}")


