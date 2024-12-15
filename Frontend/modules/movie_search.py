import streamlit as st
import requests
import pickle

# Cấu hình API URL
BASE_URL = "http://localhost:8000"

# Tải dữ liệu phim từ file pickle
movies = pickle.load(open("../Backend/data/movies.pkl", "rb"))

def movie_search():
    # Kiểm tra trạng thái đăng nhập
    if "user" not in st.session_state or "user_id" not in st.session_state["user"]:
        st.error("User not logged in. Please log in first.")
        return
    
    # Lấy user_id từ session_state
    user_id = st.session_state["user"]["user_id"]

    # Giao diện tìm kiếm phim
    st.title("Search for Movies")
    movie_name = st.selectbox("Select a movie", movies["original_title"].values)

    # Hiển thị thông tin phim và thêm nút Watch
    if movie_name:
        st.subheader(f"Selected Movie: {movie_name}")

        # Nút Watch
        if st.button("Watch", key="watch_button"):  # Sử dụng key để đảm bảo không xung đột
            response = requests.post(
                f"{BASE_URL}/api/history/history/{user_id}/add",  # user_id trong URL
                params={"movie_title": movie_name}       # Tên phim trong query params
            )

            # Kiểm tra phản hồi từ API
            if response.status_code == 200:
                st.success(f"'{movie_name}' has been added to your watch history!")
            else:
                st.error("Failed to add movie to your watch history.")

