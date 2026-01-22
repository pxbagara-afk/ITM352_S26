#Ask the user to enter their weight in pounds
#Convert the weight to (1pound=0453502 kg)
#name: Paul Bagara
#date: January 22, 2026

kg_to_pounds = 0.453502

weight_in_pounds = input("Please enter your weight in pounds: ")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kg = weight_in_pounds_float * kg_to_pounds   
weight_in_kg = round(weight_in_kg)

print("You entered:", weight_in_pounds)
print(f"Your weight in kilograms is: {weight_in_kg} kg")