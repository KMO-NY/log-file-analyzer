import os
from db_handler import create_database
from log_parser import process_log_files
from report_generator import generate_summary_report

if __name__ == "__main__":
    print("🚀 Initializing Log Analyzer...")
    
    # Ensure necessary folders exist
    os.makedirs("logs", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    
    create_database()
    print("✅ Database initialized.")
    
    process_log_files()
    print("📂 Logs processed and stored in database.")
    
    generate_summary_report()
    print("📊 Summary report generated.")
