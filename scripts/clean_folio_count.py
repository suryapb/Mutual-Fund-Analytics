"""
Clean the industry folio count dataset.

Performs duplicate removal, text cleanup, date conversion,
numeric conversion, and validation of folio count values.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "06_industry_folio_count.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "industry_folio_count_cleaned.csv"
)


def clean_folio_count():
    """Load, clean, validate, and save industry folio count data."""

    folio = pd.read_csv(RAW_FILE)

    # Remove duplicate rows
    folio = folio.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    text_columns = folio.select_dtypes(include="object").columns

    for column in text_columns:
        folio[column] = folio[column].str.strip()

    # Convert month column to datetime
    folio["month"] = pd.to_datetime(
        folio["month"],
        errors="coerce"
    )

    # Convert folio count to numeric
    folio["total_folios_crore"] = pd.to_numeric(
        folio["total_folios_crore"],
        errors="coerce"
    )

    # Keep valid non-negative folio counts
    folio = folio[
        folio["total_folios_crore"] >= 0
    ]

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned dataset
    folio.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Industry folio count cleaned successfully: "
        f"{len(folio)} records saved."
    )


def main():
    """Run the industry folio count cleaning process."""
    clean_folio_count()


if __name__ == "__main__":
    main()