from userService import UserService
from userRepository import UserRepository

class UserController:
    def __init__(self) -> None:
        pass

    def get_user_controller(self, user_id):
        user_repo_object = UserRepository()
        user_service_object = UserService(user_repo_object)

        user_return = user_service_object.get_user(user_id)

        return user_return