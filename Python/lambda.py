# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.  
# Sample Output:
# 25
# 48
  


# a = lambda x: x + 15
# print(a(10))

# b = lambda x, y: x * y
# print(b(6, 8))


# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.  
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

# a=lambda x: x*2
# b=lambda x: x*3
# c=lambda x: x*4
# d=lambda x: x*5

# s=a(15)
# print(f"Double the number of 15 = {s}") 
# s=b(15)
# print(f"Triple the number of 15 = {s}")         
# s=c(15)
# print(f"Quadruple the number of 15 = {s}")
# s=d(15)
# print(f"Quintuple the number 15 = {s}")



  
# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# a=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]


# b = sorted(a, key=lambda x: x[1])

# print(b)



  
# 4. Write a Python program to sort a list of dictionaries using Lambda.  
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, 
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
  
# a= [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#  {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# b = sorted(a, key=lambda x: x['model'],reverse=True)

# print(b)


# 5. Write a Python program to filter a list of integers using Lambda.  
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# en=list(filter(lambda x:x%2==0,a))
# on=list(filter(lambda x:x%2!=0,a))
# print(f"Even numbers from the said list: {en}")
# print(f"Odd numbers from the said list: {on}")



# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.  
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# a=[1,2,3,4,5,6,7,8,9,10]
# sq=list(map(lambda x: x*x,a))
# cu=list(map(lambda x: x*x*x,a))
# print(f"Square every number of the said list: {sq}")
# print(f"Cube every number of the said list: {cu}")


# 7. Write a Python program to find if a given string starts with a given character using Lambda.  
# Sample Output:
# True
# False


# a=lambda x,y: x.startswith(y)
# v=a("hululu","h")
# print(v)   


  
# 8. Write a Python program to extract year, month, date and time using Lambda.  
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# a= "2020-01-15 09:03:32.744178"
# b=a.split(" ")
# c=b[0].split("-")

# year = (lambda x: x[0])(c)
# month = (lambda x: x[1])(c)
# date = (lambda x: x[2])(c)
# time = (lambda x: x)(b[1])
# print(year)
# print(month)
# print(date)
# print(time)



# 9. Write a Python program to check whether a given string is number or not using Lambda.  
# Sample Output:
# True
# True
# False
# True
# False
# True
# Print checking numbers:
# True
# True

# a='1234'
# b=lambda x: x.isdigit()
# v=b(a)
# print(v)


# 10. Write a Python program to create Fibonacci series upto n using Lambda.  
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]

# ye=lambda x, y: x + y
# a=[0,1]
# n=int(input("enter the number of terms: "))
# for i in range(2,n):
#     a.append(ye(a[i - 2], a[i - 1]))
# print(a)





  
# 11. Write a Python program to find intersection of two given arrays using Lambda.  
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]
  
# a=[1, 2, 3, 5, 7, 8, 9, 10]
# b=[1, 2, 4, 8, 9]
# c=list(filter(lambda x:x in b,a))
# print(f"Intersection of the said arrays: {c}")


# 12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.  
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]

# a=[-1, 2, -3, 5, 7, 8, 9, -10]
# b=sorted(filter(lambda x:x>=0,a))
# c=sorted(filter(lambda x:x<0,a))
# print(b+c)


# 13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.  
# Original arrays:


# a= [1, 2, 3, 5, 7, 8, 9, 10]
# e=0
# o=0
# b=list(filter(lambda x:x%2==0,a))
# c=list(filter(lambda x:x%2!=0,a))

# print(f"Even numbers : {len(b)}")
# print(f"Odd numbers : {len(c)}")



# 14. Write a Python program to find the values of length six in a given list using Lambda.  
# Sample Output:
# Monday
# Friday
# Sunday

# a=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# b=list(filter(lambda x:len(x)==6,a))

# print(b)


# 15. Write a Python program to add two given lists using map and lambda.  
# Original list:

# Result: after adding two list
# [5, 7, 9]
  
# a= [1, 2, 3]
# b=[4, 5, 6]

# b=list(map(lambda x,y: x+y ,a,b))
# print(b)




# 16. Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda. Input number of students, names and grades of each student.  
# Input number of students: 5
# Name: S ROY
# Grade: 1
# Name: B BOSE
# Grade: 3
# Name: N KAR
# Grade: 2
# Name: C DUTTA
# Grade: 1
# Name: G GHOSH
# Grade: 1
# Names and Grades of all students:
# [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# Second lowest grade: 2.0
# Names:
# N KAR
  
# s=[]
# n=int(input("Input number of students: "))
# for i in range(n):
#     n=input("Name: ")
#     g=int(input("Grade: "))
#     s.append([n,g])

# print(f"Names and Grades of all students  : \n {s} ")
# b=sorted (s,key=lambda x: x[1])
# print(f"Second lowest grade: {b[1][1]}")
# print(f"names : {b[1][0]}")


# 17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.  
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]


# a=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# b=list(filter(lambda x: x%19==0 or x%13==0,a))
# print(b)


# 18. Write a Python program to find palindromes in a given list of strings using Lambda.  
# Orginal list of strings:
# ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']
  
# a=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

# b=list(filter(lambda x:x[:]==x[::-1] ,a))
# print(b)



# 19. Write a Python program to find all anagrams of a string in a given list of strings using lambda.  
# Orginal list of strings:
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['bcda', 'cbda', 'adcb']
  

# a= ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# b='abcd'
# c=list(filter(lambda x:sorted(x) == sorted(b),a))
# print(c)


# 20. Write a Python program to find the numbers of a given string and store them in a list, display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.  
# Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
# Numbers in sorted form:
# 20 23 56
  
# a="sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
# b=a.split()
# c=list(filter(lambda x:x.isdigit(),b ))
# d=sorted(list(filter(lambda x:int(x)>len(c),c)))
# print(d)


# 21. Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.  
# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22

# a=[2,4,6,9,11]
# b=int(input("enter no. : "))
# c=list(map(lambda x:x*b,a))
# print(c)


# 22. Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an lowercase letter. Use lambda function.  
# Result:
# 16


# a="Use lambda Function".split()
# c=0
# b=sum(map(lambda x: len(x) if (x[0].isupper()) else (0) ,a))
# print(b)



# 23. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.  
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: -32
# Sum of the negative numbers: 48

# a=[2, 4, -6, -9, 11, -12, 14, -5, 17]
# b=sum(map(lambda x:x if x>=0 else 0,a))
# c=sum(map(lambda x:x if x<0 else 0,a))
# print(f"Sum of the positive numbers: {b}")
# print(f"Sum of the negitive numbers: {c}")


# 24. Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.  
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]














# 25. Write a Python program to create the next bigger number by rearranging the digits of a given number.  
# Original number: 12
# Next bigger number: 21
# Original number: 10
# Next bigger number: False
# Original number: 201
# Next bigger number: 210
# Original number: 102
# Next bigger number: 120
# Original number: 445
# Next bigger number: 454












