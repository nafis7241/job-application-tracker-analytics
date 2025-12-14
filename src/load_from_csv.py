import sqlite3
from pathlib import Path

import pandas as pd

from .db_setup import get_connection


CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "applications_raw.csv"


def load_csv_into_db():
    # Read CSV into a DataFrame
    df = pd.read_csv(CSV_PATH)

    # Connect to SQLite
    conn = get_connection()
    cur = conn.cursor()

    # Insert rows one by one (fine for small data)
    insert_sql = """
        INSERT INTO applications (
            company_name,
            job_title,
            job_location,
            job_type,
            job_function,
            job_link,
            source,
            resume_version,
            cover_letter_used,
            recruiter_name,
            recruiter_email,
            status,
            sub_status,
            priority,
            date_saved,
            date_applied,
            date_first_response,
            date_first_interview,
            date_last_interview,
            date_offer,
            date_decision,
            salary_min,
            salary_max,
            salary_currency,
            employment_type,
            company_size,
            industry,
            notes,
            tags
        )
        VALUES (
            :company_name,
            :job_title,
            :job_location,
            :job_type,
            :job_function,
            :job_link,
            :source,
            :resume_version,
            :cover_letter_used,
            :recruiter_name,
            :recruiter_email,
            :status,
            :sub_status,
            :priority,
            :date_saved,
            :date_applied,
            :date_first_response,
            :date_first_interview,
            :date_last_interview,
            :date_offer,
            :date_decision,
            :salary_min,
            :salary_max,
            :salary_currency,
            :employment_type,
            :company_size,
            :industry,
            :notes,
            :tags
        )
    """

    for _, row in df.iterrows():
        cur.execute(insert_sql, row.to_dict())

    conn.commit()
    conn.close()


if __name__ == "__main__":
    load_csv_into_db()
