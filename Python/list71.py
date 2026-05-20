# 1. Write a Python program to sum all the items in a list. 

# a=[5,6,7,8,9]
# b=sum(a)
# print(b)

# 2. Write a Python program to multiplies all the items in a list.  

# a=[1,2,3,4]
# b=1
# for i in a:
#     b=b*i
# print(b)

# 3. Write a Python program to get the largest number from a list. 

# a=[4,9,8,4]
# b=max(a)
# print(b)

# 4. Write a Python program to get the smallest number from a list.  
# a=[4,9,8,4]
# b=min(a)
# print(b)


# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.  
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# a=['abc', 'xyz', 'aba', '1221']
# b=0
# for i in a:
#     if len(i)>=2:
#         if(i[0]==i[-1]):
#             b+=1
# print(b)

  
# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.  
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
  
# a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# b=len(a)


# for i in range(b):
#     for j in range(0,b-i-1):
#         print(b-i-1)
#         if a[j][1]>a[j+1][1]:

#             a[j], a[j+1]=a[j+1], a[j]

# print(a)



# 7. Write a Python program to remove duplicates from a list. 

# a=[2,4,6,789,6,4,3]
# a=set(a)
# print(a)
  

# 8. Write a Python program to check a list is empty or not. 

# a=[]
# b=len(a)
# if b>0:
#     print("list is not empty")
# else:
#     print("list is empty")



# 9. Write a Python program to clone or copy a list.  

# a=[3,4,5,7]
# b=a.copy()
# print(b)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.  

# a=["apple", "banana", "kiwi",  "pear", "mango"]
# n=4
# b=[]
# for i in a:
#     if len(i)>n:
#         b.append(i)
# print(b)


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.  

# a=[3,4,6,8,9,3]
# count=0
# for i in a:
#     b=a.count(i)
#     if b>1:
#         count+=1
    
# if count>0:
#     print("true")
# else:
#     print("false")


# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.  
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# a.pop(5)
# a.pop(3)
# a.pop(0)

# print(a)

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.  


# arr = []
# for i in range(3):
#     l=[]
#     for j in range(4):
#         c=[]
#         for m in range(6):
#             c.append("*")
#         l.append(c)
#     arr.append(l)
# print(arr)






# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.  


# a = [7, 8, 120, 25, 44, 20, 27]

# for x in a[:]:      
#     if x % 2 == 0: 
#         a.remove(x) 

# print(a)


# 15. Write a Python program to shuffle and print a specified list.  

# import random
# a=[3,4,5,6,7,9]
# random.shuffle(a)
# print(a)


  
# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).  
  

# L=[]
# for i in range(1,31):
#     if i < 6 or i > 25 :
#         L.append(i*i)
# print(L)


# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).  


# L=[]
# for i in range(1,31):
#     if i > 5 :
#         L.append(i*i)
# print(L)


# 18. Write a Python program to generate all permutations of a list in Python.  
  


# import itertools
# a=[1,2,3,4,5,6]
# b=itertools.permutations(a)
# for i in b:
#     print(i)

# 19. Write a Python program to get the difference between the two lists.  
  
# a=[0,2,3,4,5]
# b=[0,1,2,3,4]
# ab=[]
# ba=[]
# for i in a:
#     if i not in b:
#         ab.append(i)
# for i in b:
#     if i not in a:
#         ba.append(i)
# print(ab)
# print(ba)

# a=set([0,2,3,4,5])
# b=set([0,1,2,3,4])
# resa=a.difference(b)
# resb=b.difference(a)
# print(resa)
# print(resb)
# 20. Write a Python program access the index of a list.  
# a=[3,4,5,6,7]
# n=4
# print(a.index(n))


# 21. Write a Python program to convert a list of characters into a string.  
  
# a=["a","b","c","d"]
# b = ''.join(a)
# print(type(b))

# 22. Write a Python program to find the index of an item in a specified list.  
  

# a=[3,45,6,8]
# n=int(input("enter no."))
# print(a.index(n))


# 23. Write a Python program to flatten a shallow list.  

# a = [[1, 2], [3, 4], [5, 6]]

# res = []
# for i in a:
#     for j in i:
#         res.append(j)

# print(res)

# 24. Write a Python program to append a list to the second list.  
  
# a=[2,4,6]
# b=[6,7,9]

# c=a+b
# print(c)


# 25. Write a Python program to select an item randomly from a list.  
# import random
# a=[2,4,5,7]
# b=random.choice(a)
# print(b)




# 26. Write a python program to check whether two lists are circularly identical.  
  

# a=[1,2,3,4,5]
# b=[5,4,3,2,1]

# if len(a)==len(b):
#     for i in a:
#         if i not in b:
#             print("false")
#             break
#     else:
#         print("true")




# 27. Write a Python program to find the second smallest number in a list.  
# a=set([3,9,1,7,4,9])
# a.sort()
# print(a[1])

# 28. Write a Python program to find the second largest number in a list.  
# a=set([3,5,7,9])
# a.sort()
# print(a[-2])


# 29. Write a Python program to get unique values from a list.  
# a=[3,5,6,0,6,4,6,]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# 30. Write a Python program to get the frequency of the elements in a list.  

# a=[1,2,2,2,3,3,3,4,5,5,5,6,7,8,8]
# d={}
# for i in a:
#     d[i]=a.count(i)
# print(d)


#  31. Write a Python program to count the number of elements in a list within a specified range.  
  
# l=[10,20,30,40,50,60]

# mv=20
# xv=50
# count=0
# for i in l:
#     if mv<=i and i<=xv:
#         count+=1
# print(count)


# 32. Write a Python program to check whether a list contains a sublist.  
  
# main_list = [1, 2, 3, 4, 5]
# sub_list = [2, 3, 4]

# str_main = str(main_list).strip('[]')
# str_sub = str(sub_list).strip('[]')

# if str_sub in str_main:
#     print("Yes, it contains the sublist!")
# else:
    # print("No, it does not.")



# 33. Write a Python program to generate all sublists of a list.  


# l=[1,2,3]
# sl=[[]]
# for i in range(len(l)+1):
#     for j in range(i+1,len(l)+1):
#         sl.append(l[i:j])
# print(sl)

# 34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.  


# a=[1,2,3,4,5,6,7,8,9]
# b=[]
# for i in a:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             b.append(i)

# print(b)
                









# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.  
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
  

# l=["p","q"]
# n=5
# o=[]
# for i in range(1,n+1):
#     for j in l:
#         o.append(j+str(i))
# print(o)

# 36. Write a Python program to get variable unique identification number or string.  
  












#   37. Write a Python program to find common items from two li/sts.
# a=set([1,2,3,4])
# b=set([3,4,5,6])
# a=a.intersection(b)  
# print(a)


# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.  
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]


# a=[0,1,2,3,4,5]
# for i in range(0,len(a)-1,2):
#     a[i],a[i+1]=a[i+1],a[i]
# print(a)


# 39. Write a Python program to convert a list of multiple integers into a single integer.  
# Sample list: [11, 33, 50]
# Expected Output: 113350
# l=[1,2,3,4,5]
# s=""
# for i in l:
#     s+=str(i)
# s=int(s)
# print(s)


# 40. Write a Python program to split a list based on first character of word.  
  
# a=["apple", "banana", "allu",  "blueberry", "kivi"]

# s={}
# for i in a:
#     f=i[0]
#     if f not in s:
#         s[f]=[]
#     s[f].append(i)
# print(s)



# 41. Write a Python program to create multiple lists.  
  
# a=[1,2,3,4]
# b=['a','b','c','d']
# c=[5,6,7,9]
# print(a)
# print(b)
# print(c)


# 42. Write a Python program to find missing and additional values in two lists.  
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
  
# a=set(['a','b','c','d'])
# b=set(['d','e','f'])
# mis =a-b
# ad=b-a
# print(mis)
# print(ad)



# 43. Write a Python program to split a list into different variables.  


# a=[1,2,3,4,5]

# n , *b = a
# print(n)
# print(b)

# 44. Write a Python program to generate groups of five consecutive numbers in a list.  
  


# a=list(range(1,26))
# for i in range(0,len(a),5):
#     print(a[i:i+5])


# 45. Write a Python program to convert a pair of values into a sorted unique array.  

# a = [(1, 3), (2, 3), (4, 5), (1, 2)]
# s=[]
# for i in a:
#     for j in i:
#         if j not in s:
#             s.append(j)
# s.sort()
# print(s)


# 46. Write a Python program to select the odd items of a list.  
  

# a=[1,2,3,4,5,6,7,8,9]
# for i in a:
#     if i%2!=0:
#         print(i)


# 47. Write a Python program to insert an element before each element of a list.  
  

# a=[1,2,3,4,5]
# re=[]
# for i in a:
#     re.append(0)
#     re.append(i)
# print(re)

# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function.  
# a=[[1,2],[3,4],[4,5],[6,7]]
# for i in a:
#     print(i)


# 49. Write a Python program to convert list to list of dictionaries.  
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
  

# c=["Black", "Red", "Maroon", "Yellow"]
# cc=["#000000", "#FF0000", "#800000", "#FFFF00"]

# r=[]

# for i in range(len(c)):
#     d={'colour name :':c[i],'colour code :':cc[i]}
#     r.append(d)
# print(r)




# 50. Write a Python program to sort a list of nested dictionaries

# a= [
#     {'name': 'John', 'age': 25},
#     {'name': 'Alice', 'age': 20},
#     {'name': 'Bob', 'age': 30}
# ]

# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]['age']>a[j]['age']:
#             a[i], a[j]=a[j],a[i]
# print(a)



# 51. Write a Python program to split a list every Nth element.  
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
  


# a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n=5
# c=0
# l=[]
# for i in a:
#     if c<=n:
#         c+=1
#         l.append(i)
#     else:
#         print(l)
#         c=0
#         l=[]

    
# 52. Write a Python program to compute the similarity between two lists.  
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

# a=set(["red", "orange", "green", "blue", "white"])
# b=set(["black", "yellow", "green", "blue"])

# x=a-b
# z=b-a

# print(x)
# print(z)



# 53. Write a Python program to create a list with infinite elements.  
# a=[]
# while True:
#     a.append(1)

# print(a)


# 54. Write a Python program to concatenate elements of a list.  

# a=[1,2,3,4,5]
# r=''
# for i in a:
#     r+=str(i)
# print(r)


# 55. Write a Python program to remove key values pairs from a list of dictionaries.  
  

# data = [
#     {'name': 'John', 'age': 25},
#     {'name': 'Alice', 'age': 20},
#     {'name': 'Bob', 'age': 30}
# ]


# key ="age" 

# for d in data:
#     d.pop(key)
# print(data)

# 56. Write a Python program to convert a string to a list.  
  
# a='harsh'
# a=list(a)
# print(a)

# 57. Write a Python program to check if all items of a list is equal to a given string.  
  

# a = ["hi", "hi", "hi"]
# s = "hi"
# r=True
# for i in a:
#     if i!=s:
#         r=False
#         break
    

# print(r)


# 58. Write a Python program to replace the last element in a list with another list.  
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
  

# a=[1, 3, 5, 7, 9, 10]
# b=[2, 4, 6, 8]
# a=a[:-1]+b
# print(a)


# 59. Write a Python program to check if the n-th element exists in a given list.  
  

# a=[1,2,3,4,5,6,7,8,9]
# n=7
# if n > len(a):
#     print('out of rangge')

# else:
#     print('in range')



# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.  
  

# a= [(1, 5), (3, 2), (9, 10), (4, 1), (7, 8)]
# b=a[0]
# for  it in a:
#     if it[1]<b[1]:
#         b=it
# print(b)


# 61. Write a Python program to create a list of empty dictionaries.  

# n=5
# e=[]
# for i in range(n):
#     e.append({})
  
# print(e)



# 62. Write a Python program to print a list of space-separated elements.  
  

# a="this is a list".split(' ')
# l=[]
# for i in a:
#     l.append(i)
# print(l)


# 63. Write a Python program to insert a given string at the beginning of all items in a list.  
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
  
# a=[1,2,3,4] 
# b = "emp"
# c=[]
# for i in range(len(a)):
#     c.append(b+str(a[i]))
# print(c)


# 64. Write a Python program to iterate over two lists simultaneously.  
  
# a = [1, 2, 3]
# b = ['a', 'b', 'c']

# for i in range(len(a)):
#     print(a[i], b[i])


# 65. Write a Python program to access dictionary keys element by index.  
  
# d = {'a': 10, 'b': 20, 'c': 30}
# a=d.items()
# s=20
# for k,i in a:
#     if i==s:
#         print('value ',i , "key",k)
    


# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.  
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
  

# a=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# ls=a[0]
# ph=sum(a[0])
# for i in a:
    
#     if sum(i)>ph:
#         ph=sum(i)
#         ls=i
# print(ls)


# 67. Write a Python program to find all the values in a list are greater than a specified number.  
  

# a=[1,2,3,4,5,6,7,8,9]
# b=10
# for i in a:
#     if i<b:
#         x=True
#     else:
#         x=False
#         break
# if x==True:
#     print ("yes")
# else :
#     print("no")

# 68. Write a Python program to extend a list without append.  
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
  

# a=[10, 20, 30]
# b= [40, 50, 60]
# a=a+b
# print(a)


# 69. Write a Python program to remove duplicates from a list of lists.  
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]
  
# a=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# re=[]
# for i in a:
#     if i not in re:
#         re.append(i)
# print(re)


# 70. Write a Python program to get the depth of a dictionary.  
  

# a={'name': 'Harsh', 'age': 20, 'course': 'Python', 'marks': 85}
# b=len(a.keys())
# print(b)


# 71. Write a Python program to check if all dictionaries in a list are empty or not.  
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
  

# d=[{},{},{}]

# for i in d:
#     if len(i)!=0:
#         print("false")
#         break
# else:
#     print('True')






