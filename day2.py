# String defined functions in python

# name = "prashantjha"
# #indexing 0123456789
# print(name[0]) #p
# print(name[1]) #r
# print(name[-1])
# #print(name[15]) #error\
# print(name[0:5]) #prash
# print(name[1:]) #rashantjha
# print(name[:5]) #prash
# print(name[:]) #prashantjha
# print(name[1:8:2]) #rsat
# print(name[::-1]) #ahjtnahsrp

# ------------------------------------------------------------------------------------------------------------------------------

# String built in functions in python

# s = "Python is a High Level programming language"
# print(s.upper())  # PYTHON IS A HIGH LEVEL PROGRAMMING LANGUAGE
# print(s.lower())  # python is a high level programming language
# print(s.swapcase())  # pYTHON IS A hIGH lEVEL PROGRAMMING LANGUAGE
# print(s.capitalize())  # Python is a high level programming language
# print(s.title())  # Python Is A High Level Programming Language

# ------------------------------------------------------------------------------------------------------------------------------

# String formatting in python

# print('Subject Marks :')
# phy = 50
# chem = 60
# math = 70
# print("Physics = {}  Chemistry = {}  Mathematics = {}".format(phy, chem, math))
# print("Physics = {0}  Chemistry = {1}  Mathematics = {2}".format(phy, chem, math))
# print("Physics = {X}  Chemistry = {Y}  Mathematics = {Z}".format(X=phy, Y=chem, Z=math))
# total = phy + chem + math
# print("Total Marks",f"{total}")
# print("Roll No.=","7".zfill(4)) 

# ------------------------------------------------------------------------------------------------------------------------------

# looping 

#for(initialization; condition; increment/decrement) 
# for i in range(5): #0,1,2,3,4
#     print(i)

# for i in range(1, 5): #1,2,3,4
#     print(i)
#     print(i)

# for i in range(1, 11, 2): #1,3,5,7,9
#     print(i)

# for i in range(10, 0, -1): #10,9,8,7,6,5,4,3,2,1
#     print(i)

# for i in range(10,0,-2): #10,8,6,4,2
#     print(i)

# for i in range(1, 11):
    # print(i*2)

# # table of 2,3,4,5,6,7,8,9,10
# for i in range(1, 11):
#     print(i*2, " ", i*3, " ", i*4, " ", i*5, " ", i*6, " ", i*7, " ", i*8, " ", i*9, " ", i*10)

# print("---------------------------------------------------------------------------------------------------------------------")

# # table of 11,12,13,14,15,16,17,18,19,20
# for i in range(1, 11):
#         print(i*11," ", i*12, " ", i*13, " ", i*14, "  ", i*15, "  ", i*16, " ", i*17, " ", i*18, " ", i*19, " ", i*20)

# String looping
# name = "prashantjha"
# for i in name:
#     print(i)

# WAP to remove duplicates 
# newname = ""
# for i in name:
#     if i not in newname:
#         newname = newname + i
# print(newname)

# name="Mumbai"
# rev=""
# # WAP to reverse the string using for loop
# for i in name[::-1]:
#     rev+=i
# print(rev)

# ------------------------------------------------------------------------------------------------------------------------------

# WAP to check for palindrome string using for loop
# name = "Racecar"
# name = name.lower()
# rev = ""
# for i in name[::-1]:
#     rev += i
# if name == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# -------------------------------------------------------------------------------------------------------------------------------

# List operations 

# mylist = ["Prashant", 25, 5.9, "Mumbai", True, [1, 2, 3], (4, 5, 6), {"name": "Prashant", "age": 25}]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[:])
# print(mylist[1:8:2])
# print(mylist[::-1])

# mylist[3]= "Delhi"
# print(mylist)

# if "Mumbai" in mylist:
#     print("Found")
# else:    
#     print("Not Found")

# mylist.append("India")
# mylist.append("Python")
# print(mylist)

# mylist.insert(2, 100)
# print(mylist)

# mylist.remove("Mumbai")
# print(mylist)

# newlist = [["Prashant", "Delhi", 3.00], [ 'Mumbai', 6], [67.34, 89483, 'yyyy']]
# print(newlist)
# print(newlist[0])
# print(newlist[0][1])
# print(newlist[1][1])
# print(newlist[2][2])

# list1 = ["Om","Retharekar"]
# # print(list1*2)
# list2 = ["Prashant", "Jha"]
# print(list1 + list2)

# del list1 
# print(list1) #error
# del list2[0]
# print(list2) 

# list2.clear()
# print(list2)

# name= "Prashant"
# print(name)
# myname = list(name)
# print(myname)
# print(type(myname))

# mylist = [1, 2, 3, 4, 5]
# mylist.reverse()
# print(mylist)

# Sorting a list
# mylist = [5, 2, 9, 1, 5, 6]
# mylist.sort()
# print(mylist)
# We should know that list should contain same type of data to sort it(homogeneous data) 
# otherwise it will give error(heterogeneous data)

# mylist = [5, 2, 9, 1, 5, 6]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0] = 'prashant'
# print(mylist)
# print(newlist)

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11,],
#        [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop()) #4,7,11,15

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i], end=" ") #2,3,4,5,6,6

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50 
# print(a)

# -------------------------------------------------------------------------------------------------------------------------------

# Tuple operations

# mytuple = ("Prashant", 25, 5.9, "Mumbai", True, [1, 2, 3], (4, 5, 6), {"name": "Prashant", "age": 25})
# print(mytuple)
# print(type(mytuple))

# mytuple[2] = 6.0 #error tuple is immutable
# print(mytuple)

# init_tuple = ()
# print(init_tuple.__len__()) #0
# print(type(init_tuple)) #<class 'tuple'>

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(id(init_tuple_a))
# print(id(init_tuple_b))
# print(init_tuple_a == init_tuple_b) 

# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
# print(init_tuple_a + init_tuple_b) #('1', '2', '3', '4')

# init_tuple = (1,) * 3
# init tuple[0] = 2
# print(type(init_tuple)) #<type 'tuple'>
# print(init_tuple)

# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8])) #7

# names = [4,2,5,6,8,2]
# for i in names:
#     print(i)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# move 0s to end of list
# a = [4,0,2,5,0,1]
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(0)
# print(a)

#-----------------------------------------------------------------------------------------------------------------------------------------------
# remove duplicates from a list
# a = [1,2,2,3,4,4,5]
# a1 = []
# for i in a:
#     if i not in a1:
#         a1.append(i)
# print(a1)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# check common elements in 3 lists
# a = [1,2,3]
# b = [2,3,4]
# c = [3,4,5]
# d =[]
# for i in a:
#     if i in b and i in c:
#         d.append(i)
# print(d)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# WAP to find sum of differences of adjacent elements in an array
# a = []
# n = int(input("Enter size of array: "))
# for i in range(n):
#     val = int(input("Enter element: "))
#     a.append(val)
# print("Array is: ",a)
# sum = 0
# for i in range(len(a)-1):
#     b=abs(a[i]-a[i+1])
#     sum += b
# print("Sum of differences is: ",sum)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Break statement in for loop
# for i in range(1,5):
    # if i == 3:
        # break
    # print(i)

# Continue statement in for loop
# for i in range(1,5):
    # if i == 3:
        # continue
    # print(i)

# ----------------------------------------------------------------------------------------------------------------------------------------------

# WAP to print 
# 1 5 
# 2 4
# 4 2
# 5 1

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i," ", 6-i)

# OR

# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i == 3 and j == 3:
#         continue 
#     print(i," ",j)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# WAP to move * to start of string
# name = "prashant*is*a*good*programmer"
# stars = 0
# result = ""

# for i in name:
#     if i == '*':
#         stars += 1
#     else:
#         result += i

# result = '*' * stars + result

# print(result)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# BODMAS rule in python
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d) #160.0
# print((a-b)*(c/d)) #40.0
# print(a+(b*c)/d) #110.0

# -------------------------------------------------------------------------------------------------------------------------------

# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]
# print(id(x))
# print(id(y))
# print(id(z))
# print(x==y) #True
# print(x==z)
# print(x != z) #True

# -------------------------------------------------------------------------------------------------------------------------------

#WAP to check Anagram or not
# str1 = "listen"
# str2 = "silent"
# str1 = sorted(str1)
# str2 = sorted(str2)
# if str1 == str2:
#     print("Anagram")
# else:
#     print("Not Anagram")

# -----------------------------------------------------------------------------------------------------------------------

#WAP to count words in string
# str1="This is a sentence"
# space=1
# for i in str1:
#     if i == " ":
#         space += 1
# print("Total words: " ,space) 

# -----------------------------------------------------------------------------------------------------------------------

# print array with multiplication of other element leaving that particular value

# a=[1,2,3,4]
# for i in range(0,4):
#    for j in range(0,4):
#       if i == j:
#          continue
      
# print(a)
