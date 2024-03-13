import sqlite3
DATABASE_NAME = 'arq_limpia.db'


class MySQLUserRepository:
    def __init__(self) -> None:
        pass

    def _get_db(self):
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    
    def get_users(self, user_id):
        db = self._get_db()
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE user_id = ?"
        data = (user_id,)
        cursor.execute(query, data)
        user_data = cursor.fetchone()
        cursor.close()
        return user_data
    
    def create_tables(self):
        tables = [
            """CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,   
                contrasena TEXT NOT NULL
            )"""
        ]
        db = self._get_db()
        cursor = db.cursor()

        for table in tables:
            cursor.execute(table)