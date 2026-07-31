import pandas as pd
df = pd.read_csv("data/raw/07_scheme_performance.csv")
print(df.head())
print(df.info())
print(df.columns)
print(df.isnull().sum())
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]
for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

for col in return_columns:
    anomalies = df[(df[col] < -100) | (df[col] > 200)]
    print(f"\nAnomalies in {col}:")
    print(anomalies)
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratios:")
print(invalid_expense)
df = df.drop_duplicates()

df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("scheme_performance cleaned successfully!")

df.columns
