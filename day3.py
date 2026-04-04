'''
Q.How many types of argument we can pass in function
-> 1.Positional Argument
   2.Default Argument
   3.Keyword Argument
   4.Variable number of argument/Variable Length Argument
'''

# Rearrange Positive and Negative Numbers and rearrange them in alternating fashion

# a=[-1,-2,-3,4,5,-6]
# b=[]
# pos=[]
# neg=[]
# for i in range(len(a)):
#     if a[i]>=0:
#         pos.append(a[i])
#     else:
#         neg.append(a[i])
# print(pos)
# print(neg)
# if len(pos)>len(neg):
#     for i in range(len(neg)):
#         b.append(neg[i])
#         b.append(pos[i])
# else:
#     for i in range(len(pos)):
#         b.append(neg[i])
#         b.append(pos[i])
# print(b)

#----------------------------------------------------------------------------------------------------------------------------------------

# Find the majority element,element that appears more than n/2 times in array

# a=[3,3,4,2,4,4,2,4,4,4,4]
# count=0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             count+=1
#     if count>len(a)/2:
#         print(a[i])
#         break
#     else:
#         count=0

# ---------------------------------------------------------------------------------------------------------------------------------------

# dictionary

# mydict = {
#     101:"prashant",
#     102:"ashish",
#     "103":"mohini",
#     "104":"trivani",
#     101:"ashish",
#     104:"ashish"
# }
# print(mydict)

# with the help of key we have to print values
# a=mydict[104]
# print(a)

# we will old value by new value
# mydict[102]="peter"
# print(mydict)

# pop() method to remove pair by specific key name
# mydict.pop(102)
# print(mydict)


# print only keys
# for x in mydict:
    # print(x)

# print only values
# for x in mydict.values():
    # print(x)

# print keys and values
# for x,y in mydict.items():
    # print(x,y)

# to add new key value pair
# mydict["Mobile_no"] = 5472962853
# print(mydict)

# -----------------------------------------------------------------------------------------------------------------------------------------

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5]) #3

# a={'a':1,'b':2,'c':3}
# print(a['a','b']) #error

# arr = {}
# arr[1]=1
# arr['1']=2
# arr[1] +=1
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict) 

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box])) 

# dict = {'c' : 97, 'a':
# 96, 'b':98}
# for _ in sorted(dict):
    # print(dict[_])

# rec = {"Name": "Python", "Age": "20"}
# r = rec.copy()
# print(id(rec) == id(r))

# rec={"Name":"Python","Age":"20","Addr":"NJ","Country":"USA"}
# id1=id(rec)
# del rec
# rec={"Name":"Python","Age":"20","Addr":"NJ"}
# id2=id(rec)
# print(id1==id2)

# --------------------------------------------------------------------------------------------------------------------------------------

# To find the key with the minimum value in a dictionary
# I/P:{"X":20,"Y":10,"Z":30} 
# O/P:Y

# my_dict = {"X":20,"Y":10,"Z":30}
# min = min(my_dict.values())
# for x,y in my_dict.items():
#     if y == min:
#         print(x)
        # break

# ----------------------------------------------------------------------------------------------------------------------------------------

# Pattern Print

# for i in range(1,4):
#     for j in range(1,4):
#         print(i, end=" ")
#     print()

# n= int(input("Enter n: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+i), end=" ")
#     print()

# n = int(input("Enter n: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()

# import time
# n = int(input("Enter n: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(1)
#         print(chr(64+i),end=" ")
#     print()


# import time
# n= int(input("Enter n: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(1)
#         print("*",end=" ")
#     print()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Functions 

# def msg(): #called function
#     print("Hello World!")

# msg() #calling function
# msg()

#WAP to return multiple value
# def arithmatic():
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     add = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     return add, sub, mul, div

# # print(arithmatic()) 
# result = arithmatic()
# print("Arithematic operations:",result)
# print(type(result))

# ----------positional argument---------------
# def login(username,password):
#     if username == password:
#         print("Login successful")
#     else:
#         print("Invalid credentials")

# username = input("Enter username: ")
# password = input("Enter password: ")
# login(username, password)

# ----------keyword argument---------------
# def login(username,password):
#     if username == password:
#         print("Login successful")
#     else:
#         print("Invalid credentials")

# username = input("Enter username: ")
# password = input("Enter password: ")
# login(username="admin", password="admin")

#  -----------------default argument------------------
# def CityName(city="Goa"):
#     print(city)

# CityName("Mumbai")
# CityName("Delhi")
# CityName()

#----------------Variable length argument-------------
# def NameOfCities(*city):
#     print("City names:",city)
# NameOfCities("Goa","Nagpur","Mumbai","Delhi")\

#-------------------------------------------------------------------------------------------------------------------------------------------
#WAP for menu driven code
import sys
def add():
    val1 = int(input("Enter value 1: "))
    val2 = int(input("Enter value 2: "))
    print("Addition: ",val1+val2)

def sub():
    val1 = int(input("Enter value 1: "))
    val2 = int(input("Enter value 2: "))
    print("Subtraction: ",val1-val2)

def mul():
    val1 = int(input("Enter value 1: "))
    val2 = int(input("Enter value 2: "))
    print("Multiplication: ",val1*val2)

def div():
    val1 = int(input("Enter value 1: "))
    val2 = int(input("Enter value 2: "))
    print("Division: ",val1/val2)  

while True:
    print("Menu")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply") 
    print("4.Divide") 
    print("5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice")

