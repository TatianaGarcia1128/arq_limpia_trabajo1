from flask import Flask, render_template, request, jsonify
from user_controller import UserController
from mysql_user_repository import MySQLUserRepository

app = Flask(__name__)
mysql_user_repository = MySQLUserRepository()

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/buscar_usuario', methods=['POST'])
def buscar_usuario():
    user_id = request.form.get('userId')

    user_controller = UserController()
    user = user_controller.get_user_controller(user_id=user_id)
    #Instance class controller
    user_controller = UserController()

    #Use method get_user
    return_user_controller = user_controller.get_user_controller(user_id=user_id)

    if user:
        return jsonify({'user': return_user_controller})
    else:
        return jsonify({'error': 'Usuario no encontrado'})

if __name__ == '__main__':
    mysql_user_repository.create_tables()
   #mysql_user_repository.ingresar_datos()

    app.run(host='0.0.0.0', port=8000, debug=True)