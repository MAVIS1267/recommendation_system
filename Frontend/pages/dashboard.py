import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

def dashboard():
    st.title(f"Welcome, {st.session_state['user']['username']}")

    # Hiển thị recommend dựa trên lịch sử
    st.header("Recommended Movies")
    user_id = st.session_state["user"]["user_id"]

    response = requests.get(f"{BASE_URL}/api/recommendation/recommendations/user/{user_id}", params={"user_id": user_id})
    if response.status_code == 200:
        movies = response.json().get("recommendations", [])
        for movie in movies:
            col1, col2 = st.columns([4, 1])
            col1.write(movie)
            if col2.button("Watch", key=movie):
                requests.post(f"{BASE_URL}/add_watch_history", json={"user_id": user_id, "movie_title": movie})
                st.success(f"'{movie}' added to your watch history!")
                st.experimental_rerun()
    else:
        st.error("Could not fetch recommendations.")
