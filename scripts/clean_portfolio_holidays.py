import pandas as pd

# Read CSV
portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

# Check dataset
print(portfolio.info())
print(portfolio.isnull().sum())

# Remove duplicates
portfolio = portfolio.drop_duplicates()

# Remove spaces
text_columns = portfolio.select_dtypes(include="object").columns

for col in text_columns:
    portfolio[col] = portfolio[col].str.strip()

# Convert portfolio date
portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"],
    errors="coerce"
)

# Keep only valid weight percentages
portfolio = portfolio[
    (portfolio["weight_pct"] >= 0) &
    (portfolio["weight_pct"] <= 100)
]

# Keep only positive market value
portfolio = portfolio[portfolio["market_value_cr"] > 0]

# Keep only positive stock price
portfolio = portfolio[portfolio["current_price_inr"] > 0]

# Save cleaned CSV
portfolio.to_csv(
    "data/processed/portfolio_holdings_cleaned.csv",
    index=False
)

print("portfolio_holdings cleaned successfully!")