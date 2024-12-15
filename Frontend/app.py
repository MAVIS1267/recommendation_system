import streamlit as st

# Kiểm tra trạng thái đăng nhập
if "user" not in st.session_state:
    st.session_state["user"] = None

# Menu điều hướng
if st.session_state["user"] is None:
    from pages.login import login
    login()
else:
    st.sidebar.title("Menu")
    menu = st.sidebar.radio(
        "Navigate", ["Dashboard", "Search Movies", "Find Similar Movies", "Logout"])

    if menu == "Dashboard":
        from pages.dashboard import dashboard
        dashboard()
    elif menu == "Search Movies":
        from pages.movie_search import movie_search
        movie_search()
    elif menu == "Find Similar Movies":
        from pages.similar_movie import similar_movies
        similar_movies()
    elif menu == "Logout":
        st.session_state["user"] = None
        st.rerun()
