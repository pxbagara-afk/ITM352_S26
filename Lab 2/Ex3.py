# Ask the User to enter a floating point number,
 #Square the number, Printout the original numnber 
# and the squared result
# Name: Paul Bagara
# Date: January 22, 2026

input_value = input("Please enter a floating point number: ")
float_value = float(input_value)
squared_value = float_value ** 2

print("You entered:", input_value)
print(f"The square of {float_value} is {squared_value}.")

# round the number to 2 decimal places
rounded_squared_value = round(squared_value, 2)

print("you entered:", float_value)
print(f"The square of {float_value} rounded to 2 decimal places is {rounded_squared_value}.")