import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/06_industry_folio_count.csv")

# Check dataset
print(df.info())
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove spaces
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Convert month/date
df["month"] = pd.to_datetime(df["month"], errors="coerce")

# Convert folio count to numeric
df["total_folios_crore"] = pd.to_numeric(df["total_folios_crore"], errors="coerce")

# Keep valid folio count
df = df[df["total_folios_crore"] >= 0]

# Save cleaned CSV
df.to_csv(
    "data/processed/industry_folio_count_cleaned.csv",
    index=False
)

print("industry_folio_count cleaned successfully!")