import pandas as pd


# Load fund performance data
performance = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)


def recommend_funds(risk_appetite):
    risk_appetite = risk_appetite.strip().title()

    valid_risks = ["Low", "Moderate", "High"]

    if risk_appetite not in valid_risks:
        print("Please enter: Low, Moderate, or High")
        return

    filtered = performance[
        performance["risk_grade"].str.title() == risk_appetite
    ].copy()

    recommendations = (
        filtered
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    result = recommendations[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "max_drawdown_pct"
        ]
    ]

    print("\nTop 3 Recommended Funds")
    print(result.to_string(index=False))


risk = input(
    "Enter your risk appetite (Low / Moderate / High): "
)

recommend_funds(risk)