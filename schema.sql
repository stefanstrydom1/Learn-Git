DROP TABLE IF EXISTS cases;

CREATE TABLE cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    insured_name TEXT NOT NULL,
    layer_name TEXT NOT NULL,
    frequency DECIMAL,
    severity DECIMAL,
    target_loss_ratio DECIMAL,
    expected_loss DECIMAL,
    technical_premium DECIMAL
);