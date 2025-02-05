-- SQL script to define database schema

CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    log_level TEXT,
    message TEXT
);
