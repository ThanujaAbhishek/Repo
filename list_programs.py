#1.	Write program to merge two different lists.
'''l1 = [1,2]
l2 = [4,5]
print(l1+l2)'''
##################################################################
#2.	Remove duplicates from the list without using inbuilt functions
'''l1 = [1,2,3,4,2]
l2 =[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)'''

###################################################################
#3.	How to get the elements that are in list b but not in list a
# a = [1, 2, 3]
# b = [1, 2, 3, 4,5]
# for ele in b:
#     if ele not in a:
#         print(ele)
#####################################################################
#4.	Print all the numbers in the below list
'''a = ['abc', '123', 'hello', '23']
for ele in a:
  if ele.isdigit():
      print(ele)'''
############################################################33333333
#5.	Write a program to get alternate characters of a string in list format
# string = "hello python"
# print(list(string[::2]))
########################################################################
#6Write a program to iterate through list and build a new list, only if the items of the list have even number of characters.
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# l = []
# for ele in names:
#     if len(ele) % 2== 0:
#         l.append(ele)
# print(l)
########################################################################3333
#7.	Write a Program to print the sum of entire list and sum of only internal list
'''l = [[1,2,3],[4,5,6],[7,8,9]]
sum1 = 0
sum2 = 0
for i in l:
    sum2 = sum(i)
    print("sum of internal list",sum2)
    for x in i:
        sum1 += x
print("sum of entire list",sum1)'''
##########################################################################
#8.	Write a program to reverse the list as below
'''words = ["hi", "hello", "python"]
# o/p = ["nohtyp","olleh","ih"]
l2 = []
for ele in words[::-1]:
    l2.append(ele[::-1])
print(l2,end = " ")'''
########################################################################
#9.	Write a list comprehension to get a list of even numbers from 1-50
'''l = []
for i in range(1,51):
    if i % 2 == 0:
        l.append(i)
print(l)'''

#list comprehension
'''l =[i for i in range(1,51) if i % 2 == 0]
print(l)'''
#############################################################################
#10.Write a program to find the duplicate elements in the list without using inbuilt functions
'''names = ['apple', 'google', 'apple', 'yahoo', 'google']
new_list = []
for elements in names:
    if elements not in new_list:
        new_list.append(elements)
    else:
        print("duplicate elements are :", elements)'''
##########################################################################################
#11.Write a program to count the number occurrences of each item in the list without using any inbuilt functions
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo','apple']
'''new_dict = {}
for element in names:
    if element not in new_dict:
        new_dict[element] = 1
    else:
        new_dict[element] += 1
print(new_dict)'''
#comprehension


##########################################################################################33
#12.	Write a program to find the largest number in the list without using any inbuilt functions
numbers = [10, 20, 30, 40, 50]






