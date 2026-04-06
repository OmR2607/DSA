# Reverse list

# list=input("Enter a list seperated by spaces: ").split()
# print(list)
# print(list[::-1])

# ----------------------------------------------------------------------------------------------------------------------------------------

# Palindrome list

# list1=input("Enter a list seperated by spaces: ").split()
# if(list1 == list1[::-1]):
#     print("The list is palindrome")
# else:
#     print("The list is not palindrome")

# ---------------------------------------------------------------------------------------------------------------------------------------

# Commone element from 2 lists

# a=input("Enter a list A seperated by spaces: ").split()
# b=input("Enter a list B seperated by spaces: ").split()
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Class in Python

# class Student:
#     roll_no = 101
    
#     def studentData(self): #Method/Member Function
#         print("Student Information")

# obj= Student()
# print(obj.roll_no)
# obj.studentData()

class Demo:
    def __init__(self): #Constructor:It will automatically execute when class is called 
        print("I am Constructor")
    def msg(self):
        print("Hello, I am Class")
obj1=Demo()
obj2=Demo()
obj1.msg()
