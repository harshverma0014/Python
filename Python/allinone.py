import streamlit as st
import pymysql as sql



title="Employee Management System"

# connection to database
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



st.write(" 1 => insert")
st.write(" 2 => display")
st.write(" 3 => update")
st.write(" 4 => delete")


work=st.selectbox("select your work",["1","2" ,"3", "4"])


if st.button("submit"):
    if work=="1":
     try:
        eid=st.text_input("enter employee id")
        en=st.text_input("enter employee name")
        eg=st.selectbox("gender",["male","female","others"])
        dob=st.text_input("enter employee date of birth")
        ec=st.selectbox("enter employee city",["delhi","mumbai","kolkata","chennai"])
        es=st.text_input("enter employee salary")
        em=st.text_input("enter employee no.")

        
        if st.button("Submt"):
            try:
                
                s=f"insert into new_table values ( {eid} , '{en}', '{dob}' , '{eg}' , '{ec}' , '{es}' , '{em}' ) "
                smt.execute(s)
    
                db.commit()
                st.success("data inserted successfully")
            except Exception as e:
                st.error(e)
     except Exception as e:
                st.error(e)
        





    elif work=="2":
        try:
            smt.execute("select * from new_table")
            records=smt.fetchall()
            st.dataframe(records)
        except Exception as e:
            st.error(e)



    elif work=="3":
     try:
        id=st.text_input("Enter Employee id : ")
        st.badge("search Employee id")
        if id!='':
            smt.execute(f'Select * from employee where employeeid={id}')
    
            record=smt.fetchone()
            if (record):
                st.write("Employee id :",record['EmployeeID'])
                st.write("1] Employee Name :",record['EmployeeName'])
                st.write("2] Employee city :",record['City'])
                st.write("3] Employee salary :",record['Salary'])
                st.write("4] Exit")
                ch=st.selectbox("select your choice",["1","2","3","4"])
                pat=''
                if (ch==1):
                    en=st.text_input("Enter New Employee Name : ")
                    pat=f'employeename="{en}"'
                elif (ch==2):
                    ec=st.text_input("Enter New Employee City : ")
                    pat=f'city="{ec}"'
                elif (ch==3):
                    es=st.number_input("Enter New Employee Salary : ")
                    pat=f'salary="{es}"'
                elif (ch==4):
                    pat=''
                else:
                    st.error("Wrong option..")
                if(ch==4):
                    st.info("Exit successfully....")
                elif (st.button("update")):
                    if(pat!=''):
                        q=f"update employee set {pat} where employeeid={id}"
                        smt.execute(q)
                        db.commit()
                        st.success('Employee update successfully....')
                else:
                    st.success("Exit successfully....")
    
 

     except Exception as e:
        st.error(e)
        
        


    elif work=="4":
        try:
         id=st.text_input("Enter Employee ID u want to delete :  ")
         if id!='':
          smt.execute(f'Select * from employee where employeeid={id}')
    
          record=smt.fetchone()
          if (record):
            st.write("Employee id :",record['EmployeeID'])
            st.write("Employee Name :",record['EmployeeName'])
            st.write("Employee city :",record['City'])
            st.write("Employee salary :",record['Salary'])
        
            ch=st.text_input('Do you want to delete above record y/n:')
            if(ch.lower()=='y'):
                q=f"delete from employee where employeeid={id}"
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

