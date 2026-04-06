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

# class Demo:
#     def __init__(self): #Constructor:It will automatically execute when class is called 
#         print("I am Constructor")
#     def msg(self):
#         print("Hello, I am Class")
# obj1=Demo()
# obj2=Demo()
# obj1.msg()

# class HoD:
#     def __init__(self):
#         self.name='om retharekar'   #2 byte
#         self.age=21                 #3 byte
#         self.empid=1001             #1 byte
#     def info(self):
#         print("My Name is: ",self.name)
#         print("My Age is: ",self.age)
#         print("My Empid is: ",self.empid)
# obj = HoD()
# # obj.info()

# class HoD:
#     def __init__(self,name,age,roll_no):
#         self.name= name                 #2 byte
#         self.age= age                   #3 byte
#         self.empid= roll_no             #1 byte
#     def show(self):
#         print("My Name is: ",self.name)
#         print("My Age is: ",self.age)
#         print("My Empid is: ",self.empid)
# obj = HoD("Arjun",45,101)
# obj.show() 

# class New:
#     def __init__(self):
#         self.a = 10
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a = 20
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# Declaring instance variable outside a class by using Object

# class Student:
#     def __init__(self):
#         self.s_name = "Om"
#         self.s_roll_no = 101 #Declaring a instance variable inside a constructor
#     def getdata(self):
#         self.s_mb = 2828282828 #Declaring a instance variable inside a instance method

# obj = Student()
# obj.getdata()
# del obj.s_mb        #deleting the instance variable using object
# obj.s_branch = "CS" #adding instance variable by using object
# print(obj.__dict__)

# 1 Static Memory is equal to 1 Memory
# class New:
#     a = 20
#     def __init__(self):
#         self.b = 10
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# print()
# New.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# --------------------------------------------------------------------------------------------------------------------------------------

# CRUD operation
# import sys
# class Student: 
#     def __init__(self):
#         print("\nStudent Management System")
#         self.studentID=[]
#         self.studentName=[]
#         self.studentRollNo=[]
#         self.studentCity=[]
#     def add_student(self):
#         self.studentID.append(input("Enter Student_ID: "))
#         self.studentName.append(input("Enter Student Name: "))
#         self.studentRollNo.append(input("Enter Student Roll No: "))
#         self.studentCity.append(input("Enter Student City: "))
#         print("Record Added")

#     def show_students(self):
#         if len(obj.studentID) == 0:
#             print("No Records Found")
#         else:
#             print("Student Records:")
#             print("Student ID\tStudent Name\tStudent Roll No\tStudent City")
#             for i in range(len(obj.studentID)):
#                 print("--------------------------------------------------------------------------------------------------------------------")
#                 print(obj.studentID[i],"\t\t",obj.studentName[i],"\t\t",obj.studentRollNo[i],"\t\t",obj.studentCity[i],"\t\t")
#                 print()

#     def update_student(self):
#         ID=input("Enter Student ID to update: ")
#         if ID in self.studentID:
#             index=self.studentID.index(ID)
#             print("Student Name: ",self.studentName[index])
#             print("Student Roll No: ",self.studentRollNo[index])
#             print("Student City: ",self.studentCity[index])
#             print()
#             print("1.Update Name")
#             print("2.Update Roll No")
#             print("3.Update City")
#             choice=int(input("Enter your choice: "))
#             if choice == 1:
#                 self.studentName[index]=input("Enter new name: ")
#             elif choice == 2:
#                 self.studentRollNo[index]=input("Enter new roll no: ")
#             elif choice == 3:
#                 self.studentCity[index]=input("Enter new city: ")
#             else:
#                 print("Invalid Choice")
#         else:
#             print("Student ID not found")

#     def delete_student(self):
#         ID=input("Enter Student ID to delete: ")
#         if ID in self.studentID:
#             index=self.studentID.index(ID)
#             print("Student Name: ",self.studentName[index])
#             print("Student Roll No: ",self.studentRollNo[index])
#             print("Student City: ",self.studentCity[index])
#             print()
#             print("Do you really want to delete this record?(y/n): ")
#             choice=input("Enter your choice: ")
#             if choice == 'y':
#                 self.studentID.pop(index)
#                 self.studentName.pop(index)
#                 self.studentRollNo.pop(index)
#                 self.studentCity.pop(index)
#                 print("Record Deleted")
#             else:
#                 print("Record not deleted")
#         else:
#             print("Student ID not found")

# obj = Student()

# while(True):
#     print("\n1.Add Student")
#     print("2.Show Student")
#     print("3.Update Student")
#     print("4.Delete Student")
#     print("5.Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         obj.add_student()
#     elif choice == 2:
#         obj.show_students()
#     elif choice == 3:
#         obj.update_student()
#     elif choice == 4:
#         obj.delete_student()
#     elif choice == 5:
#         sys.exit()
#     else:
#         print("Invalid Choice")

# --------------------------------------------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self,name,roll_no,mob):
#         self.name=name
#         self.roll_no=roll_no
#         self.mob=mob
#     def display(self):
#         print(self.name," ",self.roll_no," ",self.mob)
# stud=Student("prashant",1001,22828282)
# stud.display()

# -------------------------------------------------------------------------------------------------------------------------------------

