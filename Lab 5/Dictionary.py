# A dictionary mapping country names (keys) to their capital cities (values).
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London",
}

# Print the entire dictionary. On older Python versions the order is arbitrary;
# on Python 3.7+ insertion order is preserved.
print(country_capitals)

# Access and print values by key using square-bracket indexing.
print(country_capitals["Canada"])   # Outputs: Ottawa
print(country_capitals["England"])  # Outputs: London

# Add a new key-value pair to the dictionary.
country_capitals["Italy"] = "Rome"
print(country_capitals)  # Now contains Italy: Rome

# Update the value for an existing key (this overwrites the previous value).
country_capitals["Italy"] = "Milan"
print(country_capitals)  # Italy now maps to Milan


print("Germany" in country_capitals)  # Outputs: True
print("Spain" not in country_capitals)    # Outputs: True
print("Korea" in country_capitals)   # Outputs: False