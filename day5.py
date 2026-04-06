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
# Static Method

# class Student:
#     @staticmethod
#     def get_personal_detail(first_name,last_name):
#         print("\nYour Full Name is: ",first_name," ",last_name)

#     @staticmethod
#     def contact_detail(mob_no,roll_no):
#         print("Your Mobile Number is: ",mob_no)
#         print("Your Roll Number is: ",roll_no,"\n")

# Student.get_personal_detail("Om","Retharekar")
# Student.contact_detail(2828282828,101)

# ---------------------------------------------------------------------------------------------------------------------------------

# Inheritance
'''
Extending property from one class to another class is called inheritance
Directly we are getting here reusability concept
1.Base Class: A class which inherits its property to another is called base class or parent class.
2.Derived Class: A class in which properties are inherited called as derived class or child class.

Types of Inheritance:
1.Single Inheritance
2.Multiple Inheritance
3.Multilevel Inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance
'''

# ---------------------------------------------------------------------------------------------------------------------------------

# # 1.Single level Inheritance
# class College: #Parent Class
#     def college_name(self): 
#         print("Modern College")

# class Student(College): #Child Class
#     def student_name(self): #Member Function
#         print("Student Name: Om Retharekar")
#         print("Branch: Computer Science")

# obj = Student()
# obj.college_name()
# obj.student_name() 

# # ---------------------------------------------------------------------------------------------------------------------------------

# # 2.Multilevel Inheritance
# class College: #Parent Class
#     def college_name(self): 
#         print("\tModern College")

# class Student(College): #Child Class
#     def student_name(self): #Member Function
#         print("Student Name: Om Retharekar")
#         print("Branch: Computer Science")

# class Exam(Student): #Child Class
#     def subjects(self):
#         print("Subject1: Maths")
#         print("Subject2: Physics")
#         print("Subject3: Chemistry")

# obj = Exam()
# obj.college_name()
# obj.student_name()
# obj.subjects() 

# ---------------------------------------------------------------------------------------------------------------------------------

# # 3.Multiple Inheritance
# class SubMarks:
#     math=int(input("Enter Paper Marks of Maths: "))
#     phy=int(input("Enter Paper Marks of Physics: "))
#     chem=int(input("Enter Paper Marks of Chemistry: "))
#     total=math+phy+chem
#     print("Total Marks: ",total)
# # -------------------------------------Parent Class-1-------------------------------------------------
# class PracMarks:
#     cpract = int(input("Enter Practical marks of C language: "))

# # -------------------------------------Parent Class-2-------------------------------------------------
# class Result(SubMarks, PracMarks): #Child Class
#     # If student pass in both subject and practical paper then pass
#     def total(self):
#         if self.math >= 40 and self.phy >= 40 and self.chem >= 40 and self.cpract >= 20:
#             print("Pass")
#         else:
#             print("Fail")

# obj = Result()
# obj.total()

# -------------------------------------------------------------------------------------------------------------------------------------

#Polymorphism
'''
Polymorphism means many forms
1.Method Overloading (Python does not support)
2.Method Overriding  (Python supports)
'''
# class Principal:
#     def role(self):
#         print("I am Principal")

# class Dean:
#     def role(self):
#         print("I am Dean")

# class Hod:
#     def role(self):
#         print("I am Hod")

# class Faculty:
#     def role(self):
#         print("I am Faculty")
# # --------------------------------Class declaration Completed-----------------------------------------------------

# def func(obj):
#     obj.role()                                  #calling function
# campus=[Principal(),Dean(),Hod(),Faculty()]
# for obj in campus:                              #obj=[0:Pricipal(),1:Dean(),2:Hod(),3:Faculty()]
#     func(obj)                                   #obj function

# ---------------------------------------------

## Different number of Parameters
# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

#----------------------------OR--------------------------------------

# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         elif a!=None:
#             print(a)
#         else:
#             print("No arguments")
# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)
# obj.add()

# ------------------------------------------------------------------------------------------------------------------------------------- 

#Method overriding(parent and child relationship must be there)
class Rbi:
    def homeloan_rate(self):
        print("Home Loan Rate: 8%")

class Sbi(Rbi):
    def homeloan_rate(self):        #overriding
        print("Home Loan Rate: 7%") 

class Hdfc(Sbi):
    def homeloan_rate(self):        #overriding
        print("Home Loan Rate: 6%")

obj = Rbi()
obj.homeloan_rate()
obj = Sbi()
obj.homeloan_rate()
obj = Hdfc()
obj.homeloan_rate()
