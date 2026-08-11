"""
Load cleaned Mutual Fund Analytics datasets into a SQLite database.

Creates the Bluestock mutual fund database and loads each cleaned
dataset into its corresponding analytical table.
"""

from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


PROJECT_ROOT = Path(__file__).resolve().parents[1]

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DATABASE_FILE = PROJECT_ROOT / "bluestock_mf.db"

ENGINE = create_engine(
    f"sqlite:///{DATABASE_FILE}"
)


DATASETS = {
    "dim_fund": "fund_master_cleaned.csv",
    "fact_nav": "02_nav_history_cleaned.csv",
    "fact_aum": "aum_cleaned.csv",
    "monthly_sip_inflows": "monthly_sip_inflows_cleaned.csv",
    "category_inflows": "category_inflows_cleaned.csv",
    "industry_folio_count": "industry_folio_count_cleaned.csv",
    "fact_performance": "scheme_performance_cleaned.csv",
    "fact_transactions": "investor_transactions_cleaned.csv",
    "portfolio_holdings": "portfolio_holdings_cleaned.csv",
    "benchmark_indices": "benchmark_indices_cleaned.csv",
}


def load_dataset(table_name, file_name):
    """Load one cleaned CSV file into a SQLite table."""

    file_path = PROCESSED_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(
            f"Cleaned file not found: {file_path}"
        )

    dataframe = pd.read_csv(file_path)

    dataframe.to_sql(
        table_name,
        ENGINE,
        if_exists="replace",
        index=False,
    )

    return len(dataframe)


def main():
    """Load all cleaned datasets into SQLite."""

    print("=" * 60)
    print("BLUESTOCK MUTUAL FUND ANALYTICS - SQLITE LOAD")
    print("=" * 60)

    row_counts = {}

    for table_name, file_name in DATASETS.items():
        count = load_dataset(table_name, file_name)
        row_counts[table_name] = count

    print("\nSQLite database created successfully.")
    print(f"Database: {DATABASE_FILE.name}")

    print("\nRow Counts")
    print("-" * 40)

    for table_name, count in row_counts.items():
        print(f"{table_name:<30} {count:,}")


if __name__ == "__main__":
    main()