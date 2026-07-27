print("Welcome to Mutual Fund Analytics Project")
import pandas as pd
df=pd.read_csv("data/raw/01_fund_master.csv")
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.columns)
print(df["fund_house"].unique())
print(df["category"].unique())
print(df["sub_category"].unique())
print(df["risk_category"].unique())
print(df["fund_house"].nunique())
print(df["category"].nunique())
print(df["sub_category"].nunique())
print(df["risk_category"].nunique())
print(df["fund_house"].value_counts())
csv_files=["01_fund_master.csv","02_nav_history.csv","03_aum_by_fund_house.csv","04_monthly_sip_inflows.csv",
           "05_category_inflows.csv","06_industry_folio_count.csv","07_scheme_performance.csv","08_investor_transactions.csv",
           "09_portfolio_holdings.csv","10_benchmark_indices.csv"]
for file in csv_files:
    df=pd.read_csv("data/raw/" + file)
    print("\n-----------------------")
    print("File Name:", file)
    print("Shape:", df.shape)
    print("\nData Types")
    print(df.dtypes)
    print("\nFirst 5 rows")
    print(df.head())
    print("\nMissing Values")
    print(df.isnull().sum())
    print("\nDuplicate rows")
    print(df.duplicated().sum())

        
