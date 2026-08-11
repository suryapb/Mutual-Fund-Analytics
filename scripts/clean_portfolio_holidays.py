"""
Clean the mutual fund portfolio holdings dataset.

Performs duplicate removal, text cleanup, date conversion,
and validation of holding weights, market values, and stock prices.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "09_portfolio_holdings.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "portfolio_holdings_cleaned.csv"
)


def clean_portfolio_holdings():
    """Load, clean, validate, and save portfolio holdings data."""

    portfolio = pd.read_csv(RAW_FILE)

    # Remove duplicate rows
    portfolio = portfolio.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    text_columns = portfolio.select_dtypes(include="object").columns

    for column in text_columns:
        portfolio[column] = portfolio[column].str.strip()

    # Convert portfolio date
    portfolio["portfolio_date"] = pd.to_datetime(
        portfolio["portfolio_date"],
        errors="coerce"
    )

    # Convert numeric columns
    portfolio["weight_pct"] = pd.to_numeric(
        portfolio["weight_pct"],
        errors="coerce"
    )

    portfolio["market_value_cr"] = pd.to_numeric(
        portfolio["market_value_cr"],
        errors="coerce"
    )

    portfolio["current_price_inr"] = pd.to_numeric(
        portfolio["current_price_inr"],
        errors="coerce"
    )

    # Keep valid portfolio weights
    portfolio = portfolio[
        (portfolio["weight_pct"] >= 0)
        & (portfolio["weight_pct"] <= 100)
    ]

    # Keep positive market values
    portfolio = portfolio[
        portfolio["market_value_cr"] > 0
    ]

    # Keep positive stock prices
    portfolio = portfolio[
        portfolio["current_price_inr"] > 0
    ]

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned dataset
    portfolio.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Portfolio holdings cleaned successfully: "
        f"{len(portfolio)} records saved."
    )


def main():
    """Run the portfolio holdings cleaning process."""
    clean_portfolio_holdings()


if __name__ == "__main__":
    main()