import pandas as pd

# Read CSV
folio= pd.read_csv("data/raw/06_industry_folio_count.csv")

# Check dataset
print(folio.info())
print(folio.isnull().sum())

# Remove duplicates
folio = folio.drop_duplicates()

# Remove spaces
text_columns = folio.select_dtypes(include="object").columns

for col in text_columns:
    folio[col] = folio[col].str.strip()

# Convert month/date
folio["month"] = pd.to_datetime(folio["month"], errors="coerce")

# Convert folio count to numeric
folio["total_folios_crore"] = pd.to_numeric(folio["total_folios_crore"], errors="coerce")

# Keep valid folio count
folio = folio[folio["total_folios_crore"] >= 0]

# Save cleaned CSV
folio.to_csv(
    "data/processed/industry_folio_count_cleaned.csv",
    index=False
)

print("industry_folio_count cleaned successfully!")