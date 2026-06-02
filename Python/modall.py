import pymysql as sql
import streamlit as st

@st.dialog("connection")
def con():
 n=st.text_input("enter name")
 p=st.text_input("enter pass" ,type="password")
 if st.button("connect"):
  try:
    db=sql.connect(
        host="localhost",
        port=3306,
        user=n,
        password=p,
        database='testyo' ,
        cursorclass=sql.cursors.DictCursor
    )  
    # smt=db.cursor
    st.session_state.connect=True
    st.session_state.data=db
    st.success("connected to database successfully")
    
    st.rerun()
    
  except Exception as e:
    st.error(e)

try:

 if "connect" not in st.session_state:
    st.session_state.connect=False

 if not st.session_state.connect:
    con()

 if st.session_state.connect:
    db=st.session_state.data
    smt=db.cursor()
    work=st.sidebar.radio("select your work",["0]Home","1] Insert New Employee","2] Display all Employees","3] Update Employee","4] Find Employee","5] Delete Employee"])



# home ------------------------------------------------------------------------------------------------------------------------
    if work=="0]Home":
        st.title("Employee Management System")
        st.image("ems2.png", width=100)
        st.write("Welcome to Employee Management System. Please select an option from the sidebar to manage employee records.")
        
        st.warning("Please connect to database if any error occurs.")




# insert--------------------------------------------------------------------------------------------------------------------------
    
    if work=="1] Insert New Employee":
     st.subheader("Insert Employee Record")
     try:
        eid=st.text_input("enter employee id")
        en=st.text_input("enter employee name")
        eg=st.selectbox("gender",["male","female","others"])
        dob=st.date_input("enter employee date of birth")
        ec=st.selectbox("enter employee city",["delhi","mumbai","kolkata","chennai"])
        es=st.text_input("enter employee salary")
        em=st.text_input("enter employee no.")

        
        if st.button("Submit"):
            try:
                
                s=f"insert into new_table values ( {eid} , '{en}', '{dob}' , '{eg}' , '{ec}' , '{es}' , '{em}' ) "
                smt.execute(s)
    
                db.commit()
                st.success("data inserted successfully")
            except Exception as e:
                st.error(e)
     except Exception as e:
                st.error(e)
    
    

# display --------------------------------------------------------------------------------------------------------------------------
    elif work=="2] Display all Employees":
     st.subheader("Display Employee Records")
     try:
            smt.execute("select * from new_table")
            records=smt.fetchall()
            st.dataframe(records)
     except Exception as e:
            st.error(e)


# update --------------------------------------------------------------------------------------------------------------------------
    elif work=="3] Update Employee":
     st.subheader("Update Employee Record")
     try:
        id=st.text_input("Enter Employee id : ")
        
        if id!='':
            smt.execute(f'Select * from new_table where id={id}')
    
            record=smt.fetchone()
            if (record):
                em=st.text_input('Employee Name',value=f"{record['name']}")


                dob=st.text_input('Employee Date of Birth',value=f"{record['dob']}")
                eg=st.selectbox('Employee Gender',["male","female","others"],placeholder=f"{record['gender']}")
                ec=st.selectbox('Employee City',options=["delhi","mumbai","kolkata","chennai"],placeholder=f"{record['city']}")
                es=st.text_input('Employee Salary',value=f"{record['salary']}")
                en=st.text_input('Employee Phone Number',value=f"{record['mobileno.']}")

                if st.button("Update"):
                    q=f"update new_table set name='{em}', dob='{dob}', gender='{eg}', city='{ec}', salary='{es}' where id={id}"
                    smt.execute(q) 
                    db.commit()
                    st.success('Employee updated successfully....')
            
                
            else:
                st.error(f'Employee not exist {id}')

 

     except Exception as e:
        st.error(e)


# find --------------------------------------------------------------------------------------------------------------------------
    elif work=="4] find employee":
     st.subheader("Find employee record")
     try:
        id=st.text_input("Enter Employee id : ")
        
        if id!='':
            smt.execute(f'Select * from new_table where id={id}')
    
            record=smt.fetchone()

            if(record):
                st.write("Employee id :",record['id'])
                st.write(" Employee Name :",record['name'])
                st.write(" Employee date of birth :",record['dob'])
                st.write(" Employee gender :",record['gender']) 
                st.write(" Employee city :",record['city'])
                st.write(" Employee salary :",record['salary'])
                st.write(" Employee phone number :",record['mobileno.'])
                st.success("Employee record found successfully....")
            else:
                st.error(f'Employee not exist {id}')
     except Exception as e:
        st.error(e)
    


# delete --------------------------------------------------------------------------------------------------------------------------
    elif work=="5] Delete Employee":
     st.subheader("Delete Employee Record")
     try:
         id=st.text_input("Enter Employee ID u want to delete :  ")
         if id!='':
        
          smt.execute(f'Select * from new_table where id={id}')
    
          record=smt.fetchone()
          if (record):
            st.write("Employee id :",record['id'])

            st.write(" Employee Name :",record['name'])

            st.write(" Employee date of birth :",record['dob'])

            st.write(" Employee gender :",record['gender'])

            st.write(" Employee city :",record['city'])

            st.write(" Employee salary :",record['salary'])

            st.write(" Employee phone number :",record['mobileno.'])
        
            ch=st.radio('Do you want to delete above record y/n:', ['y', 'n'])

            if(ch.lower()=='y'):
             if st.button("Delete"):
                q=f"delete from new_table where id={id}"
                smt.execute(q)
                db.commit()
                st.success('Employee deleted successfully....')
            elif(ch.lower()=='n'):
                st.info('Deletion cancelled.')
          else:
            st.error(f'Employee not exist {id}')
    
 

     except Exception as e:
            st.error(e)

















 else:
    st.warning("please connect to database")
    if st.button("connect to database"):
        st.rerun()

except Exception as e:
    st.error(e)


























# import pymysql as sql
# import streamlit as st

# @st.dialog("connection")
# def con():
#     n = st.text_input("enter name")
#     p = st.text_input("enter pass", type="password")

#     if st.button("connect"):
#         try:
#             db = sql.connect(
#                 host="localhost",
#                 port=3306,
#                 user=n,
#                 password=p,
#                 database="testyo",
#                 cursorclass=sql.cursors.DictCursor
#             )

#             st.session_state.db = db
#             st.session_state.connect = True

#             st.success("connected to database successfully")
#             st.rerun()

#         except Exception as e:
#             st.error(e)

# if "connect" not in st.session_state:
#     st.session_state.connect = False

# if not st.session_state.connect:
#     con()

# if st.session_state.connect:
#     db = st.session_state.db

#     smt = db.cursor()
#     smt.execute("select * from new_table")

#     records = smt.fetchall()

#     st.dataframe(records)
