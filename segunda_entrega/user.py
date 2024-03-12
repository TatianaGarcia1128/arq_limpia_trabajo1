import adaptador


def crear_user(user_id, nombre, correo, contrasena):
    db = adaptador.get_db()
    cursor = db.cursor()
    statement = 'INSERT INTO users (user_id, nombre, correo, contrasena) VALUES (?,?,?,?)'
    cursor.execute(statement, [user_id, nombre, correo, contrasena])
    db.commit()
    return True