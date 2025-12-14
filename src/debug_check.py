#TO Double check if the rows are really in the database, a quick verification step:

from .db_setup import get_connection

def show_applications():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, company_name, job_title, status FROM applications;")
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        print(row)

if __name__ == "__main__":
    show_applications()
