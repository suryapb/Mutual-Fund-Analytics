import pandas as pd
transaction = pd.read_csv("data/raw/08_investor_transactions.csv")
print(transaction.head())
print(transaction.info())
print(transaction.isnull().sum())

transaction["transaction_type"] = (
    transaction["transaction_type"]
    .str.strip()
    .str.title()
)

transaction["transaction_type"] = transaction["transaction_type"].replace({
    "Sip": "SIP",
    "Lump Sum": "Lumpsum",
    "Redeem": "Redemption"
})
transaction = transaction[transaction["amount_inr"] > 0]

transaction["transaction_date"] = pd.to_datetime(transaction["transaction_date"])

valid_kyc = ["Verified", "Pending", "Rejected"]

invalid = transaction[~transaction["kyc_status"].isin(valid_kyc)]

print(invalid)
transaction = transaction.drop_duplicates()

transaction.to_csv(
    "data/processed/investor_transactions_cleaned.csv",index=False
)

print("investor_transactions cleaned successfully!")

transaction.columns