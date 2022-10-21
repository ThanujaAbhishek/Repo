#swap 1st and last element
# l1 = [1,2,3,4]
# l1[0], l1[-1] =l1[-1],l1[0]
# print(l1)
#
# #(or)
# temp = l1[0]
# l1[0] = l1[-1]
# l1[-1] = temp
#list.append(l1,11)
################################################################################
#pqscal case- all 1st letter of word will be captal to name class name
#class name should not have _(underscore)
'''l2 = [1,2,3,4]

class ListExtension:
    def swap(self,list_):  #swap is a method inside class
        temp = list_[0]
        list_[0] = list_[-1]
        list_[-1] = temp
        return list_'''
#self- parameter is used to hold the abject addres(l) which is calling swap method
#creating  an instance - 0f ListExtension class
#l = ListExtension() #() execution
#using instance
#print(l.swap(l2))
#class name
#print(ListExtension.swap(l,l2))'''
##############################################################################
#accessed class variable
'''class Demo:
    #class variable
    a = 10
    b = 20
#using instance
d = Demo()
print(d.a)

#using classname
print(Demo.a) #variables are directily associated with class'''
#####################################################################################
#modify class variable
class Demo:
    #class variable
    a = 10
    b = 20

d =Demo()

#modify class variable through instance
# print(d.a)  #10
# print(Demo.a)
# d.a = 100
# print(d.a)  #100
# print(Demo.a) #modification done through instances(d) never reflect to class  #10

#modifying using class variable using classname
print(d.b)
print(Demo.b)
Demo.b = 50
print(d.b)
print(Demo.b)
