import sqlite3

DB_NAME = "habit_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT,
            date TEXT NOT NULL,
            time TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_task(title, category, date, time, notes):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, category, date, time, notes) VALUES (?, ?, ?, ?, ?)",
                   (title, category, date, time, notes))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY date, time")
    rows = cursor.fetchall()
    conn.close()
    return rows
