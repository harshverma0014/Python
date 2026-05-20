
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







import pymysql as mysql
try:
    db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='my_industry')
    smt=db.cursor()
    s="CREATE TABLE products(ProductID INT PRIMARY KEY,ProductName VARCHAR(100),SupplierID INT,CategoryID INT,QuantityPerUnit INT,UnitPrice DECIMAL(10,2),UnitsInStock INT,UnitsOnOrder INT,ReorderLevel INT,Discontinued VARCHAR(20),ManufactureDate DATE)";
    smt.execute(s)
    print("table created successfully...")
except Exception as e:
   print("error:",e)








import pymysql as mysql
try:
    db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='my_industry')
    smt=db.cursor()
    pid=input("enter productid:")
    pn=input("enter productname:")
    sid=input("enter supplierid:")
    cid=input("enter categoryid:")
    qperunit=input("enter quantityperunit:")
    uprice=input("enter umitprice:")
    us=input("enter unitsinstock:")
    uo=input("enter unitsonorder:")
    rl=input("enter reorderlevel:")
    d=input("enter discountinued:")
    mf=input("Enter Manufacture date:")
    q=f"(insert into products values({pid},'{pn}',{sid},{cid},{qperunit},{uprice},{us},{uo},{rl},'{d}','{mf}')"
    print(q)
    smt.execute(q)
    print("products submitted successfully...")
    db.commit()
    db.close()
except Exception as e:
    print("error:",e)





