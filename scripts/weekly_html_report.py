from pathlib import Path
from datetime import datetime
import pandas as pd


# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "outputs"
REPORT_DIR = PROJECT_ROOT / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# Load performance data
# --------------------------------------------------

sharpe_file = OUTPUT_DIR / "sharpe_ratio.csv"
cagr_file = OUTPUT_DIR / "cagr_comparison.csv"
drawdown_file = OUTPUT_DIR / "max_drawdown.csv"


sharpe = pd.read_csv(sharpe_file)
cagr = pd.read_csv(cagr_file)
drawdown = pd.read_csv(drawdown_file)


# --------------------------------------------------
# Display column names
# --------------------------------------------------

print("Sharpe columns:", sharpe.columns.tolist())
print("CAGR columns:", cagr.columns.tolist())
print("Drawdown columns:", drawdown.columns.tolist())

# --------------------------------------------------
# Prepare report data
# --------------------------------------------------

# Merge the three performance datasets
report_data = (
    sharpe[["amfi_code", "scheme_name", "Sharpe_Ratio", "Sharpe_Rank"]]
    .merge(
        cagr[["amfi_code", "CAGR_1Y", "CAGR_3Y", "CAGR_5Y"]],
        on="amfi_code",
        how="left"
    )
    .merge(
        drawdown[["amfi_code", "Maximum_Drawdown", "Worst_Drawdown_Date"]],
        on="amfi_code",
        how="left"
    )
)

# Sort by Sharpe ratio
report_data = report_data.sort_values(
    "Sharpe_Ratio",
    ascending=False
)

print("\nTop 5 Funds:")
print(
    report_data[
        [
            "scheme_name",
            "Sharpe_Ratio",
            "CAGR_1Y",
            "CAGR_3Y",
            "CAGR_5Y",
            "Maximum_Drawdown"
        ]
    ].head(5).to_string(index=False)
)

# --------------------------------------------------
# Prepare report data
# --------------------------------------------------

report_data = (
    sharpe[["amfi_code", "scheme_name", "Sharpe_Ratio", "Sharpe_Rank"]]
    .merge(
        cagr[["amfi_code", "CAGR_1Y", "CAGR_3Y", "CAGR_5Y"]],
        on="amfi_code",
        how="left"
    )
    .merge(
        drawdown[["amfi_code", "Maximum_Drawdown", "Worst_Drawdown_Date"]],
        on="amfi_code",
        how="left"
    )
)

report_data = report_data.sort_values(
    "Sharpe_Ratio",
    ascending=False
)

print("\nTop 5 Funds:")
print(
    report_data[
        [
            "scheme_name",
            "Sharpe_Ratio",
            "CAGR_1Y",
            "CAGR_3Y",
            "CAGR_5Y",
            "Maximum_Drawdown"
        ]
    ].head(5).to_string(index=False)
)

# --------------------------------------------------
# Generate HTML report
# --------------------------------------------------

report_date = datetime.now().strftime("%d %B %Y")

top_funds = report_data.head(5)

html_table = top_funds[
    [
        "scheme_name",
        "Sharpe_Ratio",
        "CAGR_1Y",
        "CAGR_3Y",
        "CAGR_5Y",
        "Maximum_Drawdown"
    ]
].copy()

# Format numbers
html_table["Sharpe_Ratio"] = html_table["Sharpe_Ratio"].round(2)

for column in ["CAGR_1Y", "CAGR_3Y", "CAGR_5Y", "Maximum_Drawdown"]:
    html_table[column] = (
        html_table[column]
        .apply(lambda x: f"{x:.2%}" if pd.notna(x) else "N/A")
    )

html_table = html_table.rename(
    columns={
        "scheme_name": "Fund",
        "Sharpe_Ratio": "Sharpe Ratio",
        "CAGR_1Y": "1Y CAGR",
        "CAGR_3Y": "3Y CAGR",
        "CAGR_5Y": "5Y CAGR",
        "Maximum_Drawdown": "Maximum Drawdown"
    }
)

table_html = html_table.to_html(
    index=False,
    classes="performance-table",
    border=0
)


html_content = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<title>Weekly Mutual Fund Performance Report</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background-color: #f4f6f8;
    margin: 40px;
    color: #222;
}}

.container {{
    max-width: 1100px;
    margin: auto;
    background: white;
    padding: 35px;
    border-radius: 12px;
}}

h1 {{
    margin-bottom: 5px;
}}

.subtitle {{
    color: #666;
    margin-bottom: 30px;
}}

.performance-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}}

.performance-table th {{
    background-color: #1f4e78;
    color: white;
    padding: 12px;
    text-align: center;
}}

.performance-table td {{
    padding: 10px;
    border-bottom: 1px solid #ddd;
    text-align: center;
}}

.performance-table tr:hover {{
    background-color: #f2f2f2;
}}

.highlight {{
    background-color: #e8f5e9;
    padding: 15px;
    border-radius: 8px;
    margin-top: 25px;
}}

.footer {{
    margin-top: 30px;
    color: #777;
    font-size: 12px;
}}

</style>

</head>

<body>

<div class="container">

<h1>Weekly Mutual Fund Performance Report</h1>

<div class="subtitle">
Report Date: {report_date}
</div>

<h2>Top Performing Funds</h2>

<p>
Funds are ranked based on their Sharpe Ratio, which measures
risk-adjusted performance.
</p>

{table_html}

<div class="highlight">

<h3>Report Summary</h3>

<p>
The report presents the top-performing mutual funds based on
historical Sharpe Ratio, CAGR and maximum drawdown metrics.
</p>

<p>
Higher Sharpe ratios indicate stronger historical
risk-adjusted performance, while maximum drawdown represents
the largest historical decline from a peak.
</p>

</div>

<div class="footer">

Generated automatically using Python and Pandas.
Bluestock Fintech Mutual Fund Analytics Project.

</div>

</div>

</body>
</html>
"""


report_file = (
    REPORT_DIR / "Weekly_Mutual_Fund_Performance_Report.html"
)

report_file.write_text(
    html_content,
    encoding="utf-8"
)

print("\nHTML report generated successfully!")
print(report_file)