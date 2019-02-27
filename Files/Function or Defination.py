
##function body


def add (first, second):
    total = first + second
    return total

print("Program begins from here:")
gettotal=add(10,20)
print("Sum of the numbers:",gettotal)
gettotal=add(101,200)
print("Sum of the numbers:",gettotal)
gettotal=add(10001,20020)
print("Sum of the numbers:",gettotal)
gettotal=add(1,20)
print("Sum of the numbers:",gettotal)

##defualt argument
def add (first, second, third=0):
    total = first + second
    return total

print("Program begins from here:")
gettotal=add(10,20)
print("Sum of the numbers:",gettotal)
gettotal=add(101,200,30)
print("Sum of the numbers:",gettotal)

##keywords agruments

def add (second, first):
    total = first + second
    return total

print("Program begins from here:")
gettotal=add(first = 10,second = 20)
print("Sum of the numbers:",gettotal)
gettotal=add(second = 101,first = 200)
print("Sum of the numbers:",gettotal)

## Veriable argument
l
def display(*data):
    print(data)
    for item in data:
        print(item)
    
    
display(10,20,30,40,60,70,80,["a"],["b"],["data",exit])