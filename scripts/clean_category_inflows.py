import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/05_category_inflows.csv")

# Check dataset
print(df.info())
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove leading/trailing spaces
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Convert date/month column
df["month"] = pd.to_datetime(df["month"], errors="coerce")

# Convert inflow to numeric
df["net_inflow_crore"] = pd.to_numeric(df["net_inflow_crore"], errors="coerce")

# Keep valid inflow values
df = df[df["net_inflow_crore"] >= 0]

# Fill missing category
df["category"] = df["category"].fillna("Unknown")

# Save cleaned CSV
df.to_csv(
    "data/processed/category_inflows_cleaned.csv",
    index=False
)

print("category_inflows cleaned successfully!")