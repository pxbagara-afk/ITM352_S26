# Ask the user to enter a temperature in Fahrenheit
# Convert the temperature to Celsius using the formula: C = (F - 32) * 5/9
# Print out the original Fahrenheit temperature and the converted Celsius temperature.
# Name: Paul Bagara
# Date: January 22, 2026

fahrenheit_input = input("Please enter a temperature in Fahrenheit: ")
fahrenheit_float = float(fahrenheit_input)
celsius_temp = (fahrenheit_float - 32) * 5 / 9
celsius_temp_rounded = round(celsius_temp, 1)

print("You entered:", fahrenheit_input)
print(f"The temperature in Celsius is: {celsius_temp_rounded} °C")