"""
Clean the category-wise mutual fund inflows dataset.

Performs duplicate removal, text cleanup, date conversion,
numeric conversion, and validation of inflow values.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "05_category_inflows.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "category_inflows_cleaned.csv"
)


def clean_category_inflows():
    """Load, clean, validate, and save category inflow data."""

    category = pd.read_csv(RAW_FILE)

    # Remove duplicate rows
    category = category.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    text_columns = category.select_dtypes(include="object").columns

    for column in text_columns:
        category[column] = category[column].str.strip()

    # Convert month column to datetime
    category["month"] = pd.to_datetime(
        category["month"],
        errors="coerce"
    )

    # Convert net inflow to numeric
    category["net_inflow_crore"] = pd.to_numeric(
        category["net_inflow_crore"],
        errors="coerce"
    )

    # Keep valid non-negative inflow values
    category = category[
        category["net_inflow_crore"] >= 0
    ]

    # Fill missing category names
    category["category"] = category["category"].fillna(
        "Unknown"
    )

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned dataset
    category.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Category inflows cleaned successfully: "
        f"{len(category)} records saved."
    )


def main():
    """Run the category inflow cleaning process."""
    clean_category_inflows()


if __name__ == "__main__":
    main()