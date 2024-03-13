from flask import Flask, request, jsonify
from user import User
from adaptador import Adaptador
from repo_user import Repo_user

app = Flask(__name__)
adaptador = Adaptador()
repo_user = Repo_user()

# Manejar la ruta raíz ("/")
@app.route('/')
def index():
    return '¡Bienvenido a mi aplicación!'

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    user_data = request.get_json()
    user_id = user_data['user_id']
    nombre = user_data['nombre']
    correo = user_data['correo']
    contrasena = user_data['contrasena']
    
    user = User(user_id=user_id, nombre=nombre, correo=correo, contrasena=contrasena)
    result = repo_user.save_user(user)

    return jsonify(result)

if __name__ == "__main__":
    adaptador.create_tables()

    # Configurar el servidor para que escuche en todas las interfaces en el puerto 5000
    app.run(host='0.0.0.0', port=9000, debug=False)