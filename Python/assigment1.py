# 1) The cover price of a book is $24.95, but bookstores get a 40 percent discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. Calculate the total wholesale costs for 60 copies.

# 

# cp = 24.95
# dr = 0.60
# q = 60

# # Calculate the discounted price per book
# dp = cp * (1 - dr)
# tc = dp * q

# # Calculate the shipping cost: $3 for the first copy, $0.75 for others
# sc = 3.00 + (0.75 * (q - 1))

# # Total wholesale cost
# twc = tc + sc

# print("Total wholesale cost for ",q," copies: $",twc)



# 2) You look at the clock and see that it is currently 14.00h. You set an alarm to go off 535 hours later. At what time will the alarm go off? Write a program that prints the answer. Hint: for the best solution, you will need the modulo operator



# ct=14
# at=535

# acut=(ct+at)%24
# print(acut)




# 3) Write code that can compute the surface of circle, using the variables radius and pi = 3.14159. The formula, in case you do not know, is radius times radius times pi. Print the outcome of your program as follows: “The surface area of a circle with radius ...is ...”


# r=int(input("enter radius: "))
# sa=r*r*3.14159
# print("surface area = ",sa)


# 4) Write code that classifies a given amount of money (which you store in a variable named amount), specified in cents, as greater monetary units. Your code lists the monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), and pennies (1 ct). Your program should report the maximum number of dollars that fit in the amount, then the maximum number of quarters that fit in the remainder after you subtract the dollars, then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters, and so on for nickels and pennies. The result is that you express the amount as the minimum number of coins needed.


# amount=int(input("enter amount : "))

# dollars=0
# quarters=0
# dimes=0
# nickels=0
# pennies=0

# if(amount>=100):
#     dollars=amount//100
#     amount=amount%100

# if(amount>=25):
#     quarters=amount//25
#     amount=amount%25

# if(amount>=10):
#     dimes=amount//10
#     amount=amount%10

# if(amount>=5):
#     nickels=amount//5
#     amount=amount%5

# else:
#     pennies=amount

# print("dollars: ",dollars,"quarters: ",quarters,"dimes: ",dimes,"nickels: ",nickels,"pennies: ",pennies)


# 5) Ask the user to enter three numbers. Then print the largest, the smallest, and their average, rounded to 2 decimals



# n1 = float(input("Enter the first number: "))
# n2 = float(input("Enter the second number: "))
# n3 = float(input("Enter the third number: "))

# numbers = [n1, n2, n3]


# largest = max(numbers)
# smallest = min(numbers)
# average = sum(numbers) / 3


# print("Largest: ",largest)
# print("Smallest: ",smallest)
# print("Average: ",average)
# print("round off: ",round(average))



#  6) Grades are values between zero and 10 (both zero and 10 included), and are always rounded to the nearest half point. To translate grades to the American style, 8.5 to 10 become an “A,” 7.5 and 8 become a “B,” 6.5 and 7 become a “C,” 5.5 and 6 become a “D,” and other grades become an “F.” Implement this translation, whereby you ask the user for a grade, and then give the American translation. If the user enters a grade lower than zero or higher than 10, just give an error message. You do not need to handle the user entering grades that do not end in .0 or .5, though you may do that if you like – in that case, if the user enters such an illegal grade, give an appropriate error message.


# a = float(input("enter grade: "))
# if(0<=a<=10):
#     if(8.5<=a<=10):
#         print("A")
#     elif(7.5<=a<=8.5):
#         print("B")
#     elif(6.5<=a<=7.5):
#         print("C")
#     elif(5.5<=a<=6.5):
#         print("D")
#     else:
#         print("F")
# else:
#     print("error")





# 7) Ask the user to supply a string. Print how many different vowels there are in the string. The capital version of a lower case vowel is considered to be the same vowel. y is not considered a vowel. Try to print nice output (e.g., printing “There are 1 different vowels in the string” is ugly). Example: When the user enters the string “It’s Owl Stretching Time,” the program should say that there are 3 different vowels in the string.


# text = input("Enter a string: ")

# text = text.lower()

# vowels = ["a", "e", "i", "o", "u"]

# found_vowels = []

# for c in text:
#     if c in vowels and c not in found_vowels:
#         found_vowels.append(c)

# num_vowels = len(found_vowels)

# if num_vowels == 1:
#     print("There is 1 different vowel in the string. => ",found_vowels)
# else:
#     print("There are", num_vowels, "different vowels in the string. => ",found_vowels)








