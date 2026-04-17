# create a histogram from the trip miles data
import matplotlib.pyplot as plt
import pandas as pd

# read the data file and create a dataframe
trips_df = pd.read_json("Lab 14/Trips from area 8.json")
trips_miles_series = trips_df.trip_miles

# create the histogram
plt.hist(trips_miles_series)
plt.title("Comparing frequency of trip miles")
plt.xlabel("Trip Miles")
plt.ylabel("Frequency")

plt.show()