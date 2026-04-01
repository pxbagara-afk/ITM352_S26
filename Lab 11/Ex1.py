# Read in a DCSV file and create a dataframe.
# Print some useful info.

import pandas as pd
import numpy as np
import pyarrow
import urllib.request
import ssl

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None)  # Show all columns in the output

# Create SSL context that doesn't verify certificates
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Open the URL with the custom SSL context
with urllib.request.urlopen(filename, context=context) as response:
    df = pd.read_csv(response, engine='pyarrow')

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')  # Convert order_date to datetime, coercing errors to NaT

print(df.info())
print(df.describe())
print(df.head(5))