# Ask the user to enter their birth eyar. Calcualte their age based on the current year (2026) and print it out.
# Name: Paul Bagara
# Date: January 20, 2026

birth_year_input = input("Please enter your birth year:")
birth_year_input = int(birth_year_input)
current_year = 2026
age = current_year - birth_year_input
print ( "You entered:", birth_year_input)
print (f"You are {age} years old")