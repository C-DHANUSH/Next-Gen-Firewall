from db_config import get_db_connection

def generate_security_key(data):
    db = get_db_connection()
    cur = db.cursor()

    sql = """INSERT INTO security_keys
             (keycode, fid, skey, details)
             VALUES (%s,%s,%s,%s)"""

    cur.execute(sql, (
        data["keycode"],
        data["fid"],
        data["skey"],
        data["details"]
    ))

    db.commit()
    cur.close()
    db.close()
