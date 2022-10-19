#genarate a function to generate a square and cube of a number
'''l = [1,2,3,4]
def func(a):
    for i in a:
        yield i**2
        yield i**3
print(list(func(l)))'''
####################################################################
#1.generate square number of given list
'''l = [2,4,5]
def func(a):
    for ele in a:
        yield ele **2
print(list(func(l)))'''
     #(or) genarator expression
'''res = ((ele**2)for ele in l )
print(tuple(res))'''
################################################################################
#2. generate a tuple of only numeric values in  the given list
'''items = ["flipkart",2021,"gmail",1.2,[1,2,3],2+3j,True]
def func(items):
    for i in items:
        if isinstance(i,(int,float,complex)):
            yield i
print(tuple(func(items)))

res = (i for i in items if isinstance(i,(int,float,complex)))
print(tuple(res))'''
###################################################################################
#3. generate only the string with odd length in the given list
'''names = ["bob","steve","alex","maya","john"]
def odd_string(names):
    for i in names:
        if len(i) % 2 != 0:
            yield i
print(tuple(odd_string(names)))

#generator expression
res = (i for i in names if len(i)%2 != 0)
print(list(res))'''
####################################################################################
#4. generate a list if individual data type reverse it else keep it as it is
'''items = ["flipkart",2021,"gmail",1.2,[1,2,3],2+3j,True]
def reverse_list(items):
    for i in items:
        if isinstance(i,(int,float,complex,bool)):
            res = str(i)[::-1]
            yield res
print(list(reverse_list(items)))'''
####################################################################################
#5.generate a pi values with increasing decimal number up to user defined number
'''import math
pI = math.pi
print(pI)

def func(num):
    for i in range(num):
        yield round(pI,i)
print(list(func(3)))
 #generator expression
res = (round(pI,i) for i in range(6))
print(list(res))'''
##########################################################################################
#6.a function takes variable number of positional