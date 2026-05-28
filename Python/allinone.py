import streamlit as st
import pymysql as sql

st.title("Employee Management System")
# st.markdown("""
# <body>
#     <img src="m2.png" width="400" height="200">
# </body>
# """, unsafe_allow_html=True)



st.image("m2.jpeg")
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
        
        if id!='':
            smt.execute(f'Select * from new_table where id={id}')
    
            record=smt.fetchone()
            if (record):
                st.write("Employee id :",record['id'])

                st.write("1] Employee Name :",record['name'])

                st.write("2] Employee date of birth :",record['dob'])

                st.write("3] Employee gender :",record['gender'])

                st.write("4] Employee city :",record['city'])

                st.write("5] Employee salary :",record['salary'])

                st.write("6] Employee phone number :",record['mobileno.'])

                st.write("7] Exit")
                
                ch=st.selectbox("select your choice",["1","2","3","4","5","6","7"])
                pat=''
                if (ch=="1"):
                    en=st.text_input("Enter New Employee Name : ")
                    pat=f'name="{en}"'

                elif (ch=="2"):
                    ec=st.text_input("Enter New dob : ")
                    pat=f'dob="{ec}"'
                elif (ch=="3"):
                    ec=st.selectbox("gender" ,["male","female","others"])
                    pat=f'gender="{ec}"'
    
                elif (ch=="4"):
                    ec=st.text_input("Enter New Employee City : ")
                    pat=f'city="{ec}"'
                elif (ch=="5"):
                    es=st.number_input("Enter New Employee Salary : ")
                    pat=f'salary="{es}"'
                elif (ch=="6"):
                    ec=st.text_input("Enter New dob : ")
                    pat=f'mobileno.="{ec}"'
                elif (ch=="7"):
                    pat=''
                else:
                    st.error("Wrong option..")
                if(ch==7):
                    st.info("Exit successfully....")
                elif (st.button("update")):
                    if(pat!=''):
                        q=f"update new_table set {pat} where id={id}"
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
        
            ch=st.text_input('Do you want to delete above record y/n:')

            if(ch.lower()=='y'):
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

