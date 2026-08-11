"""
Clean the mutual fund NAV history dataset.

Performs date conversion, sorting, forward-filling of missing NAV values,
duplicate removal, and validation of positive NAV values.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "02_nav_history.csv"
OUTPUT_FILE = (
    PROJECT_ROOT / "data" / "processed" / "02_nav_history_cleaned.csv"
)


def clean_nav_history():
    """Load, clean, validate, and save NAV history data."""

    nav = pd.read_csv(RAW_FILE)

    # Convert date column to datetime
    nav["date"] = pd.to_datetime(
        nav["date"],
        errors="coerce"
    )

    # Sort by fund and date
    nav = nav.sort_values(
        by=["amfi_code", "date"]
    )

    # Fill missing NAV values within each fund
    nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

    # Remove duplicate rows
    nav = nav.drop_duplicates()

    # Keep only valid positive NAV values
    nav = nav[nav["nav"] > 0]

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned data
    nav.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"NAV history cleaned successfully: "
        f"{len(nav)} records saved."
    )


def main():
    """Run the NAV history cleaning process."""
    clean_nav_history()


if __name__ == "__main__":
    main()