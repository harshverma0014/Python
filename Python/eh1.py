import mod

# a=mod.intvalue()
# b=mod.floatvalue()

# c=a+b
# print("total=",c)


while True:
 try:
    k=mod.intvalue()
    if not (k>=0 and k<=100):
        raise(Exception("invalid marks plss enter value btw 0 and 100... "))
    break
 except Exception as e:
    print("error : ",e)