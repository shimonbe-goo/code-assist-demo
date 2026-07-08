import sqlite3

DB_PATH = "app.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def find_user(username):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, username FROM users WHERE username = ?",
            (username,),
        )
        return cur.fetchone()
    finally:
        conn.close()
