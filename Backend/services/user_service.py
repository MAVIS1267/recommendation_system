import json


# Load user information from JSON file
def load_users(file_path='data/users.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{file_path}'.")
        return {}


# Save updated user information back to the JSON file
def save_users(users, file_path='data/users.json'):
    try:
        with open(file_path, 'w') as f:
            json.dump(users, f, indent=4)
        print(f"User data saved to '{file_path}'.")
    except Exception as e:
        print(f"Error: Failed to save user data. {e}")  


# Get user by username
def get_user_by_username(username, users):
    for user_id, user_info in users.items():
        if user_info['username'].lower() == username.lower():
            return user_info
    return None


