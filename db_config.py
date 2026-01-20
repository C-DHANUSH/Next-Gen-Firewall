import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="firewall_user",
        password="firewall123",
        database="nextgen_firewall",
        auth_plugin="mysql_native_password"
    )
