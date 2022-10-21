#csv file will be saved with .csv extension stroded in the form of excel sheet
# csv is a data seperated with comma
# 3 operation in file handling
# open
#read / write
#close
import csv

path = r"C:\Users\Admin\PycharmProjects\new project\files\csv_files\sample.csv"
'''with open(path) as csv_file:
    for line in csv_file:
        print(line)
        print(type(line))'''
""" 
1. open csv file
2.read /write
3. close file


reading operation in csv file

1. reader()  --read the data in the form of list
2.DictReader()--read the data in the form of dictionary -

"""
'''with open(path) as file:
    reader_obj = csv.reader(file)
    print(reader_obj)  #typecast # traverse # next()
    for row in reader_obj:
        print(row)'''

'''with open(path) as file:
    reader_obj = csv.DictReader(file)
    print(reader_obj)  #typecast # traverse # next()
    for row in reader_obj:
        print(row)'''
###########################################################################
#to count number of rows in sample.csv file
'''with open(path) as file:
    reader_obj = csv.reader(file)
    header = next(reader_obj) #to skip header (1st line is always heading)
    count = 0
    for no_rows in reader_obj:
        count += 1
    print(count)'''
###############################################################################
#to read only female emplouee in employees.csv file

#reader()  #dificullt to remember the position so go for DictReader()
'''with open(path) as csv_file:
    reader_obj = csv.reader(csv_file)
    header = next(reader_obj)

    for row in reader_obj:
        if row[1] =='female':
            print(row)'''

#DictReader()
'''with open(path) as csv_file:
    reader_obj = csv.DictReader(csv_file)

    for row in reader_obj:
        if row["gender"] == "female":
            print(row)'''
#################################################################################################
#to write data into sample.csv file

"""
1.writer()--will take list(other than dictionary can pass all coolection object) of values as input
2.DictWriter()--will take only dictionary
"""

"""
to write data we have 2 methods
1.writerow--single data
2.writerows--multuple data

"""
'''with open(path,"w") as file:
    writer_obj = csv.writer(file)
    writer_obj.writerow("hello")  #extend each char as single elemet'''

with open(path,"w") as file:
    writer_obj = csv.DictWriter(file,["name","age"])
    writer_obj.writerow({"name":"ram","age":20})
    writer_obj.writeheader() #to print header

    #writerows will take list of dictionary

####################################################################################

