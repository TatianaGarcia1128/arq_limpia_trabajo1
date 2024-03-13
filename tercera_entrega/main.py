from user_controller import UserController
from mysql_user_repository import MySQLUserRepository

#Instance class controller
user_controller = UserController()
mysql = MySQLUserRepository()

mysql.create_tables()

#Use method get_user
user_id=1
return_user_controller = user_controller.get_user_controller(user_id=user_id)

#Print rsult
print(return_user_controller)