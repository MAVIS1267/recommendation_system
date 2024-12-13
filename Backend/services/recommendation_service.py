import pickle

with open('Backend/data/cosine_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

with open('Backend/data/movies.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('Backend/data/title_index.pkl', 'rb') as f:
    title_index = pickle.load(f)

def search_movie_index(title, title_index):
    return title_index.get(title.lower(), None)

def recommend_movies(title, cosine_sim, movies, title_index, num_recommend=10   ):
    movie_index = search_movie_index(title, title_index)
    if movie_index is None:
        return "Your movie is not in our database, we will update soon!"
    similar_index = cosine_sim[movie_index].argsort(kind='quicksort')[-(num_recommend + 1):-1][::-1]
    recommended_movies = movies.iloc[similar_index]['original_title']

    return recommended_movies

def recommend_movies_history(user_id, cosine_sim, movies, title_index, history, num_recommend=10):
    user_history = history.get(user_id, [])
    if not user_history:
        return {"message": "No watch history found for this user"}
    
    # Tạo một vector one-hot cho user history
    user_vector = [1 if title_index.get(title.lower(), None) in user_history else 0 for title in title_index]
    
    # Tính cosine similarity giữa user vector và tất cả các vector phim
    sim_scores = cosine_sim.dot(user_vector)
    
    # Sắp xếp theo thứ tự giảm dần và lấy ra num_recommend phim
    similar_index = sim_scores.argsort(kind='quicksort')[-(num_recommend+1):-1][::-1]
    recommended_movies = movies.iloc[similar_index]['title']
    return recommended_movies.tolist()
