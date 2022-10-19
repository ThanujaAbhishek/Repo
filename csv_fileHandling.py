import csv
import os
path = (r"C:\Users\Admin\PycharmProjects\new project\files\csv_files")
os.chdir(path)
#read the data from excel- file
#reader()
'''with open("sample.csv") as file:
    reader_obj=csv.reader(file)
    for data in reader_obj:
        print(data)'''
#using dictionary
#DictReader()
'''with open ("sample.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        print(data)'''
#############################################################################################
#write data  to excel- sheet
#
'''with open("sample.csv","w") as file:
    writer_obj = csv.writer(file)
    #writing in single row
    writer_obj.writerow(["emp","emp_id"])
    writer_obj.writerow(["thanuja",289])
    #writing for multiple rows
    data = [["abhi",113],["thanu",345]]
    writer_obj.writerows(data)
    #(or)
    writer_obj.writerows([["aishu",123],["mom",567]])'''
#usinf DictWriter()
'''filename = ["emp","emp_id"]  #if we dont want any new line in between data then use newline=""
with open("sample.csv","w",newline="") as file:
    writer_obj = csv.DictWriter(file,["emp","emp_id"])
    writer_obj.writeheader()
    writer_obj.writerow({"emp":"bujji","emp_id":67})
    writer_obj.writerows([{"emp":"  charvi","emp_id":456},{"emp":"darsh","emp_id":45}])
#remove initial space
with open("sample.csv") as file:
    obj = csv.reader(file,skipinitialspace = True)
    for data in obj:
        print(data)'''
#############################################################
#1.write a program to read all the names of the employees in employee.csv file
'''with open("employees.csv") as file:
    reader_obj = csv.reader(file)
    #header = next(reader_obj)#--to skip header
    for data in reader_obj:
        print(data[0])
#using dictReader
with open("employee.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        print(data["name"])'''


#################################################################################
#2.writeva program toprint only the salaries that are > 70000
'''with open("employees.csv") as file:
    reader_obj = csv.reader(file)
    header = next(reader_obj)
    for data in reader_obj:
        if int(data[-1]) > 70000:
            print(data[-1])'''
#####################################################################################
#3.write a program to group male and female employees in the file
'''d ={}
with open("employees.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        if data["gender"] not in d:
            d[data["gender"]] = [data["name"]]
        else:
            d[data["gender"]] += [data["name"]]

print(d)'''
##################################################################################
#4.write a profram to group employees based on their team
'''d = {}
with open("employees.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        if data["team"] not in d:
            d[data["team"]] = [data["name"]]
        else:
            d[data["team"]] += [data["name"]]
print(d)'''
#########################################################################################
#5.write a program to sort the shares in test.csv file based on the share prices
'''with open ("test.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        print(sorted(reader_obj, key = lambda data : float(data["price"])))'''
d = {}
from collections import Counter
with open("test.csv") as file:
    reader = csv.DictReader(file)
    for data in reader:
        if data["shares"] != " ":
            d[data["name"]] = data["shares"]
c = Counter(d)
print(c)
# res = sorted(d.items(),key = lambda item :item[-1])
# print(res)
##########################################################################################3
#6.write a program to add all the shares in test.csv file
'''sum = 0
with open("test.csv") as file:
    reader_obj = csv.reader(file)
    header = next(reader_obj)
    print(list(reader_obj))
    for data in reader_obj:
        if data != []:
            sum = sum + int(data[1])
print(sum)'''


##########################################################################################
#7.Analysing vaccinations of all the countries
   #a. Total_vaccinations of all the countries











