# 1. Write a Python program to calculate the length of a string.  

# a=input('enter string : ')

# print(len(a))





# 2. Write a Python program to count the number of characters (character frequency) in a string.  Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}



# sample_string = 'google.com'
# frequencies = {}
    
# for char in sample_string:
#     if char in frequencies:
#          frequencies[char] += 1
#     else:
#         frequencies[char] = 1
# print("Expected Result : ",frequencies)


# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.  Sample String : 'w3resource'
# Expected Result : 'w3rgfgfgfce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


# a='w2esouce'

# if(len(a)>=2):
#     print(a[:2]+a[-2:])
# else:
#     print("Empty string")




# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.  Sample String : 'restart'
# Expected Result : 'resta$t'


# a="restart"
# b=a[0]
# if b in a:
#     mod=a[1:].replace(b,'$')
# print(b+mod)
    

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.  
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


# a="abc"
# b="xyz"

# f=a[:2]
# s=b[:2]

# new=a.replace(a[:2],s)+" " +b.replace(b[:2],f)
# print(new)


# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.  
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'



# a="ag"

# if(len(a)>2):
#     if(a.endswith("ing")):
#        new=(a.replace(a[-3:],"ly"))
#     else:
#         new=a+"ing"
#     print(new)
# else:
#     print("not a string")


# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
  
# a = "The lyrics is not that poora!"

# s_not = a.find('not')

# s_poor = a.find('poor')

# if s_poor > s_not and s_not > 0 and s_poor > 0:
#     a = a.replace(a[s_not:s_poor+4], 'good')

# print(a)


# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.  
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9


# a= "is the Exercises good for health".split()

# maxi=a[0]
# for i in a:
#     if len(i) > len(maxi):
#         maxi=i
# print(len(maxi))




# 9. Write a Python program to remove the nth index character from a nonempty string.  
  
# a="yeh oh mai god"
# v= (input("enter nth : "))
# b=a.partition(v)
# print(b[0]+b[2])


# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.  
  

# a="The lyrics is good!"
# b=a[-1]
# c=a[0]
# middle=a[1:-1]
# m=b+middle+c
# print(m)



# 11. Write a Python program to remove the characters which have odd index values of a given string.  


# a="The lyrics is good!"
# new=a[0::2]
# print(new)


# 12. Write a Python program to count the occurrences of each word in a given sentence.  


# a="this is a string string".split()
# d={}
# for i in a:
#     b=a.count(i)
#     d[i]=b

# print(d)





#   13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.  
  

# a="The lyrics is good!"
# print(a.lower())
# print(a.upper())


#  14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).  
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red


# a = input()

# words = a.split(",")
# unique = list(set(words))
# unique.sort()

# print(",".join(unique))


#  15. Write a Python function to create the HTML string with tags around the word(s).  
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

# def tag(a,b):
#     v= "</"+a+">" +b+ "</"+a+">" 
#     return v

# a=input('enter tag : ')
# b=input('enter string : ')
# c=tag(a,b)
# print(c)



# 16. Write a Python function to insert a string in the middle of a string.  
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}




# def brck(a,b):
#     c=len(b)//2
#     v=b[:c]+a+b[c:]
#     return v

# a="python"
# b="[[[[]]]]"
# c=brck(a,b)
# print(c)



# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).  
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

# def re(b):
#     n=a[-2:]*4
#     return n

# a="python"
# v=re(a)
# print(v)



# 18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.  
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

# a="ipy"
# b=a[:3]
# print(b)


# 19. Write a Python program to get the last part of a string before a specified character.  
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python


# a=input("string : ")
# b=input("enter char : ")
# c=a.partition(b)
# print(c[0])

 
# 20. Write a Python function to reverses a string if it's length is a multiple of 4.  
  




# a="harsher"
# if(len(a) %4==0):
#     print(a[::-1])
# else:
#     print('string length is not divisble by 4')




# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.  
  

# a="Thhj jajrhs jassk"
# count=0
# for i in a[:4]:
#     if i.isupper():
#         count+=1
# if count>1:
#     print(a.upper())
# else:
#     print("it do not contain more than 2 capitals in starting")



# 22.Write a Python program to sort a string lexicographically. 
# a="w3resource"
# b=sorted(a)
# res="".join(b)
# print(res)



# 23. Write a Python program to remove a newline in Python.  
#   x=”xxxxx\nyyyyy”

# x = "xxxxx\nyyyyy"
# a=x.replace("\n","")

# print(a)



# 24. Write a Python program to check whether a string starts with specified characters.  


# x = "xxxxxyyyyy"
# a=input("enter char")
# if x.startswith(a):
#     print("the string strats with the giver char")
# else:
#     print("the string not strats with the giver char")



# 25. Write a Python program to create a Caesar encryption.  
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.


# a=" In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence."
# r=""
# for i in a:
#     b=ord(i)+2
#     r+=chr(b)
# print(r)





# 26. Write a Python program to display formatted text (width=50) as output



# sa = """
# The Caesar cipher is one of the earliest known and simplest methods of encryption. 
# It is a type of substitution cipher in which each letter in the plaintext is 
# replaced by a letter some fixed number of positions down the alphabet.
# """

# print("-"*50,"\n",sa,"\n","-"*50)



# 27. Write a Python program to remove existing indentation from all of the lines in a given text.  


# text = """    This is line 1
#         This is line 2
#     This is line 3"""

# lines = text.split("\n")

# for i in lines:
#     print(i.strip())

# 28. Write a Python program to add a prefix text to all of the lines in a string


# stext = """Line one
# Line two
# Line three"""


# prefix=">>> "

# lines=stext.splitlines()

# res=""
# for line in lines:
#     res+= prefix + line + "\n"

# print(res)



# 29. Write a Python program to set the indentation of the first line. 



# stext = """Line one
# Line two
# Line three"""

# indent="    "

# lines=stext.splitlines()
# lines[0]=indent+lines[0]

# res=""
# for i in lines:
#     res+= i +"\n"

# print(res)


# 30. Write a Python program to print the following floating numbers upto 2 decimal places.  
  

# i=-49.3945
# v=f"{i:+.2f}"

# print(v)


# 31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign. 




# i=-49.3945
# v=f"{i:+.2f}"

# print(v)

# 32. Write a Python program to print the following floating numbers with no decimal places.  


# i=-49.3945
# v=f"{i:+.0f}"

# print(v)


# 33. Write a Python program to print the following integers with zeros on the left of specified width
# a=49589.34
# i=int(input("enter input in num: "))
# b=i*"0"
# print(b+str(a))


# 34. Write a Python program to print the following integers with '*' on the right of specified width.  
# a=49589.34




# i=int(input("enter input in num: "))
# b=i*"*"
# print(str(a)+b)


# 35. Write a Python program to display a number with a comma separator.  



# v=39432942.3432


# b=f"{v:,}"

# print(b)


# 36. Write a Python program to format a number with a percentage.  


# n=10
# total=100
# per=(n/total)*100
# print(str(per)+"%")


# 37. Write a Python program to display a number in left, right and center aligned of width 10. 


# num = 42

# # < points Left
# print(f"|{num:<10}|")

# # > points Right
# print(f"|{num:>10}|")

# # ^ points Up/Center
# print(f"|{num:^10}|")


# 38. Write a Python program to count occurrences of a substring in a string.  

# a=" Write a Python program to count occurrences of a substring in a string.  "

# s="Write"

# res=a.count(s)
# print(res)


# 39. Write a Python program to reverse a string.  

# a="39. Write a Python program to reverse a string.  "

# print(a[::-1])


# 40. Write a Python program to reverse words in a string.  

# a="40. Write a Python program to reverse words in a string.  ".split()
# rev=""
# print(a)
# for i in a:
#     rev+=i[::-1]
#     rev+=" "
# print(rev)


# 41. Write a Python program to strip a set of characters from a string.  

# a="#####pytohnnn!!!!!!!!"

# rc="#!"
# c=a.strip(rc)
# print(c)



# 42. Write a Python program to count repeated characters in a string.  
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

# s= 'thequickbrownfoxjumpsoverthelazydog'
# res=[]

# for i in s:
#     if i not in res:
#         count=s.count(i)
#         if count>1:
#             print(i,count)
#         res.append(i)



# 43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.  
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3


# area = 1256.66
# volume = 1254.725
# print(str(area)+"cm\u00b2")
# print(str(volume)+"cm\u00b3")



  
# 44. Write a Python program to print the index of the character in a string.  
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9


# a="w2resource"

# for i in range(len(a)):
#     print("Current character ",a[i]," position at ",i) 



# 45. Write a Python program to check whether a string contains all letters of the alphabet.  

# a="ajhfffffffffaks".isalpha()
# print(a)


# 46. Write a Python program to convert a given string into a list of words.  
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
  

# a="'The quick brown fox jumps over the lazy dog."
# print(a.split())

# 47. Write a Python program to lowercase first n characters in a string
# a="The quick brown fox jumps over the lazy dog."
# n=int(input("enter num : "))
# print(a[:n].upper()+a[n:])

# 48. Write a Python program to swap comma and dot in a string.  
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

# a="32.0.54,23"

# b=(a.replace(",","f"))

# c=b.replace(".",",")

# d=c.replace("f",".")
# print(d)


# 49. Write a Python program to count and display the vowels of a given text.  

# a="harsh vemra"
# count=0
# for i in a:
#     if i in "aeiouAEIOU":
#         print(i,end=", ")
#         count+=1
# print(count)



# 50. Write a Python program to split a string on the last occurrence of the delimiter.  

# a="Python,Java,C++,Ruby"
# b=a.rsplit(",",1)
# print(b)


# 51. Write a Python program to find the first non-repeating character in given string.  

# a="harsh verma"
# for i in a:
#     b=a.count(i)
#     if b==1:
#         print(i)
#         break


# 52. Write a Python program to print all permutations with given repetition number of characters of a given string.  


# text = "xy"
# for i in text:
#     for f in text:
#         print(i+f)

# import itertools
# t="9109090924"
# s=itertools.permutations(t)
# for i in s:
#     print(''.join(i))



# 53. Write a Python program to find the first repeated character in a given string.  



# a="harsh verma"
# for i in a:
#     b=a.count(i)
#     if b>1:
#         print(i)
#         break


# 54. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest. 



# a="harsh verma"
# for i in a:
#     b=a.count(i)
#     if b>1:
#         print(i)
#         break

# 55.Write a Python program to find the first repeated word in a given string.  
  


# a="harsh verma"
# for i in a:
#     b=a.count(i)
#     if b>1:
#         print(i)
#         break


# 56. Write a Python program to find the second most repeated word in a given string.  
  


# a="harsh verma"
# p=0
# for i in a:
#     b=a.count(i)
    
#     if b>1:
#         p+=1
#         if(p==2):
#             print(i)
#             break




# 57.Write a Python program to remove spaces from a given string.  

# a="harsh vemra"
# print(a.replace(" ",""))


# 58. Write a Python program to move spaces to the front of a given string.  

# a="harsh vemra"

# b=a.count(" ")
# n=a.replace(" ","")
# print(" "*b,n)




# 59. Write a Python program to find the maximum occurring character in a given string.  


# a="hahrsh vemaaera"
# n=a.count(a[0])
# m=a[0]
# for i in a:
#     b=a.count(i)
#     if(b>n):
#         m=i
#         n=b

# print(m,n)

# 60. Write a Python program to capitalize first and last letters of each word of a given string.  

# a="harsh vemra ".title()
# w=a.find(" ")
# b=a[:w] + a[w-1].upper 
# print(b)  



# 61. Write a Python program to remove duplicate characters of a given string.  

# a = "harsh verma"
# result = ""

# for i in a:
#     if i not in result:
#         result = result + i

# print(result)

# 62. Write a Python program to compute sum of digits of a given string.  
# a="244"
# s=0
# for i in a:
#     s+=int(i)

# print(s)


# 63. Write a Python program to remove leading zeros from an IP address. 


# ip = "192.168.001.009"
# for i in ip:
#     if i=="0":
#         nip=ip.replace(i,"")


# print(nip)




# 64. Write a Python program to find maximum length of consecutive 0's in a given binary string.  

# a="111000010000110"
# max=0
# count=0
# for i in a:
#     if(i=='0'):
#         count+=1
#     else:
#         if(count>max):
#             max=count
#         count=0
# print(max)
        

# 65. Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print "No common characters".  
# a = "harsh"
# b = "rohan"

# c = set(a) & set(b)

# if c:
#     print("".join(sorted(c)))
# else:
#     print("No common characters")



# 66. Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings.  
  



# a = "earth"
# b = "heart"

# count = 0

# for ch in a:
#     if ch in b:
#         b = b.replace(ch, "", 1)
#     else:
#         count += 1

# count += len(b)

# print("Characters to remove  =>", count)


# 67. Write a Python program to remove all consecutive duplicates of a given string.  
# a = "aabbbbeeeeffggg"
# b=""
# for i in a:
#     if i not in b:
#         b+=i
# print(b)


# 68. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string.  

# a="this is a sample string "
# os=""
# ms=""
# for i in a:
#     if a.count(i)>1:
#         if i not in ms:
#            ms+=i+' '
#     else:
#         os+=i+' '
# print(os,'\n',ms)

# 69. Write a Python program to find the longest common sub-string from two given strings.  

# a="this is a sample string ".split()
# b="yesssh this must be a string".split()
# c=""
# for i in a:
#     if i in b:
#         if len(i) > len(c):
#             c=i
            
# if c:
#     print("Longest common word:", c)
# else:
#     print("No common words found")


# 70. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.  

# a="this is a sample string ".split()
# b="yesssh this must be a string".split()
# c=""
# for i in a:
#     if i in b:
#         c+= i+" "
            
# if c:
#     print( c)
# else:
#     print("No common words found")


# 71. Write a Python program to move all spaces to the front of a given string in single traversal.  

# text = "Python Exercises"

# spaces = ""
# letters = ""

# for char in text:
#     if char == " ":
#         spaces += char
#     else:
#         letters += char

# result = spaces + letters


# print(result)


# 72. Write a Python code to remove all characters except a specified character in a given string.  
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P
# Original string
# google
# Remove all characters except g in the said string:
# gg
# Original string
# exercises
# Remove all characters except e in the said string:
# eee


# a="google"
# b=input("enter char: ")
# s=""
# for i in a:
#     if i == b:
#         s+=i

# print(s)

# 73. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.  

# text = "Hello @ 123 World!"

# # Initialize counters
# u_count = 0  # Uppercase
# l_count = 0  # Lowercase
# n_count = 0  # Numeric
# s_count = 0  # Special characters

# for char in text:
#     if char.isupper():
#         u_count += 1
#     elif char.islower():
#         l_count += 1
#     elif char.isdigit():
#         n_count += 1
#     else:
#         # If it's not a letter or digit, it's a special character/space
#         s_count += 1

# print(u_count)
# print(l_count)
# print(n_count)
# print(s_count)



# 74. Write a Python program to find the minimum window in a given string which will contain all the characters of another given string.  
# Example 1
# Input : str1 = " PRWSOERIUSFK "
# str2 = " OSU "
# Output: Minimum window is "OERIUS"


# str1 = "PRWSOERIUSFK"
# str2 = "OSU"

# a=str2[0]
# b=str2[-1]

# c=str1.find(a)
# d=str1.find(b)

# print(str1[c:d+1])

#  75. Write a Python program to find smallest window that contains all characters of a given string.  
  

# str1 = "PRWSOERIUSFK"
# str2 = "OSU"

# a=str2[0]
# b=str2[-1]

# c=str1.find(a)
# d=str1.find(b)

# print(str1[c:d+1])


# 76. Write a Python program to count number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters.  

# a="this is this a this python this string "
# b=input("enter string => ")

# c=a.count(b)
# print(c)



# import itertools
# a="ascd"
# b=list(itertools.permutations(a,2))
# print(len(b))




# 77. Write a Python program to count number of non-empty substrings of a given string.  




# text = "abdc"
# n = len(text)
# count=0
# for i in range(n):
#     for j in range(i,n):
#         count+=1

# print(count)


#   78. Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet


# text = "abc".upper()
# n=len(text)
# count=0
# for i in range(n):
#     if ord(text[i]) - ord('A') == i:
#         count+=1
#         print("match fount at ",i)
# print( "toatal : ",count)

# 79. Write a Python program to find smallest and largest word in a given string

# a="this is a string".split()
# mi=min(a,)
# ma=max(a,)

# print(mi,ma)


# 80. Write a Python program to count number of substrings with same first and last characters of a given string.  


# a="radar"
# count=0
# n=len(a)
# for i in range(n):
#     for j in range(i,n):
#         c=a[i:j+1]
#         if c[0]==c[-1]:
#             count+=1
# print(count)



# 81. Write a Python program to find the index of a given string at which a given substring starts. If the substring is not found in the given string return 'Not found'.  
  


# a="radar"
# b="da"

# ind=a.find(b)
# if(ind != -1):
#     print(ind)

# else:
#     print("not found")


# 82. Write a Python program to wrap a given string into a paragraph of given width.  
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick
# brown fox.
  

# a="The quick brown fox."
# w=10
# for i in range(0,len(a),w):
#     print(a[i:i+w])


# 83. Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer.  
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001


# num = 25

# d = str(num)
# o = oct(num)[2:]
# h = hex(num)[2:].upper()
# b = bin(num)[2:]

# print(d, o, h, b)


# 84. Write a Python program to swap cases of a given string.  
# Sample Output:
 # pYTHON eXERCISES

# a="Python Exersises"
# for i in a:
#     if i.isupper():
#         print(i.lower(),end="")
#     else:
#         print(i.upper(),end="")

# 85. Write a Python program to convert a given Bytearray to Hexadecimal string.  
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d




# def gethexa(l):
#     e=[]
#     for i in l:
#         e.append(hex(i)[2:])
#     return ''.join(e)
# a=[111,12,45,67,109]
# t=gethexa(a)
# print(t)





# a=[111,12,45,67,109]
# b=""
# for i in a:
#     b+=hex(i)[2:]+" "


# print(b)



# 86. Write a Python program to delete all occurrences of a specified character in a given string.  
# Sample Output:
# Original string:
# Delete all occurrences of a specified character in a given string
# Modified string:
# Delete ll occurrences of specified chrcter in given string



# a="Delete all occurrences of a specified character in a given string"

# ch="a"

# b=a.replace(ch,"")

# print(b)




# 87. Write a Python program find the common values that appear in two given strings.  
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python


# a="Python3"
# b="Python2.7"
# v=""
# for i in a:
#     if i in b and i not in v:
#         v+=i

# print(v)



# 88. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.  
# Sample Output:
# Input the string: W3resource
 # ['Valid string.']
  

# a="this is a String  this is a string"
# mil=10
# up=False
# lo=False
# nu=False
# len=len(a)>=mil

# for i in a:
#     if i.isupper():
#         up=True
#     if i.islower():
#         lo=True
#     if i.isdigit():
#         nu=True
# if( up and lo and nu ):
#     print("valid ")
# else:
#     print("invalid")


# 89. Write a Python program to remove unwanted characters from a given string.  
# Sample Output:
# Original String : Pyth*^on Exercis^es
# After removing unwanted characters:
# Python Exercises
# Original String : A%^!B#*CD
# After removing unwanted characters:
 # ABCD
# a="Pyth*^on Exercis^es"
# for i in a:
#     if i.isalnum() or i ==" ":
#         print(i,end="")




# 90. Write a Python program to remove duplicate words from a given string.  
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution

# a="Python Exercises Practice Solution Exercises".split()
# res=''
# for i in a:
#     if i not in res:
#         res+=i+ " "

# print(res)


# 91. Write a Python program to convert a given heterogeneous list of scalars into a string.  
# Sample Output:
# Original list:
# ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# Convert the heterogeneous list of scalars into a string:
# Red,100,-50,green,w,3,r,12.12,False
  
# a=['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# res=""
# for i in a:
#     res+=str(i)+","

# print(res)




# 92. Write a Python program to find the string similarity between two given strings.  
# Sample Output:
# Original string:
# Python Exercises
# Python Exercises
# Similarity between two said strings:
# 1.0
# Original string:
# Python Exercises
# Python Exercise
# Similarity between two said strings:
# 0.967741935483871
# Original string:
# Python Exercises
# Python Ex.
# Similarity between two said strings:
# 0.6923076923076923
# Original string:
# Python Exercises
# Python
# Similarity between two said strings:
# 0.5454545454545454
# Original string:
# Java Exercises
# Python
# Similarity between two said strings:
# 0.0


# a = "earth"
# b = "heart"

# count = 0

# for ch in a:
#     if ch not in b:
#         count += 1
        

# print(count)






# 93. Write a Python program to extract numbers from a given string.  
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]


# a="red 12 black 45 green".split()

# b=[]
# for i in a:
#     if i.isdigit():
#         b.append(int(i))

# print(b)


# 94. Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.  
# Sample Output:
# (255, 165, 1)
# (255, 255, 255)
# (0, 0, 0)
# (255, 0, 0)
# (0, 0, 128)
# (192, 192, 192)
  

# h = "FFA501"  

# r_hex = h[0:2]
# g_hex = h[2:4]
# b_hex = h[4:]

# r = int(r_hex, 16)
# g = int(g_hex, 16)
# b = int(b_hex, 16)

# rgb = (r, g, b)

# print(rgb)





# 95. Write a Python program to convert the values of RGB components to a hexadecimal color code.  
# Sample Output:
# FFA501
# FFFFFF
# 000000
# 000080
# C0C0C0

# L=[]
# abc='FFFFFF'
# for i in range(len(abc)-1):
#     if i % 2 == 0:
#         L.append(int((abc[i:i+2]),16))

# print(tuple(L))

# 96. Write a Python program to convert a given string to camelcase.  
# Sample Output:
# javascript
# fooBar
# fooBar
# foo.Bar
# fooBar
# foobar
# fooBar

# other_words=""
# s = "foo bar loo"

# s = s.replace(".", " ").replace("-", " ")

# words = s.split()


# first_word = words[0].lower()
# for w in words[1:]:

#     other_words +=w.capitalize() 
    
# result = first_word + other_words

# print(result)



# 97. Write a Python program to convert a given string to snake case.  
# Sample Output:
# java_script
# foo_bar
# foo_bar
# foo.bar
# foo_bar
# foo_bar
# foo_bar

# s = "Foo Bar"

# s = s.replace(".", " ").replace("-", " ")

# words = s.lower().split()

# result = "_".join(words)

# print(result) 



# 98. Write a Python program to decapitalize the first letter of a given string.  
# Sample Output:
# java Script
# python

# a="String"
# b=a[0].lower()
# c=a[1:]
# d=b+c
# print(d)






  
# 99. Write a Python program to split a given multiline string into a list of lines.  
# Sample Output:
# Original string: This
# is a
# multiline
# string.
# Split the said multiline string into a list of lines:
# ['This', 'is a', 'multiline', 'string.', '']



# a="""This
# is a
# multiline
# string.
# """.splitlines()
# b=[]
# for i in a:
#     b.append(i)
# print(b)



# 100. Write a Python program to check whether any word in a given sting contains duplicate characrters or not. Return True or False.  
# Sample Output:
# Original text:
# Filter out the factorials of the said list.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# Python Exercise.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# The wait is over.
# Check whether any word in the said sting contains duplicate characrters or not!
# True


# a="Filter out the factorials of the said list.".split()

# for i in a:
#     if i not in a[a.index(i)+1:]:
#         print("false")
#         break
#     else:
#         print("true")



# 101. Write a Python program to add two strings as they are numbers (Positive integer values). Return a message if the numbers are string.  
# Sample Output:
# 42
# Error in input!
# Error in input!

# s1 = "10"
# s2 = "32"

# if s1.isdigit() and s2.isdigit():
#     print(int(s1) + int(s2))
# else:
#     print("Error in input!")





























































































