from flask import Flask, request, jsonify
import user
import adaptador

app = Flask(__name__)

# Manejar la ruta raíz ("/")
@app.route('/')
def index():
    return '¡Bienvenido a mi aplicación!'


# @app.after_request
# def after_request(response):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Credentials"] = "true"
#     response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
#     response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF"
#     return response

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    user_data = request.get_json()
    user_id = user_data['user_id']
    nombre = user_data['nombre']
    correo = user_data['correo']
    contrasena = user_data['contrasena']
    result = user.crear_user(user_id=user_id, nombre=nombre, correo=correo, contrasena=contrasena)
    return jsonify(result)

if __name__ == "__main__":
    adaptador.create_tables()

    # Configurar el servidor para que escuche en todas las interfaces en el puerto 5000
    app.run(host='0.0.0.0', port=9000, debug=False)