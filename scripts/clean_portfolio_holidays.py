import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

# Check dataset
print(df.info())
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove spaces
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Convert portfolio date
df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"],
    errors="coerce"
)

# Keep only valid weight percentages
df = df[
    (df["weight_pct"] >= 0) &
    (df["weight_pct"] <= 100)
]

# Keep only positive market value
df = df[df["market_value_cr"] > 0]

# Keep only positive stock price
df = df[df["current_price_inr"] > 0]

# Save cleaned CSV
df.to_csv(
    "data/processed/portfolio_holdings_cleaned.csv",
    index=False
)

print("portfolio_holdings cleaned successfully!")