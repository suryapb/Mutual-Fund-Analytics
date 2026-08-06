import pandas as pd

# Read CSV
category = pd.read_csv("data/raw/05_category_inflows.csv")

# Check dataset
print(category.info())
print(category.isnull().sum())

# Remove duplicates
category = category.drop_duplicates()

# Remove leading/trailing spaces
text_columns = category.select_dtypes(include="object").columns

for col in text_columns:
    category[col] = category[col].str.strip()

# Convert date/month column
category["month"] = pd.to_datetime(category["month"], errors="coerce")

# Convert inflow to numeric
category["net_inflow_crore"] = pd.to_numeric(category["net_inflow_crore"], errors="coerce")

# Keep valid inflow values
category = category[category["net_inflow_crore"] >= 0]

# Fill missing category
category["category"] = category["category"].fillna("Unknown")

# Save cleaned CSV
category.to_csv(
    "data/processed/category_inflows_cleaned.csv",
    index=False
)

print("category_inflows cleaned successfully!")