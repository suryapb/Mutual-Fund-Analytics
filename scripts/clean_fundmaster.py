import pandas as pd

# Read CSV
fund= pd.read_csv("data/raw/01_fund_master.csv")

# Check data
print(fund.info())
print(fund.isnull().sum())

# Remove duplicate rows
fund = fund.drop_duplicates()

# Remove leading/trailing spaces from text columns
text_columns = fund.select_dtypes(include="object").columns

for col in text_columns:
    fund[col] = fund[col].str.strip()

# Convert launch_date to datetime
fund["launch_date"] = pd.to_datetime(fund["launch_date"], errors="coerce")

# Fill missing text values
fund = fund.fillna({
    "fund_house": "Unknown",
    "category": "Unknown",
    "sub_category": "Unknown",
    "fund_manager": "Unknown"
})

# Validate expense ratio
fund = fund[
    (fund["expense_ratio_pct"] >= 0.1) &
    (fund["expense_ratio_pct"] <= 2.5)
]

# Save
fund.to_csv(
    "data/processed/fund_master_cleaned.csv",
    index=False
)

print("fund_master cleaned successfully!")