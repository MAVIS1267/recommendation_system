import json

def load_user():
    with open('data/users.json', 'r') as f:
        users_data = json.load(f)
    return users_data

def login(email, password):
    users_data = load_user()
    for user_id, user_data in users_data.items():
        if user_data['email'] == email:
            if user_data['password'] == password:
                return {
                    "status": True,
                    "user": {
                        "user_id": user_data['user_id'],
                        "username": user_data['username'],
                        "email": user_data['email']
                    }
                }
            return {
                "status": False,
                "message": "Invalid password"
            }
    return {
        "status": False,
        "message": "Email not found"
    }
        