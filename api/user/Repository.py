from database.Mongo import db
from api.user.Model import User
from uuid import uuid4


class UserRepository:
    def __init__(self):
        self.users = db.get_collection('users')

    def save(self, user: User) -> User:
        user.set_id(str(uuid4()))
        self.users.insert_one(user.dict())
        return user