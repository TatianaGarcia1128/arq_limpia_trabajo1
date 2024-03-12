import sqlite3
DATABASE_NAME = 'arq_limpia.db'

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,   
            contrasena TEXT NOT NULL
        )"""
    ]
    db = get_db()
    cursor = db.cursor()

    for table in tables:
        cursor.execute(table)