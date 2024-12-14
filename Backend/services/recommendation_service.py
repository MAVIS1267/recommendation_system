import pickle
import json

with open('data/cosine_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

with open('data/movies.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('data/title_index.pkl', 'rb') as f:
    title_index = pickle.load(f)

with open('data/user_watch_history.json', 'r') as f:
    user_data = json.load(f)
    users_history = {str(user['id']): user['watch_history'] for user in user_data["users"]}


def search_movie_index(title, title_index):
    return title_index.get(title.lower(), None)


def recommend_movies(title, cosine_sim, movies, title_index, num_recommend=10):
    movie_index = search_movie_index(title, title_index)
    if movie_index is None:
        return "Your movie is not in our database, we will update soon!"
    similar_index = cosine_sim[movie_index].argsort(
        kind='quicksort')[-(num_recommend + 1):-1][::-1]
    recommended_movies = movies.iloc[similar_index]['original_title'].tolist()

    return recommended_movies


def recommend_movies_history(user_id, cosine_sim, movies, title_index, num_recommend=10):
    user_history = users_history.get(str(user_id), None)
    if not user_history:
        return {"message": "No watch history found for this user"}

    user_indices = [title_index.get(title.lower(), None)
                    for title in user_history]
    similarity_score = cosine_sim[user_indices].sum(axis=0)
    similar_movies_indices = similarity_score.argsort(
        kind='quicksort')[-(num_recommend + len(user_indices)):][::-1]
    recommended_indices = [
        index for index in similar_movies_indices if index not in user_indices][:num_recommend]

    return movies.iloc[recommended_indices]['original_title'].tolist()


if __name__ == "__main__":
    print(recommend_movies_history(1, cosine_sim, movies, title_index))
