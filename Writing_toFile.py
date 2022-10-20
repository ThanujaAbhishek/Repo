#open a file for write operation----without context manager
#write mode will create a new file everytime if it is already existing it will override it
#everytime it will create a new file
"""write methods
#1. write()-->can write single line
#2.writelines() -->it will take list of strings
"""
from collections import deque, Counter
from itertools import islice

#file_obj =open(path,"w)
path = r"C:\Users\Admin\PycharmProjects\new project\files\sample1.txt"
'''with open(path,"w")as file:
    file.write("helloworld\n")
    file.writelines(["hai\n","hello\n"])'''
########################################################################
#opening file in create mode
#file_obj =open(path,"x)
#if file is already present create mode will throw error
#always checck first if already present or not
#we cant read file in "x" mode
#we can write using "x" mode
#only in "r" mode we can read
'''with open(path,"x") as file:
    print(file.read())'''
#######################################################################
#read and write operation
# r/w
'''with open(path,"r+")as file:
    file.write("thanu\n")
    file.seek(0)#-->seek() will take position of character as index not lines
    for line in file:
        print(line)'''
#############################################################################3
#print only %th line
'''with open(path) as file:
    count = 0
    for line in file:
        count += 1
        if count == 5:
            print(line)
            break'''
###############################################################################
'''line_num = 5
with open(path) as file:
    count = 0
    for line in file:
        count += 1
        if count == line_num:
            print(line)
            break'''
'''expected_line_no = 5
with open(path) as file:
    for line_num,line in enumerate(file,start = 1):
        if line_num == expected_line_no:
            print(line)
            break'''
######################################################################
#whenever we want to slice a itterator object we use islice
#normally using slice[:] operator we cant slice iterartor object
#islice is a class
#from itertools import islice
#   islice
''''a= [12,56,24,97,100,23]
b = iter(a)
from itertools import islice
obj = islice(b,0,2)
#(b,0,2)  --> (obj,start index,end index)
#(b,2)  -> (obj,end index)
print(list(obj))'''
########################################################################
#to read 5th line
'''line_num = 5
with open(path) as file:
    lines = islice(file,line_num-1,line_num)
print(list(lines))'''
#####################################################################
#to read first 3 lines
'''with open(path) as file:
    lines = islice(file,3)
    print(list(lines))'''
################################################################
#to getlast 3 lines
#[len(a)-3: len(a)]
'''with open(path) as file:
    file_length = 0
    for line in file:
        file_length += 1
    file.seek(0)
    lines = islice(file,file_length-3,file_length )
    print(list(lines))'''
#######################################################################3
#deque()-->to get last few elements

with open(path) as file:
    lines = deque(file,3)
    print(list(lines))
####################################################################
#counter() ---> count the character
#count the number of elements present in iterator object
string = "hello world"
obj = Counter(string)
print(obj)
print(dict(obj))#---> #o/p will be in dicticonary
#to get most repeating character
print(obj.most_common())  #--o/p: list of tuples
print(obj.most_common(2)) #--most common elements
#above comment will give 2 most common elements




