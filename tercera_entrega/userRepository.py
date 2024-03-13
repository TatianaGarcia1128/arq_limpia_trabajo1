from mysql_user_repository import MySQLUserRepository

class UserRepository:
    def __init__(self):
        pass

    
    def get_user_repo(self, user_id):
        mysql_db = MySQLUserRepository()
        user_list = mysql_db.get_users(user_id)
        return user_list