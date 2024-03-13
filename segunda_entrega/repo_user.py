from adaptador import Adaptador

adaptador = Adaptador()

class Repo_user:
    def __init__(self):
        pass
        
    def save_user(self, user_object):
        statement = 'INSERT INTO users (user_id, nombre, correo, contrasena) VALUES (?,?,?,?)'
        print(user_object.user_id, user_object)
        adaptador.execute_query(statement, (user_object.user_id, user_object.nombre, user_object.correo, user_object.contrasena))
        return True
    