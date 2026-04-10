#WAP to calculate highest sales of a company in M days of N products
'''
I/P: M=3 N=4
        100 198 333 323
        122 232 221 111
        223 565 245 764
'''
#O/P: 333 232 764

# m = int(input("Enter number of days: "))
# n = int(input("Enter number of products: "))

# matrix = []

# for i in range(m):
#     print("Enter elements for row", i + 1)
#     row = []

#     for j in range(n):
#         value = int(input(f"Enter element at position [{i}][{j}]: "))
#         row.append(value)
#     matrix.append(row)

# print("\nMatrix:")
# for row in matrix:
#     print(row)

# print("\nHighest sales:")

# for row in matrix:
#     print(max(row),end=" ")

#-------------------------------------------------------------------------------------------------------------------------------

#-------------------Menu Driven Linked List-------------------------

# import sys
# class Node:
#     def __init__(self,data):
#         self.data = data  #instance variable
#         self.next = None

# class LinkedList:
#         def __init__(self):
#                 self.head = None
#                 self.tail = None

#         #Add Node in Single LinkedList
#         def addNode(self,value):
#                 node = Node(value)  #Create new memory
#                 if self.head is None:
#                         self.head = node
#                         self.tail = node
#                 else:
#                         self.tail.next = node
#                         self.tail = node
        
#         #Add Node in Beginning
#         def addNodeInBeginning(self,value):
#                 node = Node(value)
#                 if self.head is None:
#                         self.head = node
#                         self.tail = node
#                 else:
#                         node.next = self.head
#                         self.head = node
        
#         #Add Node in End
#         def addNodeInEnd(self,value):
#                 node = Node(value)
#                 if self.head is None:
#                         self.head = node
#                         self.tail = node
#                 else:
#                         self.tail.next = node
#                         self.tail = node

#         #Add Node in Between
#         def addNodeInBetween(self,value,index):
#                 node = Node(value)
#                 if self.head is None:
#                         self.head = node
#                         self.tail = node
#                 elif index == 0:
#                         node.next = self.head
#                         self.head = node
#                 else:
#                         temp = self.head
#                         for i in range(index-1):
#                                 if temp.next is None:
#                                         print("Index out of bound")
#                                         return
#                                 else: 
#                                         temp=temp.next
#                         node.next = temp.next
#                         temp.next = node
                

#         def displayLinkedList(self):
#                 temp = self.head
#                 while temp is not None:
#                         print(temp.data,end=" -> ")
#                         temp = temp.next
#                 print()

#         def deleteNode(self,index):
#                 if self.head is None:
#                         print("Linked List is empty")
#                 elif index == 0:
#                         self.head = self.head.next
#                 else:
#                         temp = self.head
#                         for i in range(index-1):
#                                 if temp.next is None:
#                                         print("Index out of bound")
#                                         return
#                                 else: 
#                                         temp=temp.next
#                         temp.next = temp.next.next


# if __name__ == "__main__":
#     object = LinkedList()
#     while True:
#         print()
#         print("--------------------------------")
#         print("1. Add Node LinkedList")
#         print("2. Add Node in Beginning")
#         print("3. Add Node in Between")
#         print("4. Add Node in End")
#         print("5. Display LinkedList")
#         print("6. Delete Node in LinkedList")
#         print("7. Exit")
#         print()
#         choice = int(input("Enter your choice: "))
#         if choice == 1:
#             value = int(input("Enter the value for node: "))
#             object.addNode(value)
#             print("Node added successfully in single LinkedList")
#         elif choice == 2:
#             value = int(input("Enter the value for node: "))
#             object.addNodeInBeginning(value)
#             print("Node added successfully")
#         elif choice == 3:
#             data = int(input("Enter the data: "))
#             index = int(input("Enter the index(start from 0): "))
#             object.addNodeInBetween(data,index)
#             print("Node added successfully")
#         elif choice == 4:
#             data = int(input("Enter the data: "))
#             object.addNodeInEnd(data)
#             print("Node added successfully")
#         elif choice == 5:
#             object.displayLinkedList()
#         elif choice == 6:
#             index = int(input("Enter the index(start from 0) to be deleted: "))
#             object.deleteNode(index)
#             print("Node deleted successfully")
#         elif choice == 7:
#             sys.exit()
#         else:
#             print("Invalid choice")

# --------------------------------------------------------------------------------------------------------------------------------

#Remove leading zeros from a list of integers
#I/P: [0,0,0,1,2,0,3,0,0,4,5]
#O/P: [1,2,0,3,0,0,4,5]

# a = [0,0,0,1,2,0,3,0,0,4,5]
# i=0
# while i<len(a):
#     if a[i]==0:
#         a.pop(i)
#     else:
#         break
# print(a)

#-------------------------------------------------------------------------------------------------------------------------------

#-----------------Regular Expression(RegEx)----------------------

'''
Regular expressions:
it is used to develop the digital circuit 
used to develop the compiler and interpreter
used to develop the communication protocol like TCP/IP etc.
used to develop validation logic
used to develop the pattern matching and searching application like ctrl + f 
the engine is written in C-Language
this engine execute and write the re module 

Compile() Function
this function available inside re module and this function used to compile the pattern into regular expression object and which have various methods , 
which execute various operation like
'''
# import re                               #import re module for performing all the regular expression based
# count = 0                               #to count the number of matching found
# pattern = re.compile("function")        #string converts into bytecode
# #print(pattern)
# matcher = pattern.finditer("A function in python is defined by a def keyword but function is not a built in function")
# # print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),".....",i.end(),"--->",i.group())
# print("The number of occurence of function in string is :",count)


#--------------------------------------------------------------------------------------------------------------------------------

# import re    
# count=0   
# matcher=re.finditer("Hi","HiHiHiHi")  
# # print(matcher)  
# for i in matcher:# loop 4 times execute  
#     count+=1   
#     print(i.start(),"...",i.end(),"--->",i.group())  
# print("The number of occurrences: ",count) 

#---------------------------------------------------------------------------------------------------------------------------------

# import re 
# obj = input("Enter any charater :")
# objmatch=re.finditer(obj,"Hello World , W@r III")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),".....",match.end(),"--->",match.group())

#---------------------------------------------------------------------------------------------------------------------------------

#match() function operation -->It always matches the start of the string
# import re 
# a = input("Enter string to perform match operation :")
# m = re.match(a,"Python is very import language")
# print(m)
# if m != None:
#         print("Match found at beginning level")
#         print(m.start(), "...", m.end())
# else:
#         print("Match not found at beginning level")

# ---------------------------------------------------------------------------------------------------------------------------------

#fullmatch() function operation -->It always matches complete string
# import re 
# a = input("Enter string to perform fullmatch operation :")
# m = re.fullmatch(a,"Python")
# print(m)
# if m != None:
#         print("Match found at end level")
#         print(m.start(), "...", m.end())
# else:
#         print("Match not found at end level")

#--------------------------------------------------------------------------------------------------------------------------------

#search() function operation -->If the match found anywhere in the string then it return object else it will return None
# import re 
# a = input("Enter string to perform search operation :")
# m = re.search(a,"Python is very import language")
# print(m)
# if m != None:
#         print(m.start(), "...", m.end())
# else:
#         print("There sis no matching anywhere")

#Search from file
# import re
# a = a = input("Enter string to perform search operation :")
# f = open("myfile.txt","r")
# c = f.read()
# m = re.search(a,c)
# print(m)
# if m != None:
#         print(m.start(), "...", m.end())
# else:
#         print("There is no matching anywhere")

#--------------------------------------------------------------------------------------------------------------------------------

#findall() function --> This funtion return a list which containing all matches

# import re
# a = re.findall('[^0-9]',"aacbif284hff0") #^ act as not symbol, i.e. here elements other than 0-9 will be printed
# print(a)

#-------------------------------------------------------------------------------------------------------------------------------

#sub() function
# import re
# a = re.sub("Om","prashant","Hey Bro I am Om and Om is my name")
# print(a)

#-------------------------------------------------------------------------------------------------------------------------------

'''subn subn()- It is as similiar as sub() function only one thing is different that it also return number of replacement. 
This return in tuple where first element is string and second one is number of replacement 
'''
# import re
# obj = re.subn("Om","prashant","Hey Bro I am Om and Om is my name")
# print(obj)
# print("The string is :",obj[0])
# print("The number of replacement is :",obj[1])

#--------------------------------------------------------------------------------------------------------------------------------

#WAP to check the valid mobile number
# A mobile number is valid if it is of length 10 and starts with 6,7,8,9
# import re
# mo = input("Enter mobile number :")
# obj = re.fullmatch("[0-5]\d{9}",mo)
# if obj != None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")

#-------------------------------------------------------------------------------------------------------------------------------

#WAP to check valid email id
# import re
# email = input("Enter email id :")
# obj1 = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",email)
# obj2 = re.fullmatch("\w[a-zA-Z0-9_.]*@ybit[.]ac[.]in",email)
# if obj1 != None or obj2 != None:
#     print("Valid email id")
# else:
#     print("Invalid email id")

#--------------------------------------------------------------------------------------------------------------------------------

# import os,sys
# fname=input("Enter file Name: ")
# if os.path.isfile(fname):
#     print("File Exists")
#     f=open(fname,"r")
# else:
#     print("File Not Exists")
#     sys.exit()
# data=f.read()
# print(data)
# f.close()

#--------------------------------------------------------------------------------------------------------------------------------