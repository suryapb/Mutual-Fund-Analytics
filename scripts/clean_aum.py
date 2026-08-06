import pandas as pd

# Read CSV
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Check dataset
print(aum.info())
print(aum.isnull().sum())

# Remove duplicates
aum = aum.drop_duplicates()

# Remove spaces from text columns
text_columns = aum.select_dtypes(include="object").columns

for col in text_columns:
    aum[col] = aum[col].str.strip()

# Convert date column (change column name if needed)
aum["date"] = pd.to_datetime(aum["date"], errors="coerce")

# Convert AUM to numeric
aum["aum_crore"] = pd.to_numeric(aum["aum_crore"], errors="coerce")

# Keep only valid AUM
aum = aum[aum["aum_crore"] > 0]

# Fill missing fund house names
aum["fund_house"] = aum["fund_house"].fillna("Unknown")

# Save cleaned file
aum.to_csv(
    "data/processed/aum_cleaned.csv",
    index=False
)

print("aum_by_fund_house cleaned successfully!")