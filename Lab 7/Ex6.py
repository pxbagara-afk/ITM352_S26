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


data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

user_input = input("Enter a value to add to the tuple: ")

try:
    # This will still fail because .append() doesn't exist for tuples
    data.append(user_input)
except AttributeError:
    # Handling the error by creating a new tuple via concatenation
    # Note: (user_input,) with a comma creates a single-element tuple
    data = data + (user_input,)
    print("Direct append failed. Handled by creating a new concatenated tuple.")



data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

user_input = input("Enter a value to add to the tuple: ")

try:
    # This will still trigger the AttributeError
    data.append(user_input)
except AttributeError as e:
    print(f"Caught Error: {e}")
    
    # 1. Recast (convert) the tuple to a list
    temp_list = list(data)
    
    # 2. Now we can use .append() because it's a list
    temp_list.append(user_input)
    
    # 3. Cast it back to a tuple and assign it to 'data'
    data = tuple(temp_list)
    
    print("Success: Converted to list, appended value, and converted back to tuple.")