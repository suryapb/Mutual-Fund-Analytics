"""
Master execution script for the Bluestock Mutual Fund Analytics pipeline.

Runs data ingestion, cleaning, live NAV processing, SQLite loading,
and recommendation generation in sequence.
"""

import subprocess
import sys
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parent


def run_script(script_name):
    """Run a Python script and stop the pipeline if it fails."""
    script_path = SCRIPTS_DIR / script_name

    print(f"\nRunning: {script_name}")
    print("-" * 50)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        check=False
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{script_name} failed with exit code {result.returncode}"
        )

    print(f"Completed: {script_name}")


def main():
    """Run the complete Mutual Fund Analytics pipeline."""

    scripts = [
        "data_ingestion.py",
        "live_nav_fetch.py",

        "clean_fundmaster.py",
        "clean_nav.py",
        "clean_aum.py",
        "clean_monthly_sip.py",
        "clean_category_inflows.py",
        "clean_folio_count.py",
        "clean_performance.py",
        "clean_transactions.py",
        "clean_portfolio_holidays.py",
        "clean_benchmark_indices.py",

        "load_sqlite.py",
        "recommender.py",
    ]

    print("=" * 60)
    print("BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE")
    print("=" * 60)

    for script in scripts:
        run_script(script)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()