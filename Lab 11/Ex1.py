# Read in a CSV file and create a dataframe
# Print some useful information

import pandas as pd
import numpy as np
import pyarrow

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pdf.set_option("display.max_columns", None)  # Show all columns

df = pd.read_csv(filename, engine="pyarrow")  # or omit engine
df [orderrdate] = pd.to_datetime(df [orderdate], format="%Y-%m-%d"), errors="coerce"

pivot_table_df.pivot_table (df, index="customerid", values="orderdate", aggfunc="count").reset_index().rename(columns={"orderdate": "num_orders"})
print(df.info())
print(df.describe())
print(df.head())