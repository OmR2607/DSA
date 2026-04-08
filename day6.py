#WAP to compress a string by replacing consecutive characters with their counts
#input = "aaabbbcccc"
#output = "a3b3c4"
# s = "aaabbbcccc"
# a = ""
# for i in s:
#     if i not in a:
#         a += i
#         a += str(s.count(i))
# print(s)
# print(a)

#----------------------------------------------------------------------------------------------------------------------------------------------

#WAP to reverse each word in a string

# s = "Hello World"
# a = s.split()
# print (a)
# b = ""
# for i in a:
#     b += i[::-1] + " "
# print(s)
# print(b)

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Abstraction

'''
A class which contains one or more abstract methods is called an abstract class.
An abstract method is a method that has a declaration but does not have an implementation.

'''

# from abc import ABC, abstractmethod  
# class Help4code(ABC): # abstract class  
#     @abstractmethod # decorator  
#     def training(self):# abstract method  
#         pass  
       
#     @abstractmethod   # abstract method  
#     def placement(self):  
#         pass  
  
# class Ashish(Help4code):  
#     def training(self):  
#         print('C , C++ , Java')  
#     def placement(self):  
#         print("Java placement")  
  
# class Ankush(Help4code):  
#     def training(self):  
#         print("Python | Django")  
#     def placement(self):  
#         print("Python placement students")  
  
# class Prashant(Help4code):  
#     def training(self):  
#         print("Machine learning")  
#     def placement(self):  
#         print("Data science placement")  
  
# obj1 = Ashish()  
# obj1.training()  
# obj1.placement()  
  
# obj2 = Ankush()  
# obj2.training()  
# obj2.placement()  
  
# obj3 = Prashant()  
# obj3.training()  
# obj3.placement()  

#------------------------------------------------------------------------------------------------------------------------------------------------- 

# from abc import ABC, abstractmethod   
# class Irctc(ABC):#abstract class  
  
#     @abstractmethod  
#     def bookTicket(self): # abstract method  
#         pass   
  
# class MakeMyTrip(Irctc):  
  
#     def bookTicket(self):  
#         print( "  ==========================================")  
#         print("    Welcome To makemytrip   ")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
#         print( "  ==========================================")  
          
# class GoIbibo(Irctc):  
      
#     def bookTicket(self):  
#         print("    Welcome To GOIBIBO")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
  
# class Yatra(Irctc):  
      
#     def bookTicket(self):  
#         print("    Welcome To Yatra  ")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
  
# m = MakeMyTrip()  
# m.bookTicket()  
# g = GoIbibo()  
# g.bookTicket()  
# y = Yatra()  
# y.bookTicket()  

# ---------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------Encapsulation-------------------------
# class Base: #parent class
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "Prashant" #public data member
#         self.__c = "Ashish" #private member

# #cretaing a dervied class/child class
# class Derived(Base): #Child Class
#     def __init__(self):
#         #calling Constructor of Base class
#         Base.__init__(self) 
#         #print("Calling private member of base class: ")
#         # print(self.a)
#         # print(self.__c)

# obj1=Derived()
# print(obj1.a)
# # print(obj1.__c)
# obj2 = Base()
# print(obj2.a)
# print(obj2.__c)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# class Rbi:
#     #Declaring public method
#     def publicPolicy(self):
#         print("Check the public policy of RBI")
    
#     #Declaring private method
#     def _protectedPolicy(self):
#         print("There is some private policy which is not accessible for public")
    
# class Sbi(Rbi):
#     def __init__(self):                 #first sbi class constructor called
#         Rbi.__init__(self)              #Second parent class constructor called

#     def callingPublicMethod(self):      #Child Class public method
#         print("\nInside child class")
#         self.publicPolicy()             #calling parent class public method
    
#     def callingPrivateMethod(self):     #child class public method
#         self.__privatePolicy()          #calling parent class private method

# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod() #calling private method will give error
# obj1.publicPolicy() #calling parent class public method
# obj1.__privatePolicy() #calling parent class private method will give error
# obj2 = Rbi()
# obj2.publicPolicy() #calling parent class public method
# obj2.__privatePolicy() #calling parent class private method will give error
# obj2 = Rbi()
# obj2.publicPolicy() #calling parent class public method
# obj2._Rbi_privatePolicy() #calling parent class private method using name mangling

# -----------------------------------------------------------------------------------------------------------------------------------------

# WIPRO Problem

# n=int(input("Enter the length of list: "))
# list=[]
# odd=[]
# even=[]
# for i in range(n):
#     list.append(int(input(f"Enter the element {i+1}: ")))
# print(list) 
# for i in range(n):
#     if list[i]%2==0:
#         even.append(list[i])
#     else:
#         odd.append(list[i])
# print("Odd list: ",odd)
# print("Even list: ",even)
# print(even+odd)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# -----------------Data Structurs and Algorithm-----------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------Stack Implementation without Stack Limit-------------------------------

# import sys

# class Stack:
#     def __init__(self):
#         self.stackList = [] 

#     def push(self, value):
#         self.stackList.append(value)
    
#     def isEmpty(self):
#         if self.stackList == []:
#             True
#         else:
#             False 
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         else:
#             return self.stackList.pop()
    
#     def display(self):
#         print("---------------------------")
#         print(self.stackList)
#         print("---------------------------")

#     def isEmpty(self):
#         if self.stackList == []:
#             True
#         else:
#             False

#     def deleteStack(self):
#         self.stackList = None    
    
#     def peak(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         else:
#             return self.stackList[-1]

# obj = Stack()

# while(True):
#     print("-----------------------------------------------")
#     print("1.Push Element in Stack\n2.Pop Element from Stack\n3.Display Elements in Stack")
#     print("4.Check if Stack is Empty\n5.Delete Stack\n6.Peak Stack\n7.Exit")
#     if obj.isEmpty():
#         print("Stack is Empty")
#     choice=int(input("Enter your choice :"))
#     if choice==1:
#         val = int(input("Enter Element: "))
#         obj.push(val)
#         print("Element ",val,"is pushed into stack")
#     elif choice==2:
#         print(obj.pop(),"Popped from stack")
#     elif choice==3:
#         obj.display()
#     elif choice==4:
#         if obj.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("Stack is not Empty")
#     elif choice==5:
#         obj.deleteStack()
#         print(obj.deleteStack())
#     elif choice==6:
#         sys.exit()
#         break
#     else:
#         print("Invalid Choice")

# ---------------------------------------------------------------------------------------------------------------------------------------

# ------------------------Stack Implementation with stack limit-------------------------------

# import sys
# class Stack:
#     def __init__(self, stacksize):
#         self.stacklist=[]
#         self.stackSize = stacksize

#     def isFull(self):
#         if len(self.stacklist)==self.stackSize:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if self.stacklist==[]:
#             return True
#         else:
#             return False

#     def push(self,value):
#         if self.isFull():
#             return "stack is full"
#         else:
#             self.stacklist.append(value)
#             return "Element pushed"
    
#     def displaystack(self):
#         print("-------------------------------------------")
#         print(self.stacklist)
#         print("-------------------------------------------")
#         print()
    
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist.pop()        
    
#     def deletestack(self):
#         self.stacklist=None  
#         return "Stack is deleted" 
    
#     def peekstack(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist[-1]  
            
# size = int(input("Enter Size of Stack :"))
# stackobj=Stack(size)
# while True:
    
#     print("-----------------------------------------------")
#     print("1. Push")
#     print("2. Dispaly Stack element")
#     print("3. Check is empty")
#     print("4.Pop")
#     print("5.Delete stack")
#     print("6.Peek")
#     print("7.Exit")

#     choice =int(input("Enter your choice: "))
#     print()
#     if choice == 1:
#         val=int(input("Enter value for stack "))
#         stackobj.push(val)
#     elif choice==2:
#         stackobj.displaystack()    
#     elif choice==3:
#         print(stackobj.isEmpty())   
#         print() 
#     elif choice==4:
#         print("Poped element is :",stackobj.pop())   
#         print() 
#     elif choice==5:
#         stackobj.deletestack()  
#     elif choice==6:
#         print("The peek element is :",stackobj.peekstack()) 
#         print()   
#     elif choice==7:
#         sys.exit()    
#     else:
#         print("Enter Right Choice")    
#         print()

# ------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------Problem of Hanoi---------------------------

'''
Rule:
    1.We can move only one disk at a time.
    2.We have to pick upper disk from any one pipe.
    3.We have to place on top of any disk.
    4.We can not place any large disk on top of smaller disk.
'''
#WAP for Tower of Hanoi

import time

class Tower:
    def _init_(self):
        print("Welcome to tower of hanoi game")
        print()
        print("Given Problem A=[3,2,1]  B=[]  C=[]")
        print()
        print("Expected Output A=[]  B=[]  c=[3,2,1]")
        self.A = []
        self.B = []
        self.C = []
        
    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")
        
    def pass1(self):
        self.temp =  self.A.pop(2)  #A=[3,2]
        self.C.append(self.temp)    #C=[1]  => temp=1
        time.sleep(3)
        print("A=",self.A)
        print("Pass One Completed=================\n")
        
    def pass2(self):
        self.temp =  self.A.pop(1)  #A=[3,2]
        self.B.append(self.temp)    #C=[1]  => temp=1
        time.sleep(3)
        print("A=",self.A      ,"   ",     "B=",self.b   ,"    ","C=",self.C)
        print("Pass Two Completed=================\n")
        
        
    def pass3(self):
        self.temp =  self.C.pop(0)  #C=[]
        self.B.append(self.temp)    #B=[2,1]  
        time.sleep(3)
        print("A=",self.A      ,"   ",     "B=",self.b   ,"    ","C=",self.C)
        print("Pass Three Completed=================\n")

    def pass4(self):
        self.temp =  self.A.pop(0) 
        self.C.append(self.temp)    
        time.sleep(3)
        print("A=",self.A      ,"   ",     "B=",self.b   ,"    ","C=",self.C)
        print("Pass Four Completed=================\n")

    def pass5(self):
        self.temp =  self.B.pop(0) 
        self.A.append(self.temp)    
        time.sleep(3)
        print("A=",self.A      ,"   ",     "B=",self.b   ,"    ","C=",self.C)
        print("Pass Five Completed=================\n")

    def pass6(self):
        self.temp =  self.B.pop(0) 
        self.A.append(self.temp)    
        time.sleep(3)
        print("A=",self.A      ,"   ",     "B=",self.b   ,"    ","C=",self.C)
        print("Pass Six Completed=================\n")

    def pass7(self):
        self.temp =  self.C.pop(0) 
        self.A.append(self.temp)    
        time.sleep(3)
        print("A=",self.A      ,"   ",     "B=",self.b   ,"    ","C=",self.C)
        print("Pass Seven Completed=================\n")

towerobj = Tower()
towerobj.tower(3)
towerobj.tower(2)
towerobj.tower(1)
towerobj.pass1()
towerobj.pass2()
towerobj.pass3()
towerobj.pass4()
towerobj.pass5()
towerobj.pass6()
towerobj.pass7()
