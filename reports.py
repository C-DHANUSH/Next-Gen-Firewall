import csv
from db_config import get_db_connection

def generate_user_report():
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT uid, username, email FROM users")

    with open("user_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["User ID", "Username", "Email"])
        for row in cur.fetchall():
            writer.writerow(row)

    cur.close()
    db.close()
