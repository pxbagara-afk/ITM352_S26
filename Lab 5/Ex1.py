# A dictionary representing information about a taxi trip.
taxiTripInfo = {
    "trip_id": "da7a62fce",   # unique identifier (string)
    "trip_seconds": 360,       # duration in seconds (int)
    "trip_miles": 1.1,         # distance in miles (float)
    "fare": "6.25",          # fare as a string (could also be a float)
}

# Print the entire dictionary (shows all key-value pairs).
print(taxiTripInfo)

# Access a single value by its key using square brackets.
print(taxiTripInfo["trip_miles"])  # prints the numeric distance (1.1)

# The following line is incorrect: using parentheses attempts to call the
# dictionary like a function and will raise a TypeError.
# Correct form would be: print(taxiTripInfo["trip_miles"])
print(taxiTripInfo(trip_miles))