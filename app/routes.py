from flask import Blueprint

class User:
    def __init__(self, id, name, age):
        # will need to change id attribute when connecting to database
        self.id = id 
        self.name = name
        self.age = age

user_list = [
    User(1, "Johanna", 29),
    User(2, "Jeffrey", 29),
    User(3, "Katrina", 36)
]

user_bp = Blueprint("/users", __name__, url_prefix="/users")