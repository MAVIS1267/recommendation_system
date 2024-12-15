import streamlit as st
import requests
import pickle

BASE_URL = "http://localhost:8000"

movies = pickle.load(open("../Backend/data/movies.pkl", "rb"))


def similar_movies():
    st.title("Find Similar Movies")
    movie_name = st.selectbox("Select a movie", movies["original_title"].values)

    if st.button("Find Similar"):
        response = requests.get(f"{BASE_URL}/api/recommendation/recommendations", params={"title": movie_name})
        if response.status_code == 200:
            similar_movies = response.json().get("recommended_movies", [])
            st.write("Similar Movies:")
            for movie in similar_movies:
                st.write(f"- {movie}")
        else:
            st.error("Movie not found.")
