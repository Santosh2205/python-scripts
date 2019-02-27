##Break = Come out of the loop if some condition is meet

userinput = int (input("enter any value:"))
for val in range (1,10):
    if val == userinput:
        break
    print(val)


##Continue = It skips the current iteration
userinput = int (input("enter any value:"))
for val in range (1,10):
    if val == userinput:
        continue
    print(val)
