# Data Dictionary

## dim_fund (Source: 01_fund_master.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Unique AMFI code of the mutual fund |
| fund_house | Text | Name of the fund house |
| scheme_name | Text | Name of the mutual fund scheme |
| category | Text | Fund category (Equity, Debt, Hybrid, etc.) |
| sub_category | Text | Fund sub-category |
| launch_date | Date | Date when the scheme was launched |
| expense_ratio_pct | Float | Expense ratio of the fund |

---

## fact_nav (Source: 02_nav_history.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## fact_aum (Source: 03_aum_by_fund_house.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| fund_house | Text | Fund house name |
| date | Date | Reporting date |
| aum | Float | Assets Under Management (₹ Crores) |

---

## monthly_sip_inflows (Source: 04_monthly_sip_inflows.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| sip_inflow | Float | Monthly SIP inflow amount |

---

## category_inflows (Source: 05_category_inflows.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| category | Text | Mutual fund category |
| month | Date | Reporting month |
| inflow | Float | Net inflow amount |

---

## industry_folio_count (Source: 06_industry_folio_count.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| folio_count | Integer | Number of investor folios |

---

## fact_performance (Source: 07_scheme_performance.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| return_1y | Float | One-year return (%) |
| return_3y | Float | Three-year return (%) |
| return_5y | Float | Five-year return (%) |
| expense_ratio | Float | Expense ratio (%) |

---

## fact_transactions (Source: 08_investor_transactions.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| transaction_id | Integer | Unique transaction ID |
| amfi_code | Integer | Mutual fund identifier |
| transaction_type | Text | SIP, Lumpsum or Redemption |
| amount | Float | Transaction amount |
| transaction_date | Date | Date of transaction |
| kyc_status | Text | Investor KYC status |

---

## portfolio_holdings (Source: 09_portfolio_holdings.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| stock_symbol | Text | Stock symbol |
| stock_name | Text | Company name |
| sector | Text | Industry sector |
| weight_pct | Float | Portfolio allocation (%) |
| market_value_cr | Float | Market value (₹ Crores) |
| current_price_inr | Float | Current market price |
| portfolio_date | Date | Portfolio reporting date |

---

## benchmark_indices (Source: 10_benchmark_indices.csv)

| Column | Data Type | Description |
|---------|-----------|-------------|
| benchmark_name | Text | Benchmark index name |
| date | Date | Trading date |
| index_value | Float | Index closing value |