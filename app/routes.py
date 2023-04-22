from flask import Blueprint, jsonify, abort, make_response

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

@user_bp.route("", methods=["GET"])
def get_all_users():
    all_users_response = []
    for user in user_list:
        all_users_response.append({
            "id": user.id,
            "name": user.name,
            "age": user.age
        })
    return jsonify(all_users_response)

def validate_user(user_id):
    try:
        user_id = int(user_id)
    except:
        abort(make_response({"message":f"user {user_id} invalid"}, 400))
    
    for user in user_list:
        if user.id == user_id:
            return user
    
    abort(make_response({"message":f"user {user_id} not found"}, 404))

@user_bp.route("/<user_id>", methods=["GET"])
def get_specific_user(user_id):
    user = validate_user(user_id)

    return {
        "id": user.id,
        "name": user.name,
        "age": user.age
    }





