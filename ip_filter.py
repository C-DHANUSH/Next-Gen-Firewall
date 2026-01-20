from db_config import get_db_connection

def block_ip(ip, reason):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("INSERT INTO blocked_ips (ip_address, reason) VALUES (%s,%s)", (ip, reason))
    db.commit()
    cur.close()
    db.close()

def is_ip_blocked(ip):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM blocked_ips WHERE ip_address=%s", (ip,))
    result = cur.fetchone()
    cur.close()
    db.close()
    return result is not None
