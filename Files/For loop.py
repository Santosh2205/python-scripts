for val in range(1,10):
    print(val)
print("--------")
    
for val in range(2,10,2):
        print(val)
print("___________")
for val in range(1,10,2):
    print(val)

for val in range(100,1,-1):
    print(val)

##for loop with string
name="python"
for char in name:
    print(char)
## for loop with list
alist = [10,20,30,40]
for val in alist:
    print(val)
## for loop with dictinary
book={"char1":10,"char2":20}
for key in book:
    print(key)
    print("Value:",book[key])
## write a program to display all the list if IPs in the below format.
string="192.168.0."
for val in range(1,100,1):
    ip = string + str(val)
    print(ip)

##___________________

string="192.168."
for val in range(0,2,1):
    ip1=string + str(val) + "."
    for val in range(1,10,1):
        ip=ip1 + str(val)
        print(ip)
##write a program to display all the list if IPs in the below format.
string="http://www."
alist=["google","unix","facebook","linkedin"]
for val in alist:
    b=string + str (val) +".com"
    print(b)








