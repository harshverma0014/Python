

import streamlit as st

import pymysql as sql

@st.dialog("Conformation")
def con():
    st.title("are u sure to insert data ?")
    if st.button("yesss"):
        st.success("data inserted successfully")
        
        
        
        
        # st.rerun()
        




st.title("employee management system")



eid=st.text_input("enter employee id")
en=st.text_input("enter employee name")
eg=st.selectbox("gender",["male","female","others"])
dob=st.text_input("enter employee date of birth")
ec=st.selectbox("enter employee city",["delhi","mumbai","kolkata","chennai"])
es=st.text_input("enter employee salary")
em=st.text_input("enter employee no.")

db = None
if st.button("submit"):
 try:
    db = sql.connect(
    host ='localhost',
    port=3306,
    user='root',
    password='1234',
    database='testyo' ,
    cursorclass=sql.cursors.DictCursor
    )
    smt = db.cursor()
    s=f"insert into new_table values ( {eid} , '{en}', '{dob}' , '{eg}' , '{ec}' , '{es}' , '{em}' ) "
    smt.execute(s)
    db.commit()
    # con()
    
    if st.button("confirm"):
        con()
        st.rerun()
    
 except Exception as e:
    st.error(e)
 finally:
    if db:
        db.close()
     
