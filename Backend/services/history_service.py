import json

# Load user watch history from JSON file
def load_user_watch_history(file_path='data/user_watch_history.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return {str(user['id']): user['watch_history'] for user in data['users']}
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{file_path}'.")
        return {}


# Save updated user watch history back to the JSON file
def save_user_watch_history(user_history, file_path='data/user_watch_history.json'):
    try:
        users = [{"id": int(user_id), "watch_history": history} for user_id, history in user_history.items()]
        data = {"users": users}
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"User watch history saved to '{file_path}'.")
    except Exception as e:
        print(f"Error: Failed to save user watch history. {e}")


# Add a movie to a user's watch history
def add_movie_to_history(user_id, movie_title, user_history):
    user_id = str(user_id)
    if user_id in user_history:
        if movie_title not in user_history[user_id]:
            user_history[user_id].append(movie_title)
            return f"Movie '{movie_title}' added to user {user_id}'s watch history."
        else:
            return f"Movie '{movie_title}' is already in user {user_id}'s watch history."
    else:
        return f"User ID {user_id} not found."
