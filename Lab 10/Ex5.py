# ...existing code...
#read in a CSV file of homes data and create a dataframe
#Do some filtering and statistics on the data
import pandas as pd
df_homes = pd.read_csv("Lab 10/homes_data.csv")

shape = df_homes.shape
print(f"The homes data has {shape[0]} rows and {shape[1]} columns.")

print(df_homes.head())
print(df_homes.describe())

#select only the properties with 500 units or more units
df_large_properties = df_homes[df_homes["units"] >= 500]
df_large_properties = df_homes.loc[df_large_properties.index].drop(columns=["id", "easement"])
print(df_large_properties.head(10))

#convert columns to appropriate data types
df_large_properties["sale_price"] =pd.to_numeric(df_large_properties["sale_price"], errors="coerce")
df_large_properties["land_sqft"] = pd.to_numeric(df_large_properties["land_sqft"], errors="coerce")
df_large_properties["gross_sqft"] = pd.to_numeric(df_large_properties["gross_sqft"], errors="coerce")

#drop rows with missing values in the numberica columns
df_large_properties= df_large_properties.dropna()

#drop duplicate rows
df_large_properties = df_large_properties.drop_duplicates()

print(df_large_properties.head(10))
