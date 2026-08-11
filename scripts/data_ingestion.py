"""
Data ingestion and validation for the Bluestock Mutual Fund Analytics project.

Loads all raw CSV files, performs basic structural validation, and checks
the relationship between fund master data and NAV history.
"""

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"


CSV_FILES = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
]


def validate_file(file_name):
    """Load and validate one raw CSV file."""
    file_path = RAW_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    print(f"Validated: {file_name} | Rows: {len(df)} | Columns: {len(df.columns)}")

    return df


def validate_fund_master():
    """Validate fund master and NAV history AMFI code coverage."""

    fund_master = pd.read_csv(RAW_DIR / "01_fund_master.csv")
    nav_history = pd.read_csv(RAW_DIR / "02_nav_history.csv")

    required_columns = [
        "amfi_code",
        "fund_house",
        "category",
        "sub_category",
        "risk_category",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in fund_master.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns in fund_master: {missing_columns}"
        )

    missing_codes = (
        set(fund_master["amfi_code"])
        - set(nav_history["amfi_code"])
    )

    print(f"Fund master records: {len(fund_master)}")
    print(f"NAV history records: {len(nav_history)}")
    print(f"Missing AMFI codes in NAV history: {len(missing_codes)}")

    if missing_codes:
        print("Missing codes:", missing_codes)


def main():
    """Run raw-data ingestion and validation."""

    print("=" * 60)
    print("BLUESTOCK MUTUAL FUND ANALYTICS - DATA INGESTION")
    print("=" * 60)

    for file_name in CSV_FILES:
        validate_file(file_name)

    validate_fund_master()

    print("\nData ingestion and validation completed successfully.")


if __name__ == "__main__":
    main()