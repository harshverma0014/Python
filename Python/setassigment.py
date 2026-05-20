# 1. Write a Python program to create a set.       

# l=[2,3,4,5,7]
# l=set(l)
# print(l)


# 2. Write a Python program to iteration over sets.       

# l={3,4,5,6,7,8,9}

# for i in l:
#     print(i)


# 3. Write a Python program to add member(s) in a set.       

# l={1,2,3,4}
# l.add(5)
# print(l)



# 4. Write a Python program to remove item(s) from set       

# l={1,2,3,4}
# l.remove(4)
# print(l)


# 5. Write a Python program to remove an item from a set if it is present in the set.       


# l={1,2,3,4,5,6}
# a=9
# if a in l:
#     l.remove(a)
#     print(l)
# else:
#     print("it is not present in the set ")



# 6. Write a Python program to create an intersection of sets.       

# l={1,2,3,4,5,6}
# s={2,3,4,5,8}

# s=l.intersection(s)
# print(s)

# 7. Write a Python program to create a union of sets.       

# l={1,2,3,4,5,6}
# s={2,3,4,5,8}

# s=l.union(s)
# print(s)

# 8. Write a Python program to create set difference.       

# l={1,2,3,4,5,6}
# s={2,3,4,5,8}

# s=l.difference(s)
# print(s)

# 9. Write a Python program to create a symmetric difference.

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# d=a-b
# s=b-a
# c=d.union(s)
# print(c)




# 10. Write a Python program to issubset and issuperset.       


# s1 = {1, 2, 3}
# s2 = {1, 2, 3, 4, 5}

# print("s1 is subset of s2:", s1.issubset(s2))

# print("s2 is superset of s1:", s2.issuperset(s1))



# 11. Write a Python program to create a shallow copy of sets.       

# s={1,2,3,4,5,6}
# b=s.copy()
# print(b)


# 12. Write a Python program to clear a set.       

# a={2,3,4,6,7}
# a=a.clear()
# print(a)



# 13. Write a Python program to use of frozensets.       

# a={2,3,4,5,6}
# a=tuple(a)
# print(type(a))


# 14. Write a Python program to find maximum and the minimum value in a set.       


# a={2,3,4,6,8}
# print('maximum = ',max(a),'\nminimum = ',min(a))


# 15. Write a Python program to find the length of a set.       

# a={1,2,3,4,5,6,7,8,9}
# print(len(a))