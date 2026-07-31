import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Check dataset
print(df.info())
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Convert date column (change column name if needed)
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert AUM to numeric
df["aum_crore"] = pd.to_numeric(df["aum_crore"], errors="coerce")

# Keep only valid AUM
df = df[df["aum_crore"] > 0]

# Fill missing fund house names
df["fund_house"] = df["fund_house"].fillna("Unknown")

# Save cleaned file
df.to_csv(
    "data/processed/aum_cleaned.csv",
    index=False
)

print("aum_by_fund_house cleaned successfully!")