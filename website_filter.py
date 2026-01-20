from firewall_rules import get_rules, log_action
from datetime import datetime

def check_website(site):
    rules = get_rules()
    now = datetime.now().time()

    for r in rules:
        if r["website"] in site and r["status"] == "ACTIVE":

            if r["start_time"] and r["end_time"]:
                if not (r["start_time"] <= now <= r["end_time"]):
                    continue

            log_action(site, r["action"], "BLOCKED" if r["action"]=="BLOCK" else "ALLOWED")
            return r["action"]

    log_action(site, "ALLOW", "ALLOWED")
    return "ALLOW"
def detect_suspicious(site):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("""
      SELECT COUNT(*) FROM firewall_logs
      WHERE website=%s AND status='BLOCKED'
    """, (site,))
    count = cur.fetchone()[0]
    cur.close()
    db.close()
    return count >= 3
