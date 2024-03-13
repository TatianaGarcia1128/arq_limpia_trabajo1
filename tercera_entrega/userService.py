
class UserService:
    def __init__(self, user_repo_object):
        self.user_repo_object = user_repo_object

    def get_user(self, user_id):
        return self.user_repo_object.get_user_repo(user_id)