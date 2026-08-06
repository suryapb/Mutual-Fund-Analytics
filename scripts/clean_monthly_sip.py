import pandas as pd

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print(sip.info())
print(sip.isnull().sum())

sip = sip.drop_duplicates()

# Convert month/date column
sip["month"] = pd.to_datetime(sip["month"], errors="coerce")

# Convert SIP inflow to numeric
sip["sip_inflow_crore"] = pd.to_numeric(sip["sip_inflow_crore"], errors="coerce")

# Keep positive values
sip = sip[sip["sip_inflow_crore"] >= 0]

sip.to_csv(
    "data/processed/monthly_sip_inflows_cleaned.csv",
    index=False
)

print("monthly_sip_inflows cleaned successfully!")