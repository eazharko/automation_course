products = {
    "apple": 3,
    "banana": 2,
    "orange": 4
}
total_price = 0

for product, price in products.items():
    total_price += price
    print(f"{product} -> {price}")
print(f"Total: {total_price}")


