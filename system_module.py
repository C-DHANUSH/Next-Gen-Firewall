from db_config import get_db_connection
from datetime import date

def add_system(data):
    db = get_db_connection()
    cur = db.cursor()

    sql = """INSERT INTO systems
             (sid, sname, ftype, udate, remarks)
             VALUES (%s,%s,%s,%s,%s)"""

    cur.execute(sql, (
        data["sid"],
        data["sname"],
        data["ftype"],
        date.today(),
        data["remarks"]
    ))

    db.commit()
    cur.close()
    db.close()
