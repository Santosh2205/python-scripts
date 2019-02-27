#Method 1

import math
print(math.ceil(4.9))
print(math.tan(3))

#Method 2 - accessing methods with alias name

import math as m
print(m.ceil(4.9))
print(m.tan(3))

#Method 3 - importing only required methods

from math import ceil,log

print(ceil(4.9))
print(log(3))

#Method 4 - importing all methods

from math import*
print(ceil(4.9))

import os
print(os.listdir())

os.unlink("Path of file") #to remove file
os.remove("Path of file")

os.rename("path/to/current/file.foo", "path/to/new/desination/for/file.foo") #to move file from one path to another path

shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

#write a programme to display only CSV files from the current path
import os
import glob

path = 'C:\\Users\\Spatole2\\Desktop\\datasets-master'
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
print(result)
#______________________________________
#CSV file handelling
import csv
with open("employees.csv") as fobj:
    reader=csv.reader(fobj)
    for line in reader:
        print(line)
        
        

#write a program to display all the.py files and its size
import os
for file in os.listdir():
    if os.path.isfile(file):
        filesize=os.path.getsize(file)
        print("Filename:", file)
        print("size:",filesize,"bytes")
        

#write a program to remane the files from .csv to .txt present in current directory
import os
import glob

path = 'C:\\Users\\Spatole2\\Desktop\\datasets-master'
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
print(result)



