#This program demonstrates variable scope in Python.
#name:Paul Bagara   
#Date: January 27, 2026

def calculate_discounted_price(price):
    global discount
    discount=0.9
    price=price*discount
    print (f"Inside function, discounted price: {price:.2f}")
    return price

price=100
original_price= float (input("Enter the original price: (price.2f) "))
discounted_price= calculate_discounted_price(price)
print (f"Outside function, original price: {original_price:.2f}")

print(f"Original price after function call: {price:.2f}")
print (f"Discount: {discount}")