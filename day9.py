'''
Points                          Recursion                   Iteration

Space efficient?                    No                          Yes             No stack memory require in case of Iteration

Time efficient?                     No                          Yes             In case of recursion system needs more time 
                                                                                for pop and push elements to stack memory 
                                                                                which make recursion less time efficient

Easy to code?                       Yes                         No              We use recursion especially in the cases 
                                                                                we know that a problem can be 
                                                                                divided into similar sub problems

'''
#Fectorial Solution
# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(4))

#Palindrome Solution
# def isPalindrome(string):
#     if len(string) == 0:
#         return True
#     if string[0] != string[-1]:
#         return False
#     return isPalindrome(string[1:-1])

# print(isPalindrome("tacocat"))
# print(isPalindrome("awesome"))
# print(isPalindrome("a"))

#------------------------------------------------------------------------------------------------------------------------------------------------

#Power Solution
# def power(base,exp):
#     if exp==0:
#         return 1
#     return base*power(base,exp-1)

# print(power(2,0))
# print(power(2,2))

#------------------------------------------------------------------------------------------------------------------------------------------------

# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','taco','banana']))

#-----------------------------------------------------------------------------------------------------------------------------------------------

#productOfArray Solution
# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))      #6
# print(productOfArray([1,2,3,10]))   #60

# -----------------------------------------------------------------------------------------------------------------------------------------------

#fibonacci solution

# def fib(num):
#     if(num<2):
#         return num
#     return fib(num-1)+fib(num-2)

# print(fib(4))  #3
# print(fib(10)) #55
# print(fib(1))  #1

# -----------------------------------------------------------------------------------------------------------------------------------------------

#------------------------Tree-----------------------------

# class Tree:
#     def __init__(self,data):
#         self.data = data                        #instance variable
#         self.children = []
    
#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret = "  " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret+=child.__str__(level+1)                 #recursive call
#         return ret


# rootNode=Tree("Drinks")
# hot = Tree("Hot")
# cold = Tree("Cold")
# tea = Tree("Tea")
# coffee = Tree("Coffee")
# nonAlcoholic = Tree("Non-Alcoholic")
# Alcoholic = Tree("Alcoholic")

# #add child nodes in tree
# rootNode.addChild(hot)
# rootNode.addChild(cold)

# hot.addChild(tea)
# hot.addChild(coffee)

# cold.addChild(nonAlcoholic)
# cold.addChild(Alcoholic)

# print(rootNode)

#----------------------------------------------------------------------------------------------------------------------------------

#-----------------Binary tree--------------------------
'''
Perfect Binary Tree
All internal nodes have exactly two nodes
All leaf nodes are at same level
'''
# class Tree:
#     def __init__(self,data):
#         self.data = data                        #instance variable
#         self.children = []
    
#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret = "  " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret+=child.__str__(level+1)                 #recursive call
#         return ret

# rootNode=Tree("N1")
# N2 = Tree("N2")
# N3 = Tree("N3")
# N4 = Tree("N4")
# N5 = Tree("N5")
# N6 = Tree("N6")
# N7 = Tree("N7")
# N9 = Tree("N9")
# N10 = Tree("N10")

# #add child nodes in tree
# rootNode.addChild(N2)
# rootNode.addChild(N3)

# N2.addChild(N4)
# N2.addChild(N5)

# N3.addChild(N6)
# N3.addChild(N7)

# N4.addChild(N9)
# N4.addChild(N10)

# print(rootNode)

#----------------------------------------------------------------------------------------------------------------------------------

#-----------------Binary Tree using Dynamic Values--------------------------

# class Node:
#     #create a node in the tree
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self,value):
#         #insert root node in if there is no root node
#         if self.root == None:
#             self.root = Node(value)
#         else:
#             self.insertNode(self.root, value)
# # class BSTNode:
# #     def __init__(self,data):
# #         self.data = data
# #         self.left = None
# #         self.right = None        

# def inserNode(self,rootNode,value):
#     if value < rootNode,value:                 #70<50
#         #inserting node in the left and right position
#         if rootNode.left is None:
#             rootNode.left = Node(value)
#         else:
#             self.insertNode(rootNode.left,value)    #recursive call

#     else:
#         if rootNode.right is None:
#             round.right = Node(value)   #70
#         else:
