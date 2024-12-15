import streamlit as st

# Kiểm tra trạng thái đăng nhập
if "user" not in st.session_state:
    st.session_state["user"] = None

# Khi chưa đăng nhập, chỉ hiển thị trang Login
if st.session_state["user"] is None:
    st.sidebar.empty()  # Ẩn sidebar
    from modules.login import login
    login()

# Khi đã đăng nhập, hiển thị menu điều hướng
else:
    st.sidebar.title("Menu")
    menu = st.sidebar.radio(
        "Navigate", ["Dashboard", "Search Movies", "Find Similar Movies", "Logout"]
    )

    if menu == "Dashboard":
        from modules.dashboard import dashboard
        dashboard()
    elif menu == "Search Movies":
        from modules.movie_search import movie_search
        movie_search()
    elif menu == "Find Similar Movies":
        from modules.similar_movie import similar_movies
        similar_movies()
    elif menu == "Logout":
        st.session_state["user"] = None
        st.rerun()
