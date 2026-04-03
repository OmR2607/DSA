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

name="Mumbai"
# WAP to reverse the string using for loop
for i in name[::-1]:
    print(i)


