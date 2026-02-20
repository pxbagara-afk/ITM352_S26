data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

# Get input from user
user_input = input("Enter a value to add to the tuple: ")

# Create a new tuple with the added value
data = data + (user_input,)

# Print updated tuple
print("Updated tuple:", data)

data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

user_input = input("Enter a value to add to the tuple: ")

# This will cause an error
data.append(user_input)

print(data)





data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

user_input = input("Enter a value to add to the tuple: ")

try:
    # This line will trigger an AttributeError because tuples lack .append()
    data.append(user_input)
except AttributeError as e:
    print("An attempt was made to append a value to the tuple.")
    print(f"System Error Message: {e}")

print("\nFinal data state:", data)