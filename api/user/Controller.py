from flask import Blueprint, request, jsonify, abort
from api.user.Model import User
from api.user.Service import UserService

users = Blueprint('Users', __name__, url_prefix='/users')
user_service = UserService()


@users.route('', methods=['POST'])
def create_user():
    user = request.get_json()
    try:
        user = User(**user)
        user = user_service.create_user(user)
        return jsonify(user.dict()), 201
    except TypeError:
        abort(400)