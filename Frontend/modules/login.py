import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

def login():
    st.title("Login Page")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not email or not password:
            st.error("Please enter both email and password")
            return

        params = {
            "email": email,
            "password": password
        }

        try:
            response = requests.post(
                f"{BASE_URL}/api/login/user/login",
                params=params
            )

            if response.status_code == 200:
                user_data = response.json()
                st.session_state["user"] = user_data
                st.success("Login successful!")
                st.rerun()
            else:
                error_data = response.json()
                if isinstance(error_data.get("detail"), list):
                    error_msg = error_data["detail"][0]["msg"]
                else:
                    error_msg = error_data.get("detail", "Invalid credentials")
                st.error(f"Login failed: {error_msg}")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {str(e)}")