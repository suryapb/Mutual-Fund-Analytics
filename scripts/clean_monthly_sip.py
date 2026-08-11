"""
Clean the monthly SIP inflows dataset.

Performs duplicate removal, date conversion, numeric conversion,
and validation of SIP inflow values.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "04_monthly_sip_inflows.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "monthly_sip_inflows_cleaned.csv"
)


def clean_monthly_sip():
    """Load, clean, validate, and save monthly SIP inflow data."""

    sip = pd.read_csv(RAW_FILE)

    # Remove duplicate rows
    sip = sip.drop_duplicates()

    # Convert month column to datetime
    sip["month"] = pd.to_datetime(
        sip["month"],
        errors="coerce"
    )

    # Convert SIP inflow to numeric
    sip["sip_inflow_crore"] = pd.to_numeric(
        sip["sip_inflow_crore"],
        errors="coerce"
    )

    # Keep valid non-negative SIP inflows
    sip = sip[sip["sip_inflow_crore"] >= 0]

    # Create output directory if necessary
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save cleaned dataset
    sip.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Monthly SIP inflows cleaned successfully: "
        f"{len(sip)} records saved."
    )


def main():
    """Run the monthly SIP cleaning process."""
    clean_monthly_sip()


if __name__ == "__main__":
    main()