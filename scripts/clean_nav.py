import pandas as pd
df = pd.read_csv("data/raw/02_nav_history.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(
    by=["amfi_code", "date"]
)
df["nav"] = df.groupby("amfi_code")["nav"].ffill()
df = df.drop_duplicates()
df = df[df["nav"] > 0]
print(df.info())
print(df.isnull().sum())
df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print("nav_history cleaned successfully!")