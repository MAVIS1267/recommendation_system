import json

HISTORY_FILE = "data/user_watch_history.json"

def load_history():
    """
    Load watch history data from the JSON file.

    Returns:
        dict: A dictionary of user watch history.
    """
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        raise Exception(f"Error loading watch history: {str(e)}")

def save_history(history):
    """
    Save watch history data to the JSON file.

    Args:
        history (dict): A dictionary of user watch history.
    """
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def add_watch_history(user_id, movie_title):
    """
    Add a movie to the user's watch history.

    Args:
        user_id (str): User ID.
        movie_title (str): Movie title to be added.

    Returns:
        dict: A confirmation message.
    """
    history = load_history()
    if user_id not in history:
        history[user_id] = []
    if movie_title not in history[user_id]:
        history[user_id].append(movie_title)
    save_history(history)
    return {"message": f"Added '{movie_title}' to {user_id}'s watch history"}

def get_watch_history(user_id):
    """
    Retrieve the watch history of a specific user.

    Args:
        user_id (str): User ID.

    Returns:
        list: A list of movies the user has watched.
    """
    history = load_history()
    return history.get(user_id, {"message": "No watch history found for this user"})

def delete_watch_history(user_id):
    """
    Delete the watch history of a specific user.

    Args:
        user_id (str): User ID.

    Returns:
        dict: A confirmation message.
    """
    history = load_history()
    if user_id not in history:
        return {"message": "User not found in watch history"}
    del history[user_id]
    save_history(history)
    return {"message": f"Deleted watch history for user {user_id}"}
