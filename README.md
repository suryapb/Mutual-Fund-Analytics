# Mutual Fund Analytics

## Project Overview

This project is part of the Bluestock Fintech Data Analytics Internship.

The objective is to analyze mutual fund data by performing data cleaning, database design, SQL analysis, and exploratory data analysis (EDA) to generate meaningful business insights.

---

## Project Structure

```
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── EDA_Analysis.ipynb
│
├── reports/
│   └── charts/
│
├── scripts/
│
├── sql/
│
├── docs/
│
├── bluestock_mf.db
├── requirements.txt
└── README.md
```

---

## Dataset

The project uses the following datasets:

- Fund Master
- NAV History
- AUM
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLite
- SQLAlchemy
- Jupyter Notebook
- Git & GitHub

---

## Tasks Completed

### Data Cleaning
- Cleaned all datasets
- Standardized date formats
- Removed duplicates
- Validated missing values
- Validated numeric fields

### Database
- Designed SQLite star schema
- Created dimension and fact tables
- Loaded cleaned datasets into SQLite

### SQL Analysis
- Wrote analytical SQL queries
- Generated business insights

### Exploratory Data Analysis
- NAV Trend Analysis
- AUM Growth Analysis
- SIP Trend Analysis
- Category Inflow Heatmap
- Investor Demographics
- Geographic Distribution
- Folio Growth Analysis
- NAV Correlation Matrix
- Sector Allocation Analysis
- Additional visualizations

More than **15 visualizations** were created and documented.

---

## Key Insights

- Mutual fund investments increased steadily between 2022 and 2025.
- SIP inflows reached record highs in 2025.
- SBI Mutual Fund maintained the highest Assets Under Management.
- Retail investor participation increased significantly.
- Equity-oriented funds attracted the highest inflows.
- Most funds showed strong positive NAV return correlation.

---

## ETL Pipeline

The project follows an end-to-end ETL workflow:

Raw Data → Data Cleaning → SQLite Database → SQL Analysis → EDA → Advanced Analytics → Power BI Dashboard

### Data Ingestion

Raw datasets are stored in:

```text
data/raw/
The data_ingestion.py script performs initial dataset inspection and validation.

Data Cleaning

The following scripts clean and validate the datasets:

clean_fundmaster.py
clean_nav.py
clean_aum.py
clean_monthly_sip.py
clean_category_inflows.py
clean_folio_count.py
clean_performance.py
clean_transactions.py
clean_portfolio.py
clean_benchmark_indices.py

Cleaned datasets are stored in:

data/processed/
Database Loading

The load_sqlite.py script loads the cleaned datasets into the SQLite database:

bluestock_mf.db
Master Pipeline

The complete pipeline can be executed using:

python scripts/run_pipeline.py

Database Design

The cleaned datasets are loaded into SQLite tables for analytical processing.

Main tables include:

Table	Description
dim_fund	Mutual fund master information
fact_nav	Historical NAV data
fact_aum	Assets under management
monthly_sip_inflows	Monthly SIP inflows
category_inflows	Category-wise inflows
industry_folio_count	Industry folio counts
fact_performance	Scheme performance
fact_transactions	Investor transactions
portfolio_holdings	Portfolio holdings
benchmark_indices	Benchmark index data
Advanced Analytics

Advanced analytics were performed to evaluate fund risk, investor behavior, portfolio concentration, and risk-adjusted performance.

Historical VaR and CVaR

Historical Value at Risk (VaR) at the 95% confidence level was calculated using the 5th percentile of daily returns.

CVaR was calculated as the mean of returns below the VaR threshold.

The funds with the highest downside-risk observations included:

SBI Small Cap Fund - Direct Plan - Growth
Axis Small Cap Fund - Regular - Growth
ABSL Small Cap Fund - Regular - Growth
Nippon India Small Cap Fund - Regular - Growth
SBI Small Cap Fund - Regular Plan - Growth

These funds were classified as Very High Risk.

Rolling 90-Day Sharpe Ratio

A rolling 90-day Sharpe ratio was calculated to evaluate risk-adjusted performance over time.

Formula:

Rolling Sharpe =
(90-day average return / 90-day standard deviation) × √252

The analysis was performed for five key funds.

Investor Cohort Analysis

Investors were grouped according to their first transaction year.

The analysis calculated:

Average SIP amount
Total invested amount
Transaction count
Top fund preference

The 2024 cohort represented a substantially larger investment base than the 2025 cohort in the available transaction data.

SIP Continuity Analysis

Investors with at least six SIP transactions were evaluated based on their average transaction gap.

Results:

Eligible investors: 1362
At-risk investors: 1332
At-risk rate: 97.8%
Continuity rate: 2.2%

Investors with an average SIP gap greater than 35 days were classified as at-risk.

Fund Recommender

A simple risk-based fund recommendation system was developed.

Users can select:

Low
Moderate
High

The system filters funds according to risk grade and ranks them using Sharpe ratio.

Example results:

Risk Grade	Fund	Sharpe Ratio
Low	ICICI Pru Liquid Fund - Regular - Growth	7.68
Low	Kotak Liquid Fund - Regular - Growth	6.18
Low	ABSL Liquid Fund - Regular - Growth	5.14
Moderate	HDFC Top 100 Fund - Regular Plan - Growth	1.06
Moderate	Mirae Asset Large Cap Fund - Regular - Growth	1.06
Moderate	ICICI Pru Bluechip Fund - Direct - Growth	1.03
High	Kotak Emerging Equity Fund - Regular - Growth	0.96
High	ICICI Pru Midcap Fund - Regular - Growth	0.95

The recommender is an analytical demonstration and should not be considered financial advice.

Sector HHI Concentration

Portfolio concentration was measured using the Herfindahl-Hirschman Index:

HHI = Σ(weight_i²)

Higher HHI indicates greater portfolio concentration.

Highest observed HHI values included:

Fund	HHI
Axis Bluechip Fund - Regular - Growth	0.206448
ABSL Small Cap Fund - Regular - Growth	0.200700
SBI Small Cap Fund - Direct Plan - Growth	0.174751
UTI Nifty 50 Index Fund - Regular - Growth	0.174709
Nippon India Large Cap Fund - Regular - Growth	0.168298
Advanced Analytics Key Findings
Small-cap funds appeared among the funds with the highest downside risk based on historical VaR and CVaR analysis.
The 2024 investor cohort contributed a substantially larger total investment amount than the 2025 cohort in the available transaction data.
SIP continuity was a major concern, with 97.8% of eligible investors classified as at-risk using the 35-day average-gap threshold.
Low-risk liquid funds showed the highest Sharpe ratios among the recommendation groups.
Axis Bluechip Fund and ABSL Small Cap Fund showed relatively high portfolio concentration based on HHI.
Power BI Dashboard

Power BI was used to create an interactive mutual fund analytics dashboard.

The dashboard provides analysis of:

Fund performance
Risk categories
NAV trends
AUM
SIP activity
Fund categories
Investor analysis
Fund comparisons
Performance metrics

Interactive slicers and filters allow users to explore the data dynamically.

Dashboard screenshots are included in the final project report and presentation.

Final Report

The final report contains:

Executive Summary
Data Sources
ETL Design
Data Cleaning
Database Design
EDA Findings
Performance Analysis
Risk Analysis
Investor Analysis
Dashboard Analysis
Key Findings
Recommendations
Limitations
Conclusion

File:

reports/Final_Report.pdf
Presentation

A 12-slide presentation was created covering:

Title
Problem and Objective
Data Sources
Project Architecture
EDA Highlights
EDA Highlights
Performance Metrics
Risk Metrics
Dashboard Analysis
Dashboard Analysis
Key Findings
Thank You

File:

reports/Bluestock_MF_Presentation.pptx
Setup Instructions

Install the required Python packages:

pip install -r requirements.txt

Run the complete pipeline from the project root:

python scripts/run_pipeline.py

The pipeline performs the required data ingestion, cleaning, database loading, and analytical processing.

To run the fund recommender separately:

python scripts/recommender.py
Limitations
Historical VaR and CVaR are based on historical return distributions.
Historical performance does not guarantee future performance.
The fund recommender is a simplified analytical model.
The recommender should not be considered financial advice.
SIP continuity results depend on the available transaction history.
HHI results depend on the available portfolio holdings data.
Some datasets are provided for internship/capstone analysis and may not represent live production data.
Future Improvements

Potential future improvements include:

Real-time NAV integration
Automated Power BI refresh
Machine-learning-based fund recommendation
Portfolio optimization
Monte Carlo risk simulation
Predictive SIP churn analysis
Automated investor alerts
Web-based deployment
Final Deliverables

The project deliverables include:

Advanced_Analytics.ipynb
var_cvar_report.csv
recommender.py
rolling_sharpe_chart.png
Final_Report.pdf
Bluestock_MF_Presentation.pptx
Cleaned datasets
SQLite database
Power BI dashboard
README.md
Project Status
 Data ingestion
 Data cleaning
 SQLite database
 SQL analysis
 Exploratory Data Analysis
 Advanced analytics
 Risk analysis
 Investor cohort analysis
 SIP continuity analysis
 Fund recommender
 HHI concentration analysis
 Power BI dashboard
 Final report
 Presentation
 Master pipeline
 README documentation




 ## Bonus Challenge B3 — Monte Carlo NAV Simulation

A Monte Carlo simulation was implemented to project possible NAV outcomes for five selected mutual funds over a 5-year horizon.

### Methodology

- Historical daily NAV data was used to calculate daily returns.
- Historical mean daily return and daily volatility were calculated for each selected fund.
- 5,000 simulated NAV paths were generated for each fund.
- The simulation horizon was 5 years using 252 trading days per year, resulting in 1,260 simulated trading days.
- 5th, 25th, 50th, 75th and 95th percentile outcomes were calculated.

### Selected Funds

- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip

### Outputs

- `outputs/monte_carlo_simulation.csv`
- `reports/charts/monte_carlo_projection.png`
- `reports/charts/monte_carlo_outcome_range.png`
- `notebooks/06_Monte_Carlo_Simulation.ipynb`

### Important Note

Monte Carlo simulation provides probabilistic scenarios based on historical return and volatility characteristics. It is not a guaranteed prediction of future NAV performance.


## Bonus Challenge B4 — Markowitz Efficient Frontier

Modern Portfolio Theory (Markowitz Portfolio Optimization) was applied to five selected mutual funds to analyze the relationship between portfolio risk and expected return.

### Selected Funds

- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip

### Methodology

- Calculated historical daily returns from NAV data.
- Calculated annualized expected returns.
- Calculated the annualized covariance matrix.
- Generated 10,000 random portfolios.
- Calculated portfolio expected return, volatility and Sharpe ratio.
- Identified the Maximum Sharpe portfolio.
- Identified the Minimum Volatility portfolio.
- Created an Efficient Frontier visualization.
- Compared optimal portfolio allocations.

### Results

| Portfolio | Expected Return | Volatility | Sharpe Ratio |
|---|---:|---:|---:|
| Maximum Sharpe | 18.96% | 6.51% | 2.91 |
| Minimum Volatility | 16.79% | 6.09% | 2.76 |

### Maximum Sharpe Portfolio Allocation

| Fund | Weight |
|---|---:|
| SBI Bluechip | 29.52% |
| Nippon Large Cap | 27.16% |
| ICICI Bluechip | 20.52% |
| Kotak Bluechip | 16.56% |
| Axis Bluechip | 6.25% |

### Outputs

- `notebooks/07_Markowitz_Portfolio_Optimization.ipynb`
- `outputs/markowitz_optimal_weights.csv`
- `outputs/markowitz_portfolio_summary.csv`
- `reports/charts/markowitz_efficient_frontier.png`
- `reports/charts/markowitz_portfolio_weights.png`

### Conclusion

The Markowitz analysis demonstrates how combining multiple mutual funds can improve diversification and provide different risk-return combinations.

The Maximum Sharpe portfolio achieved the highest simulated risk-adjusted return, while the Minimum Volatility portfolio achieved the lowest simulated portfolio risk.

The results are based on historical data and should not be interpreted as guaranteed future investment performance.
---

## Author

Surya P B

Bluestock Fintech Internship Project