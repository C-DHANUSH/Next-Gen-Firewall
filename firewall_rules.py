from db_config import get_db_connection
from datetime import datetime

def add_rule(data):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO firewall_rules
        (website, action, status, category, start_time, end_time)
        VALUES (%s,%s,'ACTIVE',%s,%s,%s)
    """, (
        data["website"],
        data["action"],
        data["category"],
        data["start_time"],
        data["end_time"]
    ))
    db.commit()
    cur.close()
    db.close()

def toggle_rule(rule_id):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("""
        UPDATE firewall_rules
        SET status = IF(status='ACTIVE','INACTIVE','ACTIVE')
        WHERE id=%s
    """, (rule_id,))
    db.commit()
    cur.close()
    db.close()

def get_rules():
    db = get_db_connection()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM firewall_rules")
    data = cur.fetchall()
    cur.close()
    db.close()
    return data

def log_action(site, action, status):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO firewall_logs (website, action, status)
        VALUES (%s,%s,%s)
    """, (site, action, status))
    db.commit()
    cur.close()
    db.close()

def get_logs():
    db = get_db_connection()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM firewall_logs ORDER BY log_time DESC")
    logs = cur.fetchall()
    cur.close()
    db.close()
    return logs
rules = []
logs = []
rid = 1

def add_rule(website, action):
    global rid
    rules.append({"id": rid, "website": website, "action": action, "enabled": True})
    logs.append(f"{website} → {action.upper()}")
    rid += 1

def get_rules():
    return rules

def toggle_rule(id):
    for r in rules:
        if r["id"] == id:
            r["enabled"] = not r["enabled"]

def get_logs():
    return logs
