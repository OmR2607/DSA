# n=int(input("Enter the number of types of product :"))
# k=int(input("Enter the lucky number K :"))
# list=[]
# for i in range(n):
#     item=int(input("Enter price of {}th product :".format(i+1)))
#     list.append(item)
# print(list)

#---------------------------------------------------------------------------------------------------------------------------------

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

#     def insertNode(self,rootNode,value):
#         if value < rootNode.data:                 
#             #inserting node in the left and right position
#             if rootNode.left is None:
#                rootNode.left = Node(value)
#             else:
#                self.insertNode(rootNode.left,value)    #recursive call

#         else:
#             if rootNode.right is None:
#                 rootNode.right = Node(value)   
#             else:
#                 self.insertNode(rootNode.right,value)    #recursive call
        
#     def search(self,value):
#         #search value in the tree
#         return self.searchNode(self.root,value)
        
#     def searchNode(self,rootNode,value):           
#         if rootNode is None:
#             return False
#         if rootNode.data == value:
#             return True
#         if value < rootNode.data:
#             return self.searchNode(rootNode.left,value)
#         else:
#             return self.searchNode(rootNode.right,value)

#     def searchnode(self, rootnode, value):
#         if rootnode is None:
#             return "Value not found"

#         if rootnode.data == value:
#             return "Value found"

#         elif value < rootnode.data:
#             return self.searchnode(rootnode.left, value)

#         else:
#             return self.searchnode(rootnode.right, value)

#     def inorder(self, rootnode):
#         if rootnode is not None:
#             self.inorder(rootnode.left)
#             print(rootnode.data, end=" ")
#             self.inorder(rootnode.right)

#     def preorder(self, rootnode):
#         if rootnode is not None:
#             print(rootnode.data, end=" ")
#             self.preorder(rootnode.left)
#             self.preorder(rootnode.right)

#     def postorder(self, rootnode):
#         if rootnode is not None:
#             self.postorder(rootnode.left)
#             self.postorder(rootnode.right)
#             print(rootnode.data, end=" ")

#     def deletetree(self):
#         self.root = None
#         return "Tree deleted successfully"

# # object creation
# btobj = BinaryTree()
# btobj.insert(70)
# btobj.insert(50)
# btobj.insert(90)
# btobj.insert(30)
# btobj.insert(60)
# btobj.insert(80)
# btobj.insert(100)

# print("Inorder Traversal:")
# btobj.inorder(btobj.root)

# print("\nPreorder Traversal:")
# btobj.preorder(btobj.root)

# print("\nPostorder Traversal:")
# btobj.postorder(btobj.root)

# print("\nSearch 40:", btobj.searchnode(btobj.root, 40))
# print("Search 100:", btobj.searchnode(btobj.root, 100))

# print(btobj.deletetree())

#--------------------------------------------------------------------------------------------------------------------------------

#------------------Binary Search Tree----------------------

# class BSTNode:
#     def __init__(self,data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None

#     def insertNode(self,rootNode,nodeValue):
#         if rootNode.data == None:
#             rootNode.data = nodeValue
#         elif nodeValue < rootNode.data:
#             if rootNode.leftChild is None:
#                 rootNode.leftChild = BSTNode(nodeValue)
#             else:
#                 self.insertNode(rootNode.leftChild, nodeValue)
#         else:
#             if rootNode.rightChild is None:
#                 rootNode.rightChild = BSTNode(nodeValue)
#             else:
#                 self.insertNode(rootNode.rightChild, nodeValue)
#         return "Node inserted successfully"

#     def PreOrderTraversal(self,rootNode):
#         if rootNode is None:
#             return
#         print(rootNode.data,end=" ")
#         self.PreOrderTraversal(rootNode.leftChild)
#         self.PreOrderTraversal(rootNode.rightChild)

#     def InOrderTraversal(self,rootnode):
#         if not rootnode:
#             return
#         self.InOrderTraversal(rootnode.leftChild)
#         print(rootnode.data,end=" ")
#         self.InOrderTraversal(rootnode.rightChild)

#     def PostOrderTraversal(self,rootnode):
#         if not rootnode:
#             return
#         self.PostOrderTraversal(rootnode.leftChild)
#         self.PostOrderTraversal(rootnode.rightChild)
#         print(rootnode.data,end=" ")
#     def levelOrderTraversal(self,rootNode):
#         if rootNode is None:
#             return
#         queue = []
#         queue.append(rootNode)
#         while len(queue) > 0:
#             currentnode = queue.pop(0)
#             print(currentnode.data,end=" ")
#             if currentnode.leftChild is not None:
#                 queue.append(currentnode.leftChild)
#             if currentnode.rightChild is not None:
#                 queue.append(currentnode.rightChild)

# newBST = BSTNode(None)
# newBST.insertNode(newBST,70)
# newBST.insertNode(newBST,50)
# newBST.insertNode(newBST,90)
# newBST.insertNode(newBST,30)
# newBST.insertNode(newBST,60)
# newBST.insertNode(newBST,80)
# newBST.insertNode(newBST,100)
# newBST.insertNode(newBST,20)
# newBST.insertNode(newBST,40)

# print("PreOrder Traversal:")
# newBST.PreOrderTraversal(newBST)

# print("\nInOrder Traversal:")
# newBST.InOrderTraversal(newBST)

# print("\nPostOrder Traversal:")
# newBST.PostOrderTraversal(newBST)

# print("\nLevelOrder Traversal:")
# newBST.levelOrderTraversal(newBST)

#---------------------------------------------------------------------------------------------------------------------------------

#Check Prime numbers in a range

# start=int(input("Enter the start of range :"))
# end=int(input("Enter the end of range :"))
# for i in range(start,end+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,end=" ")
# print()

#---------------------------------------------------------------------------------------------------------------------------------

#calculate compound interest

# principal=float(input("Enter the principal amount : "))
# rate=float(input("Enter the rate of interest : "))
# time=float(input("Enter the time in years : "))

# compound_interest=(principal)*((1+(rate/100))**time)-principal
# print("Compound Interest : ",compound_interest)

#---------------------------------------------------------------------------------------------------------------------------------

