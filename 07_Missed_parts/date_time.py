import pandas as pd

df = pd.DataFrame({
    "Date": ["2025-05-10", "2025-08-15", "2026-01-20"]
})

# Convert the Date column into datetime format

df["Date"] = pd.to_datetime(df["Date"])
print(df["Date"])

# .dt → Extracts information from datetime values.

df["Year"] = df["Date"].dt.year

df["Month"] = df["Date"].dt.month

df["Day"] = df["Date"].dt.day

print(df)