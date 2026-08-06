import pandas as pd

# Read CSV
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

# Check dataset
print(benchmark.info())
print(benchmark.isnull().sum())

# Remove duplicates
benchmark = benchmark.drop_duplicates()

# Remove spaces from text columns
text_columns = benchmark.select_dtypes(include="object").columns

for col in text_columns:
    benchmark[col] = benchmark[col].str.strip()

# Convert date
benchmark["date"] = pd.to_datetime(benchmark["date"], errors="coerce")

# Convert index value to numeric
benchmark["close_value"] = pd.to_numeric(benchmark["close_value"], errors="coerce")

# Keep only positive index values
benchmark = benchmark[benchmark["close_value"] > 0]

# Save cleaned CSV
benchmark.to_csv(
    "data/processed/benchmark_indices_cleaned.csv",
    index=False
)

print("benchmark_indices cleaned successfully!")