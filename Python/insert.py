

# import streamlit as st

# import pymysql as sql

# @st.dialog("Conformation")
# def con():
#     st.title("are u sure to insert data ?")
#     if st.button("yesss"):
#         st.success("data inserted successfully")
        




# st.title("employee management system")


# with st.form("emp_form", clear_on_submit=True):
#  eid=st.text_input("enter employee id")
#  en=st.text_input("enter employee name")
#  eg=st.selectbox("gender",["male","female","others"])
#  dob=st.text_input("enter employee date of birth")
#  ec=st.selectbox("enter employee city",["delhi","mumbai","kolkata","chennai"])
#  es=st.text_input("enter employee salary")
#  em=st.text_input("enter employee no.")

# db = None
# if st.button("submit"):
#  try:
#     db = sql.connect(
#     host ='localhost',
#     port=3306,
#     user='root',
#     password='1234',
#     database='testyo' ,
#     cursorclass=sql.cursors.DictCursor
#     )
#     smt = db.cursor()
#     s=f"insert into new_table values ( {eid} , '{en}', '{dob}' , '{eg}' , '{ec}' , '{es}' , '{em}' ) "
#     smt.execute(s)
#     db.commit()
#     submitted = st.form_submit_button("Submit")

#     if submitted:
#         # Insert into database
#         st.success("Data inserted successfully")
    
#  except Exception as e:
#     st.error(e)
#  finally:
#     if db:
#         db.close()
     















import streamlit as st
import pymysql as sql

# Initialize session state
if "eid" not in st.session_state:
    st.session_state.eid = ""
    st.session_state.en = ""
    st.session_state.dob = ""
    st.session_state.es = ""
    st.session_state.em = ""

st.title("Employee Management System")

eid = st.text_input("Enter Employee ID", key="eid")
en = st.text_input("Enter Employee Name", key="en")
eg = st.selectbox("Gender", ["male", "female", "others"])
dob = st.text_input("Enter Employee Date of Birth", key="dob")
ec = st.selectbox("Enter Employee City", ["delhi", "mumbai", "kolkata", "chennai"])
es = st.text_input("Enter Employee Salary", key="es")
em = st.text_input("Enter Employee No.", key="em")

db = None

if st.button("Submit"):
    try:
        db = sql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='1234',
            database='testyo',
            cursorclass=sql.cursors.DictCursor
        )

        smt = db.cursor()

        s = f"""
        insert into new_table
        values ({eid}, '{en}', '{dob}', '{eg}', '{ec}', '{es}', '{em}')
        """

        smt.execute(s)
        db.commit()

        st.success("Data inserted successfully")
        with st.form("emp_form", clear_on_submit=True):
        # Clear input boxes
         st.session_state.eid = ""
         st.session_state.en = ""
         st.session_state.dob = ""
         st.session_state.es = ""
         st.session_state.em = ""

        st.rerun()

    except Exception as e:
        st.error(e)

    finally:
        if db:
            db.close()