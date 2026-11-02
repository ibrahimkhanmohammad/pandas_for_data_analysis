import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara", "John", "Aisha"],
    "Age": [21, 24, 22, 25, 23],
    "Marks": [85, 90, 78, 88, 95],
    "City": ["Hyderabad", "Delhi", "Mumbai", "Chennai", "Bangalore"]
}

df = pd.DataFrame(data)

# 1. head(n) - Displays the first n rows.
print(df.head(3))

# 2. tail(n) - Displays the last n rows.
print(df.tail(2))

# 3. info() - Provides information about your DataFrame.
print(df.info())

# 4. describe() - Provides statistical information about numerical columns.
print(df.describe())