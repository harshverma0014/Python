
# import pymysql as sql
# db = sql.connect(
#     host ='localhost',
#     port=3306,
#     user='root',
#     password='1234',
#     database='pythontest' 
#     )
# try:
    
#     smt = db.cursor()
#     ie=input("enter the id of the employee: ")
#     ne=input("enter the name of the employee: ")
#     de=input("enter the dob of the employee: ")
#     ge=input("enter the gender of the employee: ")
#     sa=input("enter the salary of the employee: ")
#     ci=input("enter the city of the employee: ")
#     mo=input("enter the mobile number of the employee: ")

#     s=f"insert into employes values ( {ie} , '{ne}', '{de}' , '{ge}' , {sa} , '{ci}' , '{mo}' ) "
#     smt.execute(s)
#     print(s)
#     db.commit()
   
# #     db.close()
# # except Exception as e:
# #     print(e)







# import pymysql as mysql
# try:
#     db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='my_industry')
#     smt=db.cursor()
#     s="CREATE TABLE products(ProductID INT PRIMARY KEY,ProductName VARCHAR(100),SupplierID INT,CategoryID INT,QuantityPerUnit INT,UnitPrice DECIMAL(10,2),UnitsInStock INT,UnitsOnOrder INT,ReorderLevel INT,Discontinued VARCHAR(20),ManufactureDate DATE)";
#     smt.execute(s)
#     print("table created successfully...")
# except Exception as e:
#    print("error:",e)








# import pymysql as mysql
# try:
#     db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='my_industry')
#     smt=db.cursor()
#     pid=input("enter productid:")
#     pn=input("enter productname:")
#     sid=input("enter supplierid:")
#     cid=input("enter categoryid:")
#     qperunit=input("enter quantityperunit:")
#     uprice=input("enter umitprice:")
#     us=input("enter unitsinstock:")
#     uo=input("enter unitsonorder:")
#     rl=input("enter reorderlevel:")
#     d=input("enter discountinued:")
#     mf=input("Enter Manufacture date:")
#     q=f"(insert into products values({pid},'{pn}',{sid},{cid},{qperunit},{uprice},{us},{uo},{rl},'{d}','{mf}')"
#     print(q)
#     smt.execute(q)
#     print("products submitted successfully...")
#     db.commit()
#     db.close()
# except Exception as e:
#     print("error:",e)




# ----------------------------------------------------------


# l=39,40 



# -------------------------------------------------------------




# EDIT


# try:
#     import pymysql as mysql
#     db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='sample',cursorclass=mysql.cursors.DictCursor)

#     smt=db.cursor()
#     id=input("Enter Employee ID u want to edit :  ")
#     smt.execute(f'Select * from employee where employeeid={id}')
    
#     record=smt.fetchone()
#     if (record):
#         print("Employee id :",record['EmployeeID'])
#         print("1] Employee Name :",record['EmployeeName'])
#         print("2] Employee city :",record['City'])
#         print("3] Employee salary :",record['Salary'])
#         print("4] Exit")
#         ch=int(input('Enter Choice[1-4] :'))
#         pat=''
#         if (ch==1):
#             en=input("Enter New Employee Name : ")
#             pat=f'employeename="{en}"'
#         elif (ch==2):
#             ec=input("Enter New Employee City : ")
#             pat=f'city="{ec}"'
#         elif (ch==3):
#             es=input("Enter New Employee Salary : ")
#             pat=f'salary="{es}"'
#         elif (ch==4):
#             print("Exit")
#         else:
#             print("Wrong option..")
#         if(pat!=''):
#          q=f"update employee set {pat} where employeeid={id}"
#          smt.execute(q)
#          db.commit()
#          print('Employee update successfully....')
#     db.close()
 

# except Exception as e:
#     print('Error : ',e)








# delete

# try:
#     import pymysql as mysql
#     db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='sample',cursorclass=mysql.cursors.DictCursor)

#     smt=db.cursor()
#     id=input("Enter Employee ID u want to delete :  ")
#     smt.execute(f'Select * from employee where employeeid={id}')
    
#     record=smt.fetchone()
#     if (record):
#         print("Employee id :",record['EmployeeID'])
#         print("Employee Name :",record['EmployeeName'])
#         print("Employee city :",record['City'])
#         print("Employee salary :",record['Salary'])
        
#         ch=input('Do you want to delete above record y/n:')
#         if(ch.lower()=='y'):
#          q=f"delete from employee where employeeid={id}"
#          smt.execute(q)
#          db.commit()
#          print('Employee deleted successfully....')
#     else:
#         print(f'Employee not exist {id}')
#     db.close()
 

# except Exception as e:
#     print('Error : ',e)





# join


# try:
#     import pymysql as mysql
#     db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='power_bi',cursorclass=mysql.cursors.DictCursor)

#     smt=db.cursor()
#     smt.execute('Select categories.categoryname,products.productname,products.unitprice from products,categories where categories.categoryid=products.categoryid')
    
#     records=smt.fetchall()
    
#     for record in records:
#         print(record['categoryname'],record['productname'],record['unitprice'])
#     db.close()

# except Exception as e:
#     print('Error : ',e)






# ----------------------------------------------------------


# l=41 april 21



# -------------------------------------------------------------

# exception handling
























