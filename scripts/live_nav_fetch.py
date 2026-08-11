"""
Fetch latest NAV data for selected mutual funds using the MFAPI service.

The downloaded NAV files are saved in the project's data/raw directory.
"""

from pathlib import Path

import pandas as pd
import requests


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

FUNDS = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841,
}


def fetch_nav(fund_name, amfi_code):
    """Fetch NAV history for one mutual fund and save it as CSV."""

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    if "data" not in data:
        raise ValueError(
            f"NAV data not available for {fund_name} ({amfi_code})"
        )

    nav_df = pd.DataFrame(data["data"])

    output_file = RAW_DIR / f"{fund_name}.csv"
    nav_df.to_csv(output_file, index=False)

    print(f"Saved: {output_file}")


def main():
    """Fetch NAV data for all configured funds."""

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("LIVE NAV DATA FETCH")
    print("=" * 60)

    for fund_name, amfi_code in FUNDS.items():
        fetch_nav(fund_name, amfi_code)

    print("\nLive NAV data fetched successfully.")


if __name__ == "__main__":
    main()