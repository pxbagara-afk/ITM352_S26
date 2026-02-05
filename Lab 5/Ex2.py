# A tuple of numeric trip measurements (e.g. durations or distances).
# Tuples are immutable ordered sequences.
trip_durations = (1.1, 0.8, 2.5, 2.6)

# A tuple of fares corresponding to the trips above.
trip_fare = (6.25, 5.25, 10.5, 8.05)


# The block below attempts to create a mapping of labels to these tuples,
# but it's written incorrectly in the original file:
#
# Original (invalid):
# taxiTrips = [
#     "miles":tripdurations,
#     "fare":trip_fare
# ]
#
# Problems:
# - Square brackets produce a list; the `key:value` syntax is only valid inside
#   a dictionary (curly braces `{}`).
# - The name `tripdurations` doesn't match the defined `trip_durations`.
#
# Corrected form using a dictionary (and the correct variable names):
taxiTrips = {
    "miles": trip_durations,
    "fare": trip_fare,
}
print(f"The third trip was {taxiTrips['miles'][2]} miles.")  # Prints the third trip's details.
