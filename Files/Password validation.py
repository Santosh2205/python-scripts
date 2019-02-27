name = input("Enetr your password :")
print(name)
C=("$" in name or "#" in name or"@" in name)
B=name.__len__()
if C== True and B >= 6 and B <= 12:
    print("Valid Password")
else:
    print("Invalid Password")

print("________________________")

##Ip Address confermation
name = input("Enetr IP address :")
print(name)
A=name.split(".")
print(A[3])
if A[3] !="":
    print("Valid IP")
else:
    print("Invalid IP")
    