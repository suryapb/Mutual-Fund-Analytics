"""
Clean the mutual fund scheme performance dataset.

Converts return and expense-ratio fields to numeric values,
removes duplicate records, and validates performance metrics.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "07_scheme_performance.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "scheme_performance_cleaned.csv"
)


RETURN_COLUMNS = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
]


def clean_scheme_performance():
    """Load, clean, validate, and save scheme performance data."""

    performance = pd.read_csv(RAW_FILE)

    # Convert return columns to numeric
    for column in RETURN_COLUMNS:
        performance[column] = pd.to_numeric(
            performance[column],
            errors="coerce"
        )

    # Convert expense ratio to numeric
    performance["expense_ratio_pct"] = pd.to_numeric(
        performance["expense_ratio_pct"],
        errors="coerce"
    )

    # Remove duplicate rows
    performance = performance.drop_duplicates()

    # Remove unrealistic return values
    for column in RETURN_COLUMNS:
        performance = performance[
            (performance[column].isna())
            | (
                (performance[column] >= -100)
                & (performance[column] <= 200)
            )
        ]

    # Remove invalid expense ratios
    performance = performance[
        (performance["expense_ratio_pct"].isna())
        | (
            (performance["expense_ratio_pct"] >= 0.1)
            & (performance["expense_ratio_pct"] <= 2.5)
        )
    ]

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned dataset
    performance.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Scheme performance cleaned successfully: "
        f"{len(performance)} records saved."
    )


def main():
    """Run the scheme performance cleaning process."""
    clean_scheme_performance()


if __name__ == "__main__":
    main()