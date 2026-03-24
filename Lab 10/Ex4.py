#Read a JSON file of taxi trip data and create a dataframe
import json
import pandas as pd

taxi_df = pd.read_json("Lab 10/taxi_trips.json")
print (taxi_df.describe())

print(taxi_df.head())
print(taxi_df["fare"].median())
