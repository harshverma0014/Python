import streamlit as st
import pymysql as sql

st.title("Employee Management System")

st.image("ems2.png", width=400)


# connection to database  ---------------------------------------------------------------------------------------------

try:
    db=sql.connect(
        host="localhost",
        port=3306,
        user='root',
        password='1234',
        database='testyo' ,
        cursorclass=sql.cursors.DictCursor
    )
    smt=db.cursor()
    st.success("connected to database successfully")
except Exception as e:
    st.error(e)



work=st.sidebar.radio("select your work",["1] Insert","2] Display","3] Update","4] Delete"])

# insert--------------------------------------------------------------------------------------------------------------------------
if work=="1] Insert":
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
elif work=="2] Display":
    st.subheader("Display Employee Records")
    try:
            smt.execute("select * from new_table")
            records=smt.fetchall()
            st.dataframe(records)
    except Exception as e:
            st.error(e)


# update --------------------------------------------------------------------------------------------------------------------------
elif work=="3] Update":
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

 

    except Exception as e:
        st.error(e)
        
        

# delete --------------------------------------------------------------------------------------------------------------------------
elif work=="4] Delete":
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
        st.error("invalid input")

