import streamlit as st
st.title("Login Page")

if st.button("run"):
    st.session_state.logged_in = True
    st.rerun()