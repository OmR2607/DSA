#Sort Dictionary by Key or Value
#I/P: {"B":2,"A":1,"C":3}
#O/P: Ascending Order by key:{"A":1,"B":2,"C":3}
#     Descending Order by Value:{"C":3,"B":2,"A":1}

# Dict = {"B":2,"A":1,"C":3}
# Asc = sorted(Dict.items())
# Des = sorted(Dict.items(),reverse=True)
# Asc = dict(Asc)
# Des = dict(Des)
# print("Ascending Order by key:",Asc)
# print("Descending Order by Value:",Des)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Remove all elements from a Dictionary
#I/P:{"A":1,"B":2,"C":3}
#O/P: {}

# my_dict = {"A":1,"B":2,"C":3}
# my_dict.clear()
# print(my_dict)

# ------------------------------------------------------------------------------------------------------------------------------------------------

#Count the Number of Non-Empty Values in a Dictionary
#I/P: {"A":1,"B":"","C":"3","D":None,"E":"Five"}
#O/P: Number of non empty values: 3

# dict1 = {"A":1,"B":"","C":"3","D":None,"E":"Five"}
# count = 0
# for i in dict1.values():
#     if i:
#         count+=1
# print("Number of non empty values:",count)

# ------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------Queue Implementation----------------------------

# import sys
# class Queue:
#     def __init__(self, queueSize):
#         self.queueList=[]
#         self.queueSize = queueSize

#     def isFull(self):
#         if len(self.queueList) == self.queueSize:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if self.queueList==[]:
#             return True
#         else:
#             return False

#     def Enqueue(self):                #Add Element in Queue from rare
#         if self.isFull():
#             return "Queue is full"
#         else:
#             val=int(input("Enter value for Queue: "))
#             self.queueList.append(val)
#             return "Element pushed"
    
#     def DisplayQueue(self):
#         print("-------------------------------------------")
#         print(self.queueList)
#         print("-------------------------------------------")
#         print()
    
#     def Dequeue(self):                      #Remove Element from Queue from front
#         if self.isEmpty():
#             return "Queue is empty"
#         else:
#             return self.queueList.pop(0)        
    
#     def DeleteQueue(self):
#         choice=input("Are you sure you want to delete Queue (y/n): ").lower()
#         if choice == "y":
#             self.queueList.clear()  
#             return "Queue is deleted" 
#         elif choice == "n":
#             return "Queue is not deleted"
#         else:
#             return "Invalid Choice"
    
#     def PeekQueue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         else:
#             return self.queueList[-1]  
            
# size = int(input("Enter Size of Queue :"))
# queueObj=Queue(size)       #Queue Object is created
# while True:
    
#     print("-----------------------------------------------")
#     print("1. Enqueue Element in Queue ")
#     print("2. Dispaly Queue element ")
#     print("3. Check Queue isEmpty ")
#     print("4. Dequeue Element from Queue ")
#     print("5. Delete Queue ")
#     print("6. Peek ")
#     print("7. Exit")

#     choice =int(input("Enter your choice: "))
#     print()
#     if choice == 1:
#         print(queueObj.Enqueue())
#     elif choice==2:
#         queueObj.DisplayQueue()    
#     elif choice==3:
#         print(queueObj.isEmpty())   
#         print() 
#     elif choice==4:
#         print("Poped element is :",queueObj.Dequeue())   
#         print() 
#     elif choice==5:
#         queueObj.DeleteQueue()  
#         print()
#     elif choice==6:
#         print("The peek element is :",queueObj.PeekQueue()) 
#         print()   
#     elif choice==7:
#         sys.exit()    
#     else:
#         print("Invalid Choice")    
#         print()

#------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------Complexity----------------------------------

'''
Time Complexity
Space Complexity

Big O Notation
O(1)        -   Constant Time       -   Accessing a specific eleement in array      -   Array
O(n)        -   Linear Time         -   Loop through array elements                 -   Array
O(log n)    -   Logarithmic Time    -   Find an element in sorted array             -   Binary Search
O(n^2)      -   Quadratic Time      -   Looking at every index in the array twice   -   Array
O(2^n)      -   Exponential Time    -   Double recursion in Fibonacci               -   Fibonacci
O(n log n)  -   Log-Linear Time     -   Merge Sort                                  -   Merge Sort

O(1) - Constant Time
array = [1,2,3,4,5]
array[0]                            //It takes constant time to access first element

O(n) - Linear Time
array = [1,2,3,4,5]
for element in array:
    print(element))                 //Linear time since it is visiting every element of the array

O(log n) - Logarithmic Time
array = [1,2,3,4,5]
for index in range(0,len(array),3):
    print(array[index])            //Logarithmic time since it is visiting only some elements

O(n^2) - Quadratic Time
array = [1,2,3,4,5]
for x in array:
    for y in array:
        print(x,y)                  //It takes quadratic time to access all elements

O(2^n) - Exponential Time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)       //It takes exponential time to access all elements

------------------------------------------------------------------------------------------------------------------------------------------------

|-----------------------|------------------------------|-----------------------------|
|                       |         Time Complexity      |       Space Complexity      |
|-----------------------|------------------------------|-----------------------------|
|    Create Stack       |              O(1)            |            O(1)             |
|        Push           |          O(1)/O(n^2)         |            O(1)             |
|        Pop            |              O(1)            |            O(1)             |
|       Peek            |              O(1)            |            O(1)             |
|      isEmpty          |              O(1)            |            O(1)             |
|   Delete Entire Stack |              O(1)            |            O(1)             |
|-----------------------|------------------------------|-----------------------------|

DSA is independent of language
There are 2 ways to implement stack:
1. Using Array(List)
    - Easy to implement 
    - Speed problem when it grows
2. Using Linked List
    -Fast Performance
    -Implementation is not easy
'''

#----------------------------------------------------------------------------------------------------------------------------------------------

#WAP to find the biggest number in the array
# def findBiggestNumber(array):
#     index = array[0]                   #----->O(1)
#     for i in range(1,len(array)):      #----->O(n)
#         if array[i] > index:           #----->O(1)
#             index = array[i]           #----->O(1)
#     return index

# array = [2,4,5,6,7,1,9,3,4,5,6]
# print(findBiggestNumber(array))        #----->O(1)

# ----------------------------------------------------------------------------------------------------------------------------------------------

# WAP to check count of special characters and white spaces in given string
#I/P:"gasgg54@#vscsd!s*"
# str = "gasgg54@#vscsd!s*"
# count = 0
# for i in str: 
#     if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9'):
#         continue
#     else       
#         count+=1
# print("Count of special characters and white spaces in given string:",count)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# WAP to check whether the number is square of some number or not
#I/P: 79,77,54,81,48,34,25,16
# import math
# n= int(input("Enter total number of plots:"))
# a = []
# for i in range(n):
#     a.append(int(input("Enter the plot area:")))
# count = 0
# for i in a:
#     if math.sqrt(i) == math.sqrt(i)//1:
#         count+=1
# print("The total square plots are:",count)

# -----------------------------------------------------------------------------------------------------------------------------------------------

#-----------------Linear Search------------------------

# def LinearSearch(array, target):            #----->O(n)
#     for i in range(len(array)):             #----->O(n)
#         if array[i] == target:              #----->O(1)
#             return i+1                      #----->O(1)
#     return -1                               #----->O(1)

# array = [1,2,3,4,5,6,7,8,9]
# print("Array : ",array)
# target = int(input("Enter the target element: "))
# result = LinearSearch(array,target)

# if result == -1:
#     print("Element not found")
# else:
    # print("Element found at index:",result)

#----------------------------------------------------------------------------------------------------------------------------------------------

#-----------------Binary Search------------------------

# def BinarySearch(array,target):
#     start = 0
#     end = len(array)-1
#     while start <= end:
#         mid = (start+end)//2
#         if array[mid] == target:
#             return array[mid]
#         elif array[mid] < target:
#             start = mid+1
#         else:
#             end = mid-1
#     return -1

# sorted_array = [1,2,3,4,5,6,7,8,9]
# print("Array : ",sorted_array)
# target = int(input("Enter the target element: "))
# result = BinarySearch(sorted_array,target)

# -----------------------------------------------------------------------------------------------------------------------------------------------

#-------------------Linked List Data Structure----------------------------

'''
A linked list is a linear data structure where each element(node) contains two parts:head and tail
Data:the valude stored in the node
Next: A pointer/reference to the next node in the sequence.
''' 

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

# linkedlist = LinkedList()
# linkedlist.head = Node(5)
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)

# #Linking Part
# linkedlist.head.next = second
# second.next = third
# third.next = fourth

# print("Linked List:")
# print(linkedlist.head.data)
# print(second.data)
# print(third.data)
# print(fourth.data)

# #Display LinkedList
# while linkedlist.head != None:
#     print("|",linkedlist.head.data,"|",linkedlist.head.next,"| --> ",end=" ")
#     linkedlist.head = linkedlist.head.next

#-------------------------------------------------------------------------------------------------------------------------------------------------
