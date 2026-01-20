from db_config import get_db_connection

def add_firewall(data):
    db = get_db_connection()
    cur = db.cursor()

    sql = """INSERT INTO firewall
             (sname, password, type, serial_no, mdate, validity)
             VALUES (%s,%s,%s,%s,%s,%s)"""

    cur.execute(sql, (
        data["sname"],
        data["password"],
        data["type"],
        data["serial_no"],
        data["mdate"],
        data["validity"]
    ))

    db.commit()
    cur.close()
    db.close()
