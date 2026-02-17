prices = [100,50,20,356]

total= 0 

for price in prices:
    total += price

print(f"Total price: {total}") 

item_count = 0
discounted_total = 0

for price in prices:
    item_count += 1
    if item_count > 2:
        discounted_price = price * 0.9
    else:
        discounted_price = price
    discounted_total += discounted_price

rounded_total = round(discounted_total, 2)
print(f"Rounded total price: ${rounded_total:.2f}")