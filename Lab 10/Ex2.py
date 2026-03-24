# ...existing code...
# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]

# Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

import pandas as pd

# create a dataframe from the lists
data = {"age": ages, "gender": gender}
df = pd.DataFrame(data, index=names)

print(df)

summary=df.describe()
print(summary)

average_age_by_gender = df.groupby("gender")["age"].mean()
print("Average age by gender:", average_age_by_gender)