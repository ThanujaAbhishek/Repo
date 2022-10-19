# 1.. to print the number of charaters in a sample.txt file

import os
from builtins import enumerate, sorted

path = r"C:\Users\Admin\PycharmProjects\new project"
os.chdir(path)
'''with open("sample.txt", "x") as file:
    file.write("hello python")'''
'''with open ("sample.txt") as file:
    count_char = 0
    for line in file:
        for char in line:
            count_char += len(char)
print(count_char)'''
#without using len()
'''with open("sample.txt",)as file:
    count_char = 0
    for line in file:
        for char in line:
                 count_char += 1
        print(count_char)'''

####################################################################################
#2.. to count the number of words in a file
'''with open("sample.txt") as file:
    count_words = 0
    for line in file:
       words = line.split()
       count_words += len(words)
    print(count_words)
#without using len()
with open("sample.txt") as file:
    count = 0
    for line in file:
       words = line.split()
       for count_word in words:
          count += 1
    print(count)'''
#################################################################################
#3.print lines staring with vowels
'''with open ("sample.txt") as file:
    for line in file:
        if line.strip():
            if line[0] in 'aeiouAEIOU':
                print(line)'''
###########################################################################################
#4.. print line_no and number of words in a line
'''with open("sample.txt") as file:
    count = 0
    for line_no,line in enumerate(file,start = 1):
        if line.strip():
            for word in line.split():
                count += 1
            print(line_no,count)'''
           # (or)

# with open("sample.txt") as file:
#     for line_no,line in enumerate(file,start = 1):
#         words = line.split()
#     print(line_no,len(words))

#without using enumerate
'''with open("sample.txt") as file:
    line_no = 0
    for line in file:
        line_no += 1
        word = line.split()
        print(line_no,len(word))'''
####################################################################################
#5.to read a file from last line          #we cant reverse the file becouse it is object  #so typecast and read it
'''with open("sample.txt") as file:
    for line in list(file)[::-1]:
        print(line)

        #(or)
with open("sample.txt") as file:
    for line in reversed(list(file)):
        print(line)'''
##############################################################################################
#6..to count the no of spaces in file
'''with open("sample.txt") as file:
    count = 0
    for line in file:
        for char in line:
            if char == " ":
                count += 1
print(count)
 #(or) using built in
with open("sample.txt") as file:
    count= 0
    for line in file:
        count += line.count(" ")
    print(count)'''
################################################################################################
#8..to creat a dictionary with each word and its count pair in the file
'''d = {}
with open("sample.txt") as file:
    for line in file:
        if line.strip():
           words = line.split()
        for item in words:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
print(d)'''
##################################################################
#9. print the most occuring word in file
'''d = {}
with open("sample.txt") as file:
    for line in file:
        if line.strip():
            word = line.split()
            for item in word:
                if item not in d:
                    d[item] = item.count(item)
                else:
                    d[item] +=item.count(item)

*res,most = sorted(d.items(),key = lambda a:a[-1])
print(most)'''
#######################################################################################
#10.print nth line rom the file
'''n = 2
with open("sample.txt") as file:
    for line_no,line in enumerate(file,start = 1):
        if line_no == n:
          print(line)'''
##########################################################################################
#11 to print 2th to 5th lines
'''with open("sample.txt") as file:
    for line_no,line in enumerate(file,start = 1):
        if line_no == 2 or line_no <= 5:
            print(line)'''

            #(or)
'''with open("sample.txt") as file:
    count = 0
    for line in file:
        count += 1
        if 2 <= count < 5:
            print(line)'''
###################################################################################

from itertools import islice
'''n= 4
with open("sample.txt") as file:
    lines = islice(file,2)
    for line in lines:
        print(line)'''
    #(or)
'''from collections import deque
with open("sample.txt") as file:
    lines = deque(file,2)
    for line in lines:
        print(line)'''
#########################################################################################3
#print last nth line
n = 2
with open("sample.txt") as file:
    count = 0
    for line in file:
        count +=1
    file.seek(0)
    lines = islice(file,count-n,count)
    for i in lines:
        print(i)
#####################################################
#print ip address and their count from access-log file
'''d ={}
with open("access-log.txt") as file:
    for line in file:
        if line.strip():
            word = line.split()
            if word[0] not in d:
                d[word[0]] = 1
            else:
                d[word[0]] += 1
print(d)
  #(or)
l = []
with open ("access-log.txt")  as file:
    for line in file:
        if line.strip():
            word = line.split()
            l.append(word[0])
print(l)
#(or)
from collections import Counter
c = Counter(l)
print(c)
print(c.most_common(3))'''
######################################################################################33
#most occuring brand names from data.txt
'''from collections import defaultdict
dd = defaultdict(int)
with open("data.txt") as file:
    for line in file:
        brand = line.split()
        dd[brand[0]] += 1
print(dd)'''
##############################################################################################
#names of the countries from football.txt file
'''l = []
from collections import Counter
with open("football.txt",encoding = "UTF-8") as file:
    for line in file:
        country = line.split()
        l.append(country[1])
print(l)
print(Counter(l))'''





















