a=10
b=20

if a < b :
    print("Inside if ")
    print("A is less than B")
else:
    print("Outside if")

name = "python"
if name.isupper():
    print("This is upper")
elif name.islower():
    print("This is lower")
elif name.isdigit():
    print("string is digit")
else:
    print("None of this")


name = input("Enetr any Filename :")
print(name)
A = name.split(".")
print(A[1])

if A[1]=="py":
    print("python file")
elif A[1]=="txt":
    print("text file")


