"""
Clean the mutual fund master dataset.

Performs duplicate removal, text cleanup, date conversion,
missing-value handling, and expense-ratio validation.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "01_fund_master.csv"
OUTPUT_FILE = (
    PROJECT_ROOT / "data" / "processed" / "fund_master_cleaned.csv"
)


def clean_fund_master():
    """Load, clean, validate, and save the fund master dataset."""

    fund = pd.read_csv(RAW_FILE)

    # Remove duplicate rows
    fund = fund.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    text_columns = fund.select_dtypes(include="object").columns

    for column in text_columns:
        fund[column] = fund[column].str.strip()

    # Convert launch date to datetime
    fund["launch_date"] = pd.to_datetime(
        fund["launch_date"],
        errors="coerce"
    )

    # Fill missing text values
    fund = fund.fillna(
        {
            "fund_house": "Unknown",
            "category": "Unknown",
            "sub_category": "Unknown",
            "fund_manager": "Unknown",
        }
    )

    # Validate expense ratio
    fund = fund[
        (fund["expense_ratio_pct"] >= 0.1)
        & (fund["expense_ratio_pct"] <= 2.5)
    ]

    # Create output directory if needed
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Save cleaned dataset
    fund.to_csv(OUTPUT_FILE, index=False)

    print(
        f"Fund master cleaned successfully: "
        f"{len(fund)} records saved."
    )


def main():
    """Run the fund master cleaning process."""
    clean_fund_master()


if __name__ == "__main__":
    main()