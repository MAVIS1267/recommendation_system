import json

USER_FILE = "Backend/data/users.json"

def load_users():
    """
    Load user data from the JSON file.

    Returns:
        dict: A dictionary of user data.
    """
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        raise Exception(f"Error loading user data: {str(e)}")

def save_users(users):
    """
    Save user data to the JSON file.

    Args:
        users (dict): A dictionary of user data.
    """
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def add_user(user_id, username, email):
    """
    Add a new user to the JSON file.

    Args:
        user_id (str): User ID.
        username (str): Username.
        email (str): Email address.

    Returns:
        dict: A confirmation message.
    """
    users = load_users()
    if user_id in users:
        return {"message": "User already exists"}
    users[user_id] = {"username": username, "email": email}
    save_users(users)
    return {"message": f"User {username} added successfully"}

def get_user(user_id):
    """
    Retrieve information about a specific user.

    Args:
        user_id (str): User ID.

    Returns:
        dict: The user's information or a message if not found.
    """
    users = load_users()
    return users.get(user_id, {"message": "User not found"})

def delete_user(user_id):
    """
    Delete a specific user from the JSON file.

    Args:
        user_id (str): User ID.

    Returns:
        dict: A confirmation message.
    """
    users = load_users()
    if user_id not in users:
        return {"message": "User not found"}
    del users[user_id]
    save_users(users)
    return {"message": f"User {user_id} deleted successfully"}
