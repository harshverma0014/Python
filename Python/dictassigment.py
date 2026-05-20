# 1. Write a Python script to sort (ascending and descending) a dictionary by value.   

# d={'a':2 ,'b':4, 'c':1,'d':3}


# a=list(d.items())

# b=len(a)


# for i in range(b):
#     for j in range(0,b-i-1):
#         if a[j][1]>a[j+1][1]:

#             a[j], a[j+1]=a[j+1], a[j]
# print(dict(a))


# 2. Write a Python script to add a key to a dictionary.   
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# def create_(n):
#     d={}
#     for i in range(n):
#         d[i]=(i+1)*10
#     return d
# a=create_(5)
# print(a)


# 3. Write a Python script to concatenate following dictionaries to create a new one.   
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# 4. Write a Python script to check if a given key already exists in a dictionary.   

# dic1={1:10, 2:20}
# r=dic1.get(1,'does not exist')
# print(r)


# 5. Write a Python program to iterate over dictionaries using for loops.   

# a={1:'a',2:'b',3:'c'}
# for i in a.items():
#     print(i)



# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).   
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    

# n=5
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)



# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.   
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
    

# n=15
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)



#
# 8. Write a Python script to merge two Python dictionaries.   
    

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}


# dic1.update(dic2)

# print(dic1)

# 9. Write a Python program to iterate over dictionaries using for loops.   
    

# a={1:'a',2:'b',3:'c'}
# for i in a.items():
#     print(i)



# 10. Write a Python program to sum all the items in a dictionary.   
    
# d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# for i in d.items():
    
#     print(sum(i))


# 11. Write a Python program to multiply all the items in a dictionary.   
    
# d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# for i,j in d.items():
    
#     print(i*j)


# 12. Write a Python program to remove a key from a dictionary.   
    
# d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# d.pop(1)
# print(d)

# 13. Write a Python program to map two lists into a dictionary.   
    

# a=[1,2,3,4,5]
# b=[2,3,4,5,6]
# r={}

# for i in range(len(a)):
#     r[a[i]]=b[i]
# print(r)


# 14. Write a Python program to sort a dictionary by key.

# a={3: 4, 5: 6, 2: 3,1: 2 , 4: 5}.items()
# a=sorted(a)
# print(dict(a))



# 15. Write a Python program to get the maximum and minimum value in a dictionary.   
    
# a={3: 4, 5: 6, 2: 3,1: 2 , 4: 5}
# ma=max(a.values())
# mi=min(a.values())

# print(ma,mi)

# 16. Write a Python program to get a dictionary from an object's fields.   
    

# name = "Harsh"
# age = 20

# d = {
#     "name": name,
#     "age": age
# }

# print(d)



# 17. Write a Python program to remove duplicates from Dictionary.   
    

# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

# res = {}

# for k, v in d.items():
#     if v not in res.values():
#         res[k] = v

# print(res)


# 18. Write a Python program to check a dictionary is empty or not.   
    
# a={1:2,2:3}
# if len(a)>0:
#     print('not empty')

# else:
#     print('empty')

# 19. Write a Python program to combine two dictionary adding values for common keys.   
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# c={}
# c=d2.copy()
# for i in d1:
#     if i in c:
#         c[i]=c[i]+d1[i]
#     else:
#         c[i]=d1[i]

# print(c)
    
        
# 20. Write a Python program to print all unique values in a dictionary.   
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
    


# a= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=set()
# for i in a:
#     for c in i.values():
#         b.add(c)
    
# print(b)



# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.   
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd


# a={'1':['a','b'], '2':['c','d']}
# b=a.values()
# c=a.keys()
# print(b)
# for i in c:
#     for j in  
#           c[]
    

# a = {'1': ['a','b'], '2': ['c','d']}

# values = list(a.values())
# print(values)
# for i in values[0]:
#     for j in values[1]:
#         print(i + j)
    


# 22. Write a Python program to find the highest 3 values in a dictionary.   
    
# a={"a":1,"c":3,"b":2,"d":4}
# b=sorted(a.values(),reverse=True)[:3]
# print(b)



# 23. Write a Python program to combine values in python list of dictionaries.   
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
    

# a= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# r={}
# for i in a:
#     k=i['item']
#     v=i['amount']

#     if k in r:
#         r[k]+=v
#     else:
#         r[k]=v
# print(r)



# 24. Write a Python program to create a dictionary from a string.   
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
    
# a='w3resourece'
# print(a)
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# 25. Write a Python program to print a dictionary in table format.   
    

# data = {
#     1: {'Name': 'John', 'Age': 20, 'Marks': 85},
#     2: {'Name': 'Alice', 'Age': 22, 'Marks': 90},
#     3: {'Name': 'Bob', 'Age': 21, 'Marks': 78}
# }

# print('id','\t','name','\t','age','\t','marks')

# for i,j in data.items():
#     print(i,'\t' , j['Name'],'\t',j['Age'],'\t',j['Marks'])


#     26. Write a Python program to count the values associated with key in a dictionary.   
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True

# a= [{'id': 1, 'success': True, 'name': 'Lary'},
#      {'id': 2, 'success': False, 'name': 'Rabi'}, 
#      {'id': 3, 'success': True, 'name': 'Alex'}]
# c=0
# for i in a:
#     if i['success']==True:
#         c+=1
# print(c)



# 27. Write a Python program to convert a list into a nested dictionary of keys.   
    

# lst = ['a', 'b', 'c']

# d = {}

# for i in reversed(lst):
#     d = {i: d}

# print(d)


# 28. Write a Python program to sort a list alphabetically in a dictionary.   
    

# d = {'a': ['banana', 'apple', 'kela']}
# d['a']=sorted(d['a'])
# print(d)


# 29. Write a Python program to remove spaces from dictionary key
#s.   
    

# d = {'a b': 1, 'c d': 2, 'e f': 3}
# a={}
# for i,j in d.items():
#     nk=i.replace(" ",'')
#     a[nk]=j
# print(a)


# 30. Write a Python program to get the top three items in a shop.   
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3



















# 31. Write a Python program to get the key, value and item in a dictionary.   
    
# d = {'a': 1, 'b': 2, 'c': 3}

# for k, v in d.items():
#     print("Key:", k)
#     print("Value:", v)
#     print("Item:", (k, v))
#     print()


# 32. Write a Python program to print a dictionary line by line. 
  
    
# d = {'a': 1, 'b': 2, 'c': 3}
# for i in d.items():
#     print(i)


# 33. Write a Python program to check multiple keys exists in a dictionary.   
    

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# c=["a","d"]
# for i in c:
#     if i in d:
#         print(i , 'exist')
#     else:
#         print(i,'does not exist')



# 34. Write a Python program to count number of items in a dictionary value that is a list.   
    


# d = {
#     'a': [1, 2, 3],
#     'b': [4, 5],
#     'c': [6, 7, 8, 9]
# }
# count=0

# for i in d.values():
#     count+= len(i)
# print(count)


# 35. Write a Python program to sort Counter by value.   
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
    














# 36. Write a Python program to create a dictionary from two lists without losing duplicate values.   
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})
    

# a = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# b = [1, 2, 2, 3]

# x = dict(zip(a, b))




# print(x)




# 37. Write a Python program to replace dictionary values with their sum.   
    
# d = {
#     'a': [1, 2, 3],
#     'b': [4, 5],
#     'c': [6, 7, 8]
# }

# for i in d:
#     d[i]=sum(d[i])
# print(d)



# 38. Write a Python program to match key values in two dictionaries.   
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
    


# x= {'key1': 1, 'key2': 3, 'key3': 2}
# y={'key1': 1, 'key2': 2}

# for i in x:
#     if i in y and x[i]==y[i]:
#         print(i ,'present in both x and y' )
  



# 39. Write a Python program to store a given dictionary in a json file.   
# Original dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# <class 'dict'>
# Json file to dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'},
#  {'firstName': 'Mervin', 'lastName': 'Friedland'},
#  {'firstName': 'Aron ', 'lastName': 'Wilkins'}],
# 
#  'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'},
#  {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
    


# a= {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'},
#                   {'firstName': 'Mervin', 'lastName': 'Friedland'},
#                     {'firstName': 'Aron ', 'lastName': 'Wilkins'}],
                    
#                       'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'},
#                                     {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

















# 40. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.   
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]


# d = {
#     'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#     'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
#     'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]
# }

# for i in d:
   
#     print(d[i][4])
# for i in d:
#     print(i,'has value',d[i])
















































































































































