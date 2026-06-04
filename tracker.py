import sqlite3
import pandas as pd

def init_db():

    conn = sqlite3.connect("applications.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        role TEXT,
        status TEXT,
        applied_date TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_application(company, role, status, applied_date):

    conn = sqlite3.connect("applications.db")
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO applications
        (company, role, status, applied_date)
        VALUES (?, ?, ?, ?)
        """,
        (company, role, status, applied_date)
    )

    conn.commit()
    conn.close()


def get_data():

    conn = sqlite3.connect("applications.db")

    df = pd.read_sql(
        "SELECT * FROM applications",
        conn
    )

    conn.close()

    return df
def update_status(company, new_status):

    conn = sqlite3.connect("applications.db")
    c = conn.cursor()

    c.execute(
        """
        UPDATE applications
        SET status=?
        WHERE company=?
        """,
        (new_status, company)
    )

    conn.commit()
    conn.close()