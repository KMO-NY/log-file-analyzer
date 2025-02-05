# Handles database operations

import sqlite3
from config import DB_NAME

def create_database():
    """Creates the database and logs table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            log_level TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_logs(batch_data):
    """Inserts a batch of logs into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO logs (timestamp, log_level, message) VALUES (?, ?, ?)", batch_data)
    conn.commit()
    conn.close()
