import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "job_tracker.db"


def get_connection():
    return sqlite3.connect(DB_PATH) #This function opens a connection to the SQLite database file at DB_PATH.


def create_applications_table():
    conn = get_connection() #opens the database
    cur = conn.cursor()
    #The below things will be used to create applications table with these columns but only if it doesn't already exist.
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS applications (   
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            company_name TEXT NOT NULL,
            job_title TEXT NOT NULL,
            job_location TEXT,
            job_type TEXT,
            job_function TEXT,
            job_link TEXT,
            source TEXT,
            resume_version TEXT,
            cover_letter_used INTEGER,
            recruiter_name TEXT,
            recruiter_email TEXT,
            status TEXT NOT NULL,
            sub_status TEXT,
            priority TEXT,
            date_saved TEXT,
            date_applied TEXT,
            date_first_response TEXT,
            date_first_interview TEXT,
            date_last_interview TEXT,
            date_offer TEXT,
            date_decision TEXT,
            salary_min REAL,
            salary_max REAL,
            salary_currency TEXT,
            employment_type TEXT,
            company_size TEXT,
            industry TEXT,
            notes TEXT,
            tags TEXT
        );
        """
    )
    conn.commit() #saves any changes (here, the "create table operation")
    conn.close() #closes the connection cleanly


if __name__ == "__main__":
    create_applications_table() #This runs only when the file is executed directly like: python -m src.db_setup
    
