-- ==========================================================
-- Query 1: Top 5 Fund Houses by Assets Under Management (AUM)
-- ==========================================================
SELECT
    fund_house,
    ROUND(AVG(aum_crore),2) AS average_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY average_aum DESC
LIMIT 5;


-- ==========================================================
-- Query 2: Average NAV for Each Fund
-- ==========================================================
SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY average_nav DESC;


-- ==========================================================
-- Query 3: Monthly Average NAV
-- ==========================================================
SELECT
    substr(date,1,7) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY substr(date,1,7)
ORDER BY month;


-- ==========================================================
-- Query 4: Number of Schemes by Fund House
-- ==========================================================
SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;


-- ==========================================================
-- Query 5: Category-wise Net Inflow
-- ==========================================================
SELECT
    category,
    SUM(net_inflow_crore) AS total_net_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_net_inflow DESC;


-- ==========================================================
-- Query 6: Top 5 States by Investment Amount
-- ==========================================================
SELECT
    state,
    ROUND(SUM(amount_inr),2) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 5;


-- ==========================================================
-- Query 7: Month-wise SIP Inflow
-- ==========================================================
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- ==========================================================
-- Query 8: Top 10 Schemes by 5-Year Return
-- ==========================================================
SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- ==========================================================
-- Query 9: Funds with Expense Ratio Less Than 1%
-- ==========================================================
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- ==========================================================
-- Query 10: Sector-wise Portfolio Market Value
-- ==========================================================
SELECT
    sector,
    ROUND(SUM(market_value_cr),2) AS total_market_value
FROM portfolio_holdings
GROUP BY sector
ORDER BY total_market_value DESC;