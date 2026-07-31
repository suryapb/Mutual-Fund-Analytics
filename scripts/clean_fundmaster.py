import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/01_fund_master.csv")

# Check data
print(df.info())
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove leading/trailing spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Convert launch_date to datetime
df["launch_date"] = pd.to_datetime(df["launch_date"], errors="coerce")

# Fill missing text values
df = df.fillna({
    "fund_house": "Unknown",
    "category": "Unknown",
    "sub_category": "Unknown",
    "fund_manager": "Unknown"
})

# Validate expense ratio
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Save
df.to_csv(
    "data/processed/fund_master_cleaned.csv",
    index=False
)

print("fund_master cleaned successfully!")