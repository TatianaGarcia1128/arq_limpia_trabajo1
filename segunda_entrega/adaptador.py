import sqlite3
DATABASE_NAME = 'arq_limpia.db'

class Adaptador:
    def __init__(self) -> None:
        pass

    def get_db(self):
        conn = sqlite3.connect(DATABASE_NAME)
        return conn

    def create_tables(self):
        tables = [
            """CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,   
                contrasena TEXT NOT NULL
            )"""
        ]
        db = self.get_db()
        cursor = db.cursor()

        for table in tables:
            cursor.execute(table)

    def execute_query(self, query, parametros=None):
        cursor = self.get_db()
        if parametros:
            cursor.execute(query, parametros)
            cursor.commit()