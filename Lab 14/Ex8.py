import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data - ensuring we use read_csv for your .csv file
file_path = "lab 14/taxi trips Fri 7_7_2017.csv"
trips_df = pd.read_csv(file_path)

# 1. Create the frequency table (Matrix)
# This counts how many times each combination of pickup and dropoff occurs
heatmap_data = pd.crosstab(
    trips_df['pickup_community_area'],
    trips_df['dropoff_community_area']
)

# 2. Set up the figure size
plt.figure(figsize=(14, 10))

# 3. Create the heatmap
# annot=False is used because there are likely too many areas to fit numbers inside cells
sns.heatmap(
    heatmap_data, 
    cmap="YlGnBu", 
    cbar_kws={'label': 'Trip Count'}
)

# 4. Add formatting and labels
plt.title("Heatmap: Pickup vs. Dropoff Community Areas", fontsize=16)
plt.xlabel("Dropoff Community Area", fontsize=12)
plt.ylabel("Pickup Community Area", fontsize=12)

# Rotate labels if they overlap
plt.xticks(rotation=90)
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()