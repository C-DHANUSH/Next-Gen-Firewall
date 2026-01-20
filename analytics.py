from db_config import get_db_connection

def firewall_stats():
    db = get_db_connection()
    cur = db.cursor()

    cur.execute("SELECT COUNT(*) FROM firewall_rules")
    rules = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM firewall_logs WHERE status='BLOCKED'")
    blocked = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM blocked_ips")
    ips = cur.fetchone()[0]

    cur.close()
    db.close()

    return {
        "rules": rules,
        "blocked": blocked,
        "ips": ips
    }
def firewall_stats():
    return {
        "rules": 6,
        "blocked": 42,
        "allowed": 118
    }
