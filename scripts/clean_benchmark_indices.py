"""
Clean the benchmark indices dataset.

Performs duplicate removal, text cleanup, date conversion,
numeric conversion, and validation of benchmark index values.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "10_benchmark_indices.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "benchmark_indices_cleaned.csv"
)


def clean_benchmark_indices():
    """Load, clean, validate, and save benchmark index data."""

    benchmark = pd.read_csv(RAW_FILE)

    # Remove duplicate rows
    benchmark = benchmark.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    text_columns = benchmark.select_dtypes(include="object").columns

    for column in text_columns:
        benchmark[column] = benchmark[column].str.strip()

    # Convert date
    benchmark["date"] = pd.to_datetime(
        benchmark["date"],
        errors="coerce"
    )

    # Convert index value to numeric
    benchmark["close_value"] = pd.to_numeric(
        benchmark["close_value"],
        errors="coerce"
    )

    # Keep only positive index values
    benchmark = benchmark[
        benchmark["close_value"] > 0
    ]

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned dataset
    benchmark.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Benchmark indices cleaned successfully: "
        f"{len(benchmark)} records saved."
    )


def main():
    """Run the benchmark index cleaning process."""
    clean_benchmark_indices()


if __name__ == "__main__":
    main()