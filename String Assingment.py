#program to check if givven data type is of string data type
'''String = "hai"
if isinstance(String,str):
    print(f"{String} is a string datatype")'''
##############################################################################
# 2..program to print elements present in even index
'''String = "programming language"
print(String[::2])'''
###############################################################################3
#3..	program to print alternate characters in the string
'''String = "python language"
print(String[::2])'''
########################################################################3
#4.	program to reverse a string using slicing
'''string = "hai everyone"
print(string[::-1])'''
############################################################################
#5.	"program to convert uppercase to lowercase characters with and without inbuilt methods."
'''string = "HAI GOODMORNING"
print(string.lower())
#(or)------>without inbuilt methods
#print(ord("A"))---->#65
for char in string:
    if ord("A") <= ord(char) <= ord("Z"):
        print(chr(ord(char)+32),end ="")'''
################################################################################
#6.	"program to convert lowercase to uppercase characters with and without inbuilt methods."
'''string = "welcome to python"
print(string.upper())
#without using inbuilt methods
for char in string:
    if ord("a") <= ord(char) <= ord(char):
        print(chr(ord(char)-32),end = "")'''
###################################################################################
#7.	"program to swap the case in the given string with and without inbuilt methods
'''string = "hello python"
print(string.swapcase())
#without inbuilt methods
for char in string:
    if ord("A") <= ord(char) <= ord("Z"):
        print(chr(ord(char)+32),end="")
    elif ord("a") <= ord(char) <= ord("z"):
        print(chr(ord(char)-32),end="")'''
########################################################################################3
#8.	program to check if a substring is present in the string or not
'''string = "hello hai goodmorning,hai everyone"
print(string.find("hai"))'''
##########################################################################################
#9.	"program to extract numeric values from the string with and without inbuilt methods"
'''string = "he005llo123hai456"
for char in string:
     if char.isdigit():
         print(char,end = " ")'''
#without using inbuilts methods
'''for char in string:
    if ord("0") <=ord(char) <= ord("9"):
        print(char,end = "")'''
#######################################################################################
#10.program to extract alphabetical values from the string with and without inbuilt methods"
'''string = "hello1236thanu57"
for char in string:
    if char.isalpha():
        print(char,end = "")'''
#without using inbuilt methods
'''for char in string:
    if (ord("a") <= ord(char) <=ord("z")) or(ord("A") <=ord(char) <= ord("Z")):
        print(char,end = "")'''
#######################################################################################
#11.program to extract only special characters from the string with and without inbuilt methods
'''string = 'hello@34%$&'
for char in string:
    if char.isalpha():
        print("")
    elif char.isdigit():
        print("")
    else:
        print(char,end = " ")'''

#####################################################################################
#13.Write a program to check if the given string is Palindrome or not with and without using reversed method.
'''string = "madam"
if string == string[::-1]:
        print("string is a palindrome")
else:
        print("string is not a palindrome")'''
#with using reversed method
'''string = "ata"
string1 = " "
for char in reversed(string):
    if string == char:
        print("palindrome")
    else:
        print("not a palindrome")'''
##################################################################################
#14.Replace "how" to "who" in the string "hi how are you" with and without inbuilt methods
'''string = "hi how are you"
print(string.replace("how","who"))'''
#without in built methods
'''string = "hai how are you"
l = string.split()
print(l)
if l[1] == "how":
    l[1] = "who"
print(l)'''
###################################################################
#15.Replace all the vowels with "*" in the string "hello world"
'''string = "hello world"
for char in string:
    if char in 'aeiouAEIOU':
        char = '*'
    print(char, end ="")'''
###########################################################################
#16.Replace all the characters which occurs more than once with "*" in the string "hello world"
string = "hello world"
i = 0
while(i < len(string)):
    if string[i] == string[i+1]:

print(string)







