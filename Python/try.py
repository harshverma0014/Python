# Columns
# import streamlit as st
# col1, col2, col3, col4 = st.columns(4)
# with col1:
# st.image("https://picsum.photos/200", width=200)
# with col2:
# st.image("https://picsum.photos/201", width=200)
# with col3:
# st.image("https://picsum.photos/200", width=200)
# with col4:
# st.image("https://picsum.photos/201", width=200)











# import streamlit as st
# @st.dialog("Login Form")
# def login_dialog():
#  st.text_input("Username")
#  st.text_input("Password", type="password")
#  if st.button("Login"):
#    st.success("Login Successful")
# if st.button("Open Dialog"):
#  login_dialog()




# import streamlit as st
# @st.dialog("Delete Confirmation")
# def confirm_delete():
#  st.warning("Are you sure you want to delete?")
#  coll, col2 = st.columns (2)
#  with coll:
#   if st.button("Yes"):
#    st.success("Deleted")
#  with col2:
#   if st.button("No"):
#    st.info("Cancelled")
# if st.button("Delete File"):
#   confirm_delete()