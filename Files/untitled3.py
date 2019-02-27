alist = [10,20]
alist.append(30)

print("after append", alist)

alist.clear()

alist.extend([50,60,70,80,10,10])
print("after extending:", alist)
print("countof 10:", alist.count(10))

#reverse happens in place
alist.reverse
print(alist)

alist.sort()
print(alist)

## Dictionary methods

adict = {"chap1":10,"chap2":20,"chap3":30}
print("Dictonary elements :",adict)
print("only keys:",adict.keys())
print("only values: ",adict.values())
print("only values in list :",tuple(adict.values()))
print("items :",adict.items())