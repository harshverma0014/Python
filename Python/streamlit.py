import streamlit as st



# st.title("TITLE")
# st.header("header")
# st.subheader("subheader")
# st.text("text")
# st.write("write")
# st.error("error")
# st.warning("warning")
# st.info("info")
# st.success("success")





# st.markdown("""
# # big
# ## small
# ### litle
# """)

# #  big
# ## small
# ### small



# st.markdown("<h1 style='color: green;'>Hello, World!</h1>", unsafe_allow_html=True)


# student=[{"roll":100,"name":"peter singh"}]
# st.dataframe(student)
# st.table(student)



# id=st.text_input("enter id")


# label="" ,placeholder="enter id"

# value="", 

# max_chars= none ,

# key=none,

# type="default/passwaord"

# help = nane,

# autocomplete = none/ email / name / password ,

# on_change = none ,

# args = none,

# kwatgs= none,

# disabled = false,
# label_visibility="visible/hidden"












# a=st.number_inpu("enterr no.)

# min_value=none,
# max_value=none,
# value="min",
# step=none
# format=none,
# key=none,
# help=none,
# on_chamge=none,
# args=none,
# kwargs=none,
# placeholder=none,
# disabled=false,
# label_visibility="visible"


# java=st.checkbox("java")


# g=t.radio("gender"=,["male","female","others"])

# at.selectbox()








# --------------------------------------------------------


# l=43 april 26



# -------------------------------------------------------





import streamlit as st

import pymysql as sql



st.title("employee management system")



eid=st.text_input("enter employee id")
en=st.text_input("enter employee name")
eg=st.selectbox("gender",["male","female","others"])
dob=st.text_input("enter employee date of birth")
ec=st.selectbox("enter employee city",["delhi","mumbai","kolkata","chennai"])
es=st.text_input("enter employee salary")
em=st.text_input("enter employee no.")


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
    # print(s)
    db.commit()
    st.success("data inserted successfully")
 except Exception as e:
    st.error(e)
 finally:

    db.close()
    