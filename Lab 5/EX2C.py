
trip_durations = (1.1, 0.8, 2.5, 2.6)
trip_fare = (6.25, 5.25, 10.5, 8.05)

# Explicit list of dictionaries pairing each trip's duration with its fare.
# This avoids using a for-loop or zip-to-dict conversion.
trips = [
	{"duration": 1.1, "fare": 6.25},
	{"duration": 0.8, "fare": 5.25},
	{"duration": 2.5, "fare": 10.5},
	{"duration": 2.6, "fare": 8.05},
]
print(trips)

tirp_num =input("What trip do you wanna know about? (1-4): ")
trip_index=(int(tirp_num)-1)
print(f"Duration:: {list(trips.keys())[trip_index]} miles")
print(f"fare:: ${list(trips.values())[trip_index]:.2f}")

