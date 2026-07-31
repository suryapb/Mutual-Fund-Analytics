import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# -----------------------------
# Read cleaned CSV files
# -----------------------------

fund = pd.read_csv("data/processed/fund_master_cleaned.csv")

nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")

aum = pd.read_csv("data/processed/aum_cleaned.csv")

sip = pd.read_csv("data/processed/monthly_sip_inflows_cleaned.csv")

category = pd.read_csv("data/processed/category_inflows_cleaned.csv")

folio = pd.read_csv("data/processed/industry_folio_count_cleaned.csv")

performance = pd.read_csv("data/processed/scheme_performance_cleaned.csv")

transactions = pd.read_csv("data/processed/investor_transactions_cleaned.csv")

portfolio = pd.read_csv("data/processed/portfolio_holdings_cleaned.csv")

benchmark = pd.read_csv("data/processed/benchmark_indices_cleaned.csv")

# -----------------------------
# Load into SQLite
# -----------------------------

fund.to_sql("dim_fund", engine, if_exists="replace", index=False)

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

sip.to_sql("monthly_sip_inflows", engine, if_exists="replace", index=False)

category.to_sql("category_inflows", engine, if_exists="replace", index=False)

folio.to_sql("industry_folio_count", engine, if_exists="replace", index=False)

performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

portfolio.to_sql("portfolio_holdings", engine, if_exists="replace", index=False)

benchmark.to_sql("benchmark_indices", engine, if_exists="replace", index=False)

print("====================================")
print("SQLite database created successfully!")
print("Database Name : bluestock_mf.db")
print("====================================")

# -----------------------------
# Verify Row Counts
# -----------------------------

print("\nRow Counts\n")

print("dim_fund :", len(fund))
print("fact_nav :", len(nav))
print("fact_aum :", len(aum))
print("monthly_sip_inflows :", len(sip))
print("category_inflows :", len(category))
print("industry_folio_count :", len(folio))
print("fact_performance :", len(performance))
print("fact_transactions :", len(transactions))
print("portfolio_holdings :", len(portfolio))
print("benchmark_indices :", len(benchmark))