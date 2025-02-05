import os
import re
from db_handler import insert_logs
from config import LOG_FOLDER

def parse_log_line(line):
    """Parses a log line and extracts timestamp, log level, and message."""
    log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)'
    match = re.match(log_pattern, line)
    if match:
        return match.groups()
    return None, None, None

def process_log_files():
    """Reads log files and stores extracted data in the database."""
    batch_data = []
    for log_file in os.listdir(LOG_FOLDER):
        if log_file.endswith(".log") or log_file.endswith(".txt"):
            with open(os.path.join(LOG_FOLDER, log_file), "r", encoding="utf-8") as file:
                for line in file:
                    timestamp, log_level, message = parse_log_line(line)
                    if timestamp:
                        batch_data.append((timestamp, log_level, message))
                    
                    if len(batch_data) >= 100:  # Batch insert for efficiency
                        insert_logs(batch_data)
                        batch_data.clear()
    
    # Insert remaining records
    if batch_data:
        insert_logs(batch_data)
