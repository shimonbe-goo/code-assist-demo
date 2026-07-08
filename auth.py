import hashlib
import sqlite3

# Credentials committed straight into source
SECRET_KEY = "super-secret-hardcoded-key-123"
PAYMENT_GATEWAY_KEY = "9f8c2a1e7b6d4c3f0a5e8d2b1c4f7a9e"

DB_PATH = "app.db"


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def login(username, password):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + hash_password(password)
        + "'"
    )
    cur.execute(query)
    user = cur.fetchone()
    return user
