# . functions for string

# print('prashantjha777'.isalnum())   
# print('prashantjha'.isalpha())   
# print('777f'.isdigit())   
# print('sdsdsdsd'.islower())   
# print(''.islower())   
# print('PRASHANTj'.isupper())   
# print('My Name Is prashant'.istitle())   
# print(''.istitle())   
# print(''.isspace())   
# print("Hello".startswith("He"))  
# print("Hello".endswith("lo"))

# ----------------------------------------------------------------------------------------------------------------------------------------

# print("Prashant".find("r"))
# print("Prashant".find("z"))
# print("Prashant".index("r"))
# print("Prashant jha".count("a"))

# --------------------------------------------------------------------------------------------------------------------------------------

# Write a function to check if a key exists in a dictionary

# def check_key(d, key):
#     return key in d

# dict={"name":"Alice","age":30}

# print(check_key(dict, "name"))
# print(check_key(dict, "city"))

# --------------------------------------------------------------------------------------------------------------------------------------

# Count frequency of elements in a list using dictionary
# Sample Input:[1,2,2,3,4,3,5]
# Output:{1:1,2:2,3:2,4:1,5:1}
# list=[1,2,2,3,4,3,5]
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

# --------------------------------------------------------------------------------------------------------------------------------------

# Exception Handling

# n1 = int(input("Enter n1: "))
# n2 = int(input("Enter n2: "))
# try:
#     print(n1/n2)
# except :
#     print("Division by zero is not possible")

# n1 = int(input("Enter n1: "))
# n2 = int(input("Enter n2: "))
# try:
#     print(n1/n2)
# except :
#     print("Division by zero is not possible")


# try:
#     n1 = int(input("Enter n1: "))
#     n2 = int(input("Enter n2: "))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("Division by zero is not possible")
# except ValueError:
#     print("Invalid input")

# try:
#     n1 = int(input("Enter n1: "))
#     n2 = int(input("Enter n2: "))
#     print(n1/n2)
# except (ValueError,ZeroDivisionError) as message:
#     print(message)

# try:
#     n1 = int(input("Enter n1: "))
#     n2 = int(input("Enter n2: "))
#     print(n1/n2)
# except (ValueError,ZeroDivisionError) as message:
#     print(message)
# except:
#     print("Something went wrong")
# else:
#     print("Good")

# Finally Block
# try:
#     n1 = int(input("Enter n1: "))
#     n2 = int(input("Enter n2: "))
#     print(n1/n2)
# except (ValueError,ZeroDivisionError) as message:
#     print(message)
# except:
#     print("Something went wrong")
# finally:
#     print("Finally Done")

# Nested try except block
# try:
#     n1 = int(input("Enter n1: "))
#     n2 = int(input("Enter n2: "))
#     try:
#         print(n1/n2)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)

# try:
#     n1 = int(input("Enter n1: "))
#     n2 = int(input("Enter n2: "))
#     print(n1/n2)
# except(ValueError,ZeroDivisionError) as msg:
#     print(msg)
# except:
#     print("Hello")
# else:
#     print("Good")
# finally:
#     print("Finally Done")

# --------------------------------------------------------------------------------------------------------------------------------------

#WAP to show  count of repeated digits together

# list1 = [5,7,8,3,7,8,9,2,3]
# list2 = []
# for i in range(len(list1)):
#     count=0
#     key=list1[i]
#     j=i+1
#     while j<len(list1):
#         if key == list1[j]:
#             if key not in list2:
#                 list2.append(key)
#         j=j+1
# print(len(list2))

# --------------------------------------------------------------------------------------------------------------------------------------

# WAP to find 2nd Largest element

# list=[7,3,9,2,2,9,8]
# list.sort()
# print(list)
# print(list[-2])

# -------------------------------------------------------------------------------------------------------------------------------------
            
# username = "" 
# password = "" 
# while username!="admin" or password!="admin":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

# name="programming"
# vowels=0
# consonants=0
# for i in name:
#     if i in 'aeiouAEIOU':
#         vowels+=1
#     else:
#         consonants+=1
# print("Vowels: ",vowels)
# print("Consonants: ",consonants)

# --------------------------------------------------------------------------------------------------------------------------------------

# WAP in python to remove all occurence of a element

# list = [1,2,2,3,4,2]
# n = int(input("Enter n: "))
# while n in list:
#     list.remove(n)
# print("List after removal:", list)
       
# --------------------------------------------------------------------------------------------------------------------------------------

# File Handling

# ------Write Mode-------

# f= open("myfile.txt","w")
# print("Name of file: ",f.name)
# print("Mode of file: ",f.mode)
# print("Is file readable: ",f.readable())
# print("Is file writable: ",f.writable())
# print("Is file closed: ",f.closed)
# f.close()
# print("Is file now closed: ",f.closed)

# ------Append Mode--------

# f=open("myfile.txt","a")
# f.write("\n Pune is a smart City")
# f.close()
# print("Operations Done")

# inserting list tuple dictionary

# f=open("myfile.txt","a")
# list = ["\nprashant ","mahesh ","suresh "]
# tuple = ('\nhello ','Om!')
# dict = {"\nName ":"Prashant","Age ":25,"City ":"Mumbai"}
# f.writelines(list)
# f.writelines(tuple)
# f.writelines(dict)
# f.close()
# print("Operations Done")

# ----------Read Mode----------

# f=open("myfile.txt","r")
# print(f.read())
# f.close()

# -----with mode--------

# with open("myfile.txt","w") as f:
#     f.write("Hello\n")
#     f.write("World\n")
#     f.write("Python\n")
#     print("File Closed:",f.closed)
    
# print("File Closed:",f.closed)

# with open("myfile.txt","r") as f:
#     content = f.read()
#     print(content)

# --------------------------------------------------------------------------------------------------------------------------------------

# Reading and writting Binary Data

# f1=open("Pic.png","rb")
# f2=open("Pic1.png","wb")
# data = f1.read()
# f2.write(data)
# print("New Image is available with the name: Pic1.png")

# --------------------------------------------------------------------------------------------------------------------------------------

# Operation with CSV file
# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["Student_ID","Roll_No","Name","Mobile_No"])

# Student_id = input("Enter Student ID: ")
# Roll_no = input("Enter Roll No: ")
# name = input("Enter Name: ")
# Mobile_no = input("Enter Mobile No: ")
# a.writerow([Student_id,Roll_no,name,Mobile_no])
# print("Student Record Added")

# --------------------------------------------------------------------------------------------------------------------------------------\

# WAP to accept "Roll_No","Name","Mobile_No","Maths","Physics",Chemistry","E-mail"
# And then calculate "Total","Percentage","Result"
# -If all subjects have passing marks then result is pass else fail(Passing Marks for each subject is 40)

# import csv
# f = open("Calculate.csv","a",newline="")
# a = csv.writer(f)
# a.writerow(["Roll_No","Name","Mobile_No","E-mail","Maths","Physics","Chemistry","Total","Percentage","Result"])
# Roll_no = input("Enter Roll No: ")
# name = input("Enter Name: ")
# Mobile_no = input("Enter Mobile No: ")
# E_mail = input("Enter E-mail: ")
# Maths = int(input("Enter Maths Marks: "))
# Physics = int(input("Enter Physics Marks: "))
# Chemistry = int(input("Enter Chemistry Marks: "))
# Total = Maths + Physics + Chemistry
# Percentage = (Total/3.0)
# if Maths >= 40 and Physics >= 40 and Chemistry >= 40:
#     Result = "Pass"
# else:
#     Result = "Fail"
# a.writerow([Roll_no,name,Mobile_no,E_mail,Maths,Physics,Chemistry,Total,Percentage,Result])
# print("Student Record Added")
# f.close()
