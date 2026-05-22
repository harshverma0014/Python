def intvalue():
 while True:
  try:
   i=int(input("enter int : "))
   return i
  except ValueError as e:
   print("ple enter integer value only... ")
   print(" error : ",e)



def floatvalue():
 while True:
  try:
   i=float(input("enter float : "))
   return i
  except ValueError as e:
   print("ple enter float value only... ")
   print(" error : ",e)


