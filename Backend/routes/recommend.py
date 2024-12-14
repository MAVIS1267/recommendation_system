from fastapi import APIRouter, HTTPException
from services.recommendation_service import recommend_movies, recommend_movies_history
import pickle
import json

router = APIRouter()

with open('data/cosine_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

with open('data/movies.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('data/title_index.pkl', 'rb') as f:
    title_index = pickle.load(f)

with open('data/user_watch_history.json', 'r') as f:
    user_data = json.load(f)
    users_history = {str(user['id']): user['watch_history'] for user in user_data["users"]}

@router.get("/recommendations")
def get_recommendations(title: str, num_recommend: int = 10):
    """Get recommendations based on a movie title."""
    recommendations = recommend_movies(title, cosine_sim, movies, title_index, num_recommend)
    if isinstance(recommendations, str):  # Check if recommendation returns an error message
        raise HTTPException(status_code=404, detail=recommendations)
    return {"recommended_movies": recommendations}

@router.get("/recommendations/user/{user_id}")
def get_user_recommendations(user_id: int, num_recommend: int = 10):
    """Get personalized recommendations based on user's watch history."""
    user_recommendations = recommend_movies_history(user_id, cosine_sim, movies, title_index, num_recommend)
    if isinstance(user_recommendations, dict):  # If no recommendations found
        raise HTTPException(status_code=404, detail=user_recommendations["message"])
    return {"user_id": user_id, "recommended_movies": user_recommendations}
