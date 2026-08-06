import pandas as pd
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
print(performance.head())
print(performance.info())
print(performance.columns)
print(performance.isnull().sum())
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]
for col in return_columns:
    performance[col] = pd.to_numeric(performance[col], errors="coerce")

for col in return_columns:
    anomalies = performance[(performance[col] < -100) | (performance[col] > 200)]
    print(f"\nAnomalies in {col}:")
    print(anomalies)
invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratios:")
print(invalid_expense)
performance = performance.drop_duplicates()

performance.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("scheme_performance cleaned successfully!")

performance.columns
