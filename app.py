from flask import Flask
from api.user.Controller import users

def create_app():
    app = Flask(__name__)
    app.register_blueprint(users)
    return app