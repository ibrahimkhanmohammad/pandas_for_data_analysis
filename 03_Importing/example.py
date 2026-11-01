import pandas as pd

df = pd.read_csv("../all_files/data.csv", index_col ="Name")

pokemon = input("Enter any pokemon to check it's stats: ")

try:
    print(df.loc[pokemon])

except KeyError:
    print(f"{pokemon} does not exist in the list")