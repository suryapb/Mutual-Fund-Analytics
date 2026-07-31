import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()

# Convert month/date column
df["month"] = pd.to_datetime(df["month"], errors="coerce")

# Convert SIP inflow to numeric
df["sip_inflow_crore"] = pd.to_numeric(df["sip_inflow_crore"], errors="coerce")

# Keep positive values
df = df[df["sip_inflow_crore"] >= 0]

df.to_csv(
    "data/processed/monthly_sip_inflows_cleaned.csv",
    index=False
)

print("monthly_sip_inflows cleaned successfully!")