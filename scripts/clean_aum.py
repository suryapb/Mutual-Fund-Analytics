"""
Clean the AUM by fund house dataset.

Performs duplicate removal, text cleanup, date conversion,
numeric conversion, and validation of AUM values.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "03_aum_by_fund_house.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "aum_cleaned.csv"
)


def clean_aum():
    """Load, clean, validate, and save AUM data."""

    aum = pd.read_csv(RAW_FILE)

    # Remove duplicate rows
    aum = aum.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    text_columns = aum.select_dtypes(include="object").columns

    for column in text_columns:
        aum[column] = aum[column].str.strip()

    # Convert date column
    aum["date"] = pd.to_datetime(
        aum["date"],
        errors="coerce"
    )

    # Convert AUM to numeric
    aum["aum_crore"] = pd.to_numeric(
        aum["aum_crore"],
        errors="coerce"
    )

    # Keep only valid positive AUM values
    aum = aum[aum["aum_crore"] > 0]

    # Fill missing fund house names
    aum["fund_house"] = aum["fund_house"].fillna("Unknown")

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned dataset
    aum.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"AUM data cleaned successfully: "
        f"{len(aum)} records saved."
    )


def main():
    """Run the AUM cleaning process."""
    clean_aum()


if __name__ == "__main__":
    main()