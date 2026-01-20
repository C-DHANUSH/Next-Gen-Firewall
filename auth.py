import hashlib
from db_config import get_db_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(data):
    db = get_db_connection()
    cur = db.cursor()

    sql = """INSERT INTO users
             (uid, username, password, gender, address, city, contact, dob, email)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    cur.execute(sql, (
        data["uid"],
        data["username"],
        hash_password(data["password"]),
        data["gender"],
        data["address"],
        data["city"],
        data["contact"],
        data["dob"],
        data["email"]
    ))

    db.commit()
    cur.close()
    db.close()

def login_user(data):
    db = get_db_connection()
    cur = db.cursor()

    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    cur.execute(sql, (
        data["username"],
        hash_password(data["password"])
    ))

    result = cur.fetchone()
    cur.close()
    db.close()
    return result
