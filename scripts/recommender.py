"""
Mutual fund recommendation tool.

Recommends the top three funds based on Sharpe ratio
within the user's selected risk appetite.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

PERFORMANCE_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "scheme_performance_cleaned.csv"
)

VALID_RISKS = [
    "Low",
    "Moderate",
    "High",
]


def load_performance_data():
    """Load cleaned scheme performance data."""

    if not PERFORMANCE_FILE.exists():
        raise FileNotFoundError(
            f"Performance file not found: {PERFORMANCE_FILE}"
        )

    return pd.read_csv(PERFORMANCE_FILE)


def recommend_funds(risk_appetite, performance):
    """
    Return the top three funds for a given risk appetite.

    Parameters
    ----------
    risk_appetite : str
        Investor risk preference: Low, Moderate, or High.

    performance : pandas.DataFrame
        Cleaned scheme performance dataset.

    Returns
    -------
    pandas.DataFrame
        Top three funds ranked by Sharpe ratio.
    """

    risk_appetite = risk_appetite.strip().title()

    if risk_appetite not in VALID_RISKS:
        raise ValueError(
            "Risk appetite must be Low, Moderate, or High."
        )

    filtered = performance[
        performance["risk_grade"]
        .astype("string")
        .str.strip()
        .str.title()
        == risk_appetite
    ].copy()

    recommendations = (
        filtered
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    result = recommendations[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "max_drawdown_pct",
        ]
    ]

    return result


def main():
    """Run the interactive fund recommendation tool."""

    performance = load_performance_data()

    risk = input(
        "Enter your risk appetite (Low / Moderate / High): "
    )

    try:
        result = recommend_funds(risk, performance)

        if result.empty:
            print("\nNo funds found for the selected risk appetite.")
            return

        print("\nTop 3 Recommended Funds")
        print("=" * 60)
        print(result.to_string(index=False))

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()