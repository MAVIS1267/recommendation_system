import streamlit as st
import requests
import pickle

BASE_URL = "http://localhost:8000"

def movie_search():
    st.title("Search for Movies")
    movie_name = st.selectbox("Enter movie name to search")

    if st.button("Search"):
        response = requests.get(
            f"{BASE_URL}/recommend_by_title", params={"title": movie_name})
        if response.status_code == 200:
            movies = response.json().get("recommendations", [])
            st.write("Movies Found:")
            for movie in movies:
                st.write(f"- {movie}")
        else:
            st.error("Movie not found.")
