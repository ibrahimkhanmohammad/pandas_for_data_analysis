# Data cleaning = the process of fixing/removing:
#           incomplete, incorrect, or irrelevant data.
#           ~75% of work done with Pandas is data cleaning


import pandas as pd
df = pd.read_csv("../all_files/data.csv")

print(df)

# 1. Dropping irrelevant columns

dropped_df  = df.drop(columns=["No", "Legendary"])
print(dropped_df)

# 2. Handling missing data

new_df = df.dropna(subset=["Type2"])
print(new_df)

# - better not to remove the entire row but instead fill it with other data by

df = df.fillna({"Type2": "None"})
print(df)

# 3. fix inconsistent values

df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Water": "WATER", "Fire": "FIRE"})
print(df)

# 4. Standardize text

# df["Name"] = df["Name"].str.upper()
# df["Name"] = df["Name"].str.lower()
# df["Name"] = df["Name"].str.title()
# df["Name"] = df["Name"].str.strip().str.lower()
# df["Name"] = df["Name"].str.len()

# print(df["Name"])

# 5. Type casting

df["Legendary"] = df["Legendary"].astype(bool)
print(df["Legendary"])

# 6. Removing duplicate entries

df = df.drop_duplicates()
print(df)







