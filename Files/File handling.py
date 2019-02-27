## File handling

fobj=open("demo.txt","w")
fobj.write("python programming\n")
fobj.write("ruby programming\n")
fobj.write("scala programming\n")
fobj.close()

## Eg
##write a program to capture any string from keyboard and write the output to the file.
name = input("Enetr any text :")
fobj=open("demo.txt","w")
fobj.write(name)
fobj.close()

## Eg 2
'''
write a program to write all the odd numbers from 700 to 400 to the file and the
file name should be with today's timestamp.
Eg: 27_Feb_2019.txt
'''
'''__________________________________________'''

#File read operations

'''reading file by line by line'''

fobj=open("demo.txt","r")
for line in fobj:
    #remove white space at the end of each line
    line=line.strip()
    #split the line with , as the delimeter
    data=line.split(",")
    #display last field
    print(data[0])
fobj.close()

#______________________________________

fobj=open("C:\\Users\\Spatole2\\Desktop\\datasets-master\\employees.csv","r")
for line in fobj:
    line=line.strip()
    if "Female" in line:
        print(line)
fobj.close()

#_____________________________________

fobj=open("C:\\Users\\Spatole2\\Desktop\\datasets-master\\employees.csv","r")
f=0
m=0
for line in fobj:
    line=line.strip()
    if "Female" in line:
        f=f + 1
    else:
        if "Male" in line:
            m=m + 1
print("No.pf female employees: -",(f))
print("No.pf male employees: -",(m))
    
fobj.close()
#________________________________________

fobj=open("C:\\Users\\Spatole2\\Desktop\\datasets-master\\employees.csv","r")
line=fobj.readline() # ignore header
count=0
for line in fobj:   
    s = line.split(",")
    if int(s[4]) > 100000:
        print(s)
        if count==5:
            break
        count=count+1
fobj.close()

#____________________________________________

fr=open("C:\\Users\\Spatole2\\Desktop\\datasets-master\\employees.csv","r")
fw=open("C:\\Users\\Spatole2\\Desktop\\datasets-master\\employees.csv","w")

for line in fr:
    line = line.strip()
    line=line.replace("Marketing","IT")
    fw.write
fr.close()
fw.close()

# contex manager

with open("C:\\Users\\Spatole2\\Desktop\\datasets-master\\employees.csv","r") as fobj:
    data = fobj.readlines()
for line in data[4:10]:
    print(line)
    