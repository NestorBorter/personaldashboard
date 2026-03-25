import sqlite3

def get_database():
    db = sqlite3.connect("dashboard.db")
    print("Opened database!")
    return db

def init_db():
    db = get_database()
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    db.commit()
    db.close()
