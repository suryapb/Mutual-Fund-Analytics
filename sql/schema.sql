use bluestock_mf;
CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    day INTEGER,
    month INTEGER,
    year INTEGER
);CREATE DATABASE bluestock_mf;
USE bluestock_mf;
CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT
);
use bluestock_mf;
CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    aum REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

use bluestock_mf;
CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    nav REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);use bluestock_mf;
CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);use bluestock_mf;
CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    amount REAL,
    transaction_type TEXT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);use bluestock_mf;
CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    aum REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

use bluestock_mf;
CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    nav REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);use bluestock_mf;
CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);use bluestock_mf;
CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    amount REAL,
    transaction_type TEXT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);