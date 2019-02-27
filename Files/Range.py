##syntax:range (start,stop,stop)

print(list(range(1,10)))
print(tuple(range(3,9)))
print(list(range(2,10,2)))
print(list(range(1,100,2)))

##write a program to capture any name from keyboard and perform the below oepations.
# if length of the string is less than 10.... string is too small
#is lenght of the string is greter than 30.. string is too big

name=input("enter any name :")
print(name)
print(name.__len__())

B=name.__len__()
print(B)
if B<10:
    print("string is too small")
elif B>30:
    print("String is too big")


'''_______________________'''

