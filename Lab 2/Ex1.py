# Ask the user for a number between 1 and 100. Square the number and print the number and its square.
# Name: Paul Bagara
# Date: January 20, 2026
print("Welcome to the Program")
value_entered = input("Please enter a decimal number between 1 and 100: ")
print("You entered:", value_entered)

value_as_integer = int(value_entered)
squared_value = value_as_integer ** 2
print("The square of the number you entered is:", squared_value)
print(f "The square of {value_as_integer} is {squared_value}.")
# Note: The above code does not handle invalid input or out-of-range values.