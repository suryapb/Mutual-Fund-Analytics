import pandas as pd
df = pd.read_csv("data/raw/08_investor_transactions.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

df["transaction_type"] = df["transaction_type"].replace({
    "Sip": "SIP",
    "Lump Sum": "Lumpsum",
    "Redeem": "Redemption"
})
df = df[df["amount_inr"] > 0]

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

valid_kyc = ["Verified", "Pending", "Rejected"]

invalid = df[~df["kyc_status"].isin(valid_kyc)]

print(invalid)
df = df.drop_duplicates()

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",index=False
)

print("investor_transactions cleaned successfully!")

df.columns