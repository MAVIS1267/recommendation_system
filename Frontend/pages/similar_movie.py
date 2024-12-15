import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

def similar_movies():
    st.title("Find Similar Movies")
    movie_name = st.text_input("Enter movie name to find similar movies")

    if st.button("Find Similar"):
        response = requests.get(f"{BASE_URL}/api/recommendation/recommendations", params={"title": movie_name})
        if response.status_code == 200:
            similar_movies = response.json().get("recommendations", [])
            st.write("Similar Movies:")
            for movie in similar_movies:
                st.write(f"- {movie}")
        else:
            st.error("Movie not found.")
