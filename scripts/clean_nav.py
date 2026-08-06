import pandas as pd
nav = pd.read_csv("data/raw/02_nav_history.csv")
print(nav.head())
print(nav.info())
print(nav.isnull().sum())
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(
    by=["amfi_code", "date"]
)
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]
print(nav.info())
print(nav.isnull().sum())
nav.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print("nav_history cleaned successfully!")