"""
Clean the investor transactions dataset.

Standardizes transaction types, validates transaction amounts and dates,
checks KYC status values, and removes duplicate transactions.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "08_investor_transactions.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "investor_transactions_cleaned.csv"
)


VALID_KYC_STATUS = [
    "Verified",
    "Pending",
    "Rejected",
]


def clean_transactions():
    """Load, clean, validate, and save investor transaction data."""

    transaction = pd.read_csv(RAW_FILE)

    # Standardize transaction types
    transaction["transaction_type"] = (
        transaction["transaction_type"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    transaction["transaction_type"] = transaction[
        "transaction_type"
    ].replace(
        {
            "Sip": "SIP",
            "Lump Sum": "Lumpsum",
            "Redeem": "Redemption",
        }
    )

    # Convert transaction amount to numeric
    transaction["amount_inr"] = pd.to_numeric(
        transaction["amount_inr"],
        errors="coerce"
    )

    # Keep positive transaction amounts
    transaction = transaction[
        transaction["amount_inr"] > 0
    ]

    # Convert transaction date
    transaction["transaction_date"] = pd.to_datetime(
        transaction["transaction_date"],
        errors="coerce"
    )

    # Standardize KYC status
    transaction["kyc_status"] = (
        transaction["kyc_status"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    # Remove invalid KYC records
    transaction = transaction[
        transaction["kyc_status"].isin(VALID_KYC_STATUS)
    ]

    # Remove duplicate transactions
    transaction = transaction.drop_duplicates()

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned dataset
    transaction.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Investor transactions cleaned successfully: "
        f"{len(transaction)} records saved."
    )


def main():
    """Run the investor transaction cleaning process."""
    clean_transactions()


if __name__ == "__main__":
    main()