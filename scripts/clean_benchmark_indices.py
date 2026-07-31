import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/10_benchmark_indices.csv")

# Check dataset
print(df.info())
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Convert date
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert index value to numeric
df["close_value"] = pd.to_numeric(df["close_value"], errors="coerce")

# Keep only positive index values
df = df[df["close_value"] > 0]

# Save cleaned CSV
df.to_csv(
    "data/processed/benchmark_indices_cleaned.csv",
    index=False
)

print("benchmark_indices cleaned successfully!")