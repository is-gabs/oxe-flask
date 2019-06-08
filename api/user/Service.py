from api.user.Repository import UserRepository
from api.user.Model import User


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user: User):
        user = self.user_repository.save(user)
        return user