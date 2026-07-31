use bluestock_mf;
CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);