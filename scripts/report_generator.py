import sqlite3
import pandas as pd
from config import DB_NAME, REPORTS_FOLDER

def generate_summary_report():
    """Generates a summary report from stored logs."""
    conn = sqlite3.connect(DB_NAME)
    query = """
        SELECT log_level, COUNT(*) as count FROM logs 
        GROUP BY log_level ORDER BY count DESC;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Save to CSV
    output_file = f"{REPORTS_FOLDER}/summary_report.csv"
    df.to_csv(output_file, index=False)
    print(f"Summary report saved as {output_file}")
