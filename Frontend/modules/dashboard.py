import streamlit as st
import requests

BASE_URL = "http://localhost:8000"


def dashboard():
    st.title(f"Welcome, {st.session_state['user']['username']}")

    # Hiển thị recommend dựa trên lịch sử
    st.header("Recommended Movies")
    user_id = st.session_state["user"]["user_id"]

    # Gửi request lấy danh sách gợi ý
    try:
        params = {"user_id": user_id}
        response = requests.get(
            f"{BASE_URL}/api/recommendation/recommendations/user/{user_id}", params=params)

        # Kiểm tra status code
        if response.status_code == 200:
            movies = response.json().get("recommended_movies", [])
            if not movies:
                st.info("No recommendations found for you.")
            else:
                for movie in movies:
                    col1, col2 = st.columns([4, 1])
                    col1.write(movie)
                    if col2.button("Watch", key=movie):
                        # Gửi request cập nhật lịch sử xem
                        watch_response = requests.post(
                            f"{BASE_URL}/api/history/history/{user_id}/add",
                            params={"movie_title": movie}
                        )
                        if watch_response.status_code == 200:
                            st.success(
                                f"'{movie}' added to your watch history!")
                            st.rerun()
                        else:
                            st.error("Failed to update watch history.")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching recommendations: {e}")
