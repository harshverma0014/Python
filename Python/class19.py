# n=int(input("enter n : "))

# l=[]
# for i in range(n):
#     a=input("enter city name ")
#     l.append(a)


# print(l)

#-----------------------------------------------------------------------------------------------------------------------


# n=int(input("enter n: "))
# l=[]
# for i in range(n):
#     roll=int(input("enter roll no. : "))
#     name=input("enter name : ")
#     p=int(input("enter physics marks: "))
#     c=int(input("enter chemistry marks: "))
#     m=int(input("enter maths marks: "))
#     l.append([roll,name,p,c,m])

# print(l)


#------------------------------------------------------------------------------------------------------------------------------------


l=[['100','peter',50,50,50],['200','harry',60,60,60]]
for s in l:
    total=s[2]+s[3]+s[4]
    per=total/3
    s.append(total)
    s.append(per)
    

print(l)












