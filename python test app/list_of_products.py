products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 45),
    ("Monitor", 300),
    ("USB Cable", 10)
]

expensive_products = list(filter(lambda product: product[1] > 100, products))
print("Products costing more than 100:")
print(expensive_products)


total = sum(price for name, price in products)
print("\nTotal cost of all products:", total)


print("\nProduct Details:")
for name, price in products:
    print(f"Product: {name} - Price: {price}")
