'''
read operation
1.read () ---entire  file line as a single string, cant seperate line by line from local machine
2.readline()----one line at a time as a string at a time from local machine
3.readlines()---->a list of string/list of lines in the file from local machine
'''
from collections import Counter

#readline() -->file_object --iterator object(once it start moving forword  it wont go back)

#readlines()-->read entire file in the form of list
#import os
path = r"C:\Users\Admin\PycharmProjects\new project\files"
#os.chdir(path,"r")

#traversing through iterator object
#to get element present inside iterator object use below 3 ways
# typecasting
# traversing
# next()
#also called lazy object because it wont give next line untill we ask for it
#thats why we use next()
'''fil_obj = open(path)
for line in fil_obj:
    print(line)'''

#next()--->
'''print(next(fil_obj))'''
#when there no line to give in itterator object next() itterator throw StopIteration object
#for loop cant throw StropIteration object

################################################
#number of charatert present
'''obj = open(path,"r")
for line in obj:
    print(line,len(line))'''
######################################################
#number of words in file
#obj is a handle
'''obj =open(path,"r")
for line in obj:
    words =line.split()
    print(line,len(words))'''
############################################################
#print First word in each line
'''obj =open(path,"r")
for line in obj:
    if line.strip(): #--check line is empty or not
     words=line.split()
     print(words[0])#-->error in 4Th line b/c []
obj.close() #-->close the file  if we want to perform any operation on same file we need to open the file'''
##########################################################################################
#to close file automatically USE CONTEXT MANAGER
#using keyword called "With"
'''with open(path,"r") as file:'''
#here file will act as handle inside with block
#if we come out of with block we cant use file object anyewhere
#because if we come out of with block file will be closed automatically
#to check weather file is closed or not--Closed property--return True--If file is closed
'''for line in file:
        if line.strip():  # --check line is empty or not
         words = line.split()
         print(words[0])
        # print(file.closed)
print(file.closed)#--to check file is closed or not'''
######################################################################################
#to get time from sample.log
# log_path = r"C:\Users\Admin\PycharmProjects\new project\files\sample.log"
# with open(log_path) as log_file:
#     for line in log_file:
#         if line.strip():
#             time_col = line.split()
#             print(time_col[1])
#######################################################################
#to check how many time is repeated
log_path = r"C:\Users\Admin\PycharmProjects\new project\files\sample.log"
with open(log_path) as log_file:
    time_count = {}
    for line in log_file:
        if line.strip():
            logs = line.split()
            if logs[1] not in time_count:
                time_count[logs[1]] = 1
            else:
                time_count[logs[1]] += 1
print(time_count)

#counter(iterable)
with open(log_path)as file:
    time_list =[]
    for line in file:
        if line.strip():
            logs = line.split()
            time_list.append(logs[1])
print(time_list)
print(Counter(time_list))

##################################################################################

