# import streamlit as st



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


# # data entery




# import streamlit as st

# import pymysql as sql



# st.title("employee management system")



# eid=st.text_input("enter employee id")
# en=st.text_input("enter employee name")
# eg=st.selectbox("gender",["male","female","others"])
# dob=st.text_input("enter employee date of birth")
# ec=st.selectbox("enter employee city",["delhi","mumbai","kolkata","chennai"])
# es=st.text_input("enter employee salary")
# em=st.text_input("enter employee no.")

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
#     # print(s)
#     db.commit()
#     st.success("data inserted successfully")
#  except Exception as e:
#     st.error(e)
#  finally:
#     if db:
#         db.close()
     



# displayall

# import streamlit as st
# import pymysql as sql
# try:
#     db = sql.connect(
#     host ='localhost',
#     port=3306,
#     user='root',
#     password='1234',
#     database='power_bi' ,
#     cursorclass=sql.cursors.DictCursor
#     )
#     smt=db.cursor()
#     smt.execute("select * from employees")
#     records=smt.fetchall()
#     st.dataframe(records)
# except Exception as e:
#     st.error(e)
# finally:
#     db.close()









# EDIT


# import streamlit as st
# try:
#     import pymysql as mysql
#     db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='sample',cursorclass=mysql.cursors.DictCursor)

#     smt=db.cursor()
#     id=st.text_input("Enter Employee id : ")
#     if id!='':
#         smt.execute(f'Select * from employee where employeeid={id}')
    
#         record=smt.fetchone()
#         if (record):
#          st.write("Employee id :",record['EmployeeID'])
#          st.write("1] Employee Name :",record['EmployeeName'])
#          st.write("2] Employee city :",record['City'])
#          st.write("3] Employee salary :",record['Salary'])
#          st.write("4] Exit")
#          ch=st.number_input('Enter Choice[1-4] :', min_value=1, max_value=4)
#          pat=''
#          if (ch==1):
#             en=st.text_input("Enter New Employee Name : ")
#             pat=f'employeename="{en}"'
#          elif (ch==2):
#             ec=st.text_input("Enter New Employee City : ")
#             pat=f'city="{ec}"'
#          elif (ch==3):
#             es=st.number_input("Enter New Employee Salary : ")
#             pat=f'salary="{es}"'
#          elif (ch==4):
#             pat=''
#          else:
#             st.error("Wrong option..")
#          if(ch==4):
#             st.info("Exit successfully....")
#          elif (st.button("update")):
#           if(pat!=''):
#            q=f"update employee set {pat} where employeeid={id}"
#            smt.execute(q)
#            db.commit()
#            st.success('Employee update successfully....')
#           else:
#             st.success("Exit successfully....")
    
 

# except Exception as e:
#     st.error(e)
# finally:
#     db.close()













# delete

# import streamlit as st
# try:
#     import pymysql as mysql
#     db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='sample',cursorclass=mysql.cursors.DictCursor)

#     smt=db.cursor()
#     id=st.text_input("Enter Employee ID u want to delete :  ")
#     if id!='':
#      smt.execute(f'Select * from employee where employeeid={id}')
    
#      record=smt.fetchone()
#      if (record):
#         st.write("Employee id :",record['EmployeeID'])
#         st.write("Employee Name :",record['EmployeeName'])
#         st.write("Employee city :",record['City'])
#         st.write("Employee salary :",record['Salary'])
        
#         ch=st.text_input('Do you want to delete above record y/n:')
#         if(ch.lower()=='y'):
#          q=f"delete from employee where employeeid={id}"
#          smt.execute(q)
#          db.commit()
#          st.success('Employee deleted successfully....')
#         elif(ch.lower()=='n'):
#             st.info('Deletion cancelled.')
#      else:
#         st.error(f'Employee not exist {id}')
    
 

# except Exception as e:
#     st.error(e)
# finally:
#     db.close()







# -----------------------------------------------------------------------



# l- 30 april 30



# ---------------------------------------------------------------------------



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
















