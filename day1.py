
'''
python is an interpreted programming language
PVM - Python virtual machine --> 
trapit bansal 
python interpreter decides the data type in runtime environment
youtube channel - googleatlife
python has 33 reserved keywords
c has 32 reserved keywords
java has 50 reserved keywords
c++ has 95 reserved keywords
identity operator - is, is not
'''
# ------------------------------------------------------------------------------------------------------------------------------------

# math = 50
# name = "Om"
# pi = 3.14
# result = True

# ------------------------------------------------------------------------------------------------------------------------------------

'''type function is used to find the data type of a variable or value'''
# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))

# -----------------------------------------------------------------------------------------------------------------------------------

'''id function is used to find the memory address of a variable or value'''
# print(id(math))
# print(id(name))
# print(id(pi))
# print(id(result))

# ----------------------------------------------------------------------------------------------------------------------------------

'''to change the type of a variable, we can use type casting functions '''
# print (2+2)
# print ("2"+"2")
# val1 = int(input("Enter value of val1: "))
# val2 = int(input("Enter value of val2: "))
# print (val1 + val2)
# print (int(3.14))
# print (int(10+5j)) -- complex numbers cannot be converted to integers
# print (int(True))
# print (float(False))
# print (int("4.22")) -- string cannot be converted to integer unless it is a valid integer string
# print (int("4"))
# print (int("Om")) -- we cannot convert string name to integer  

# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# # print(complex("Om")) -- we cannot convert string name to complex number unless it is a valid complex number string
# print(complex(5,-3))
# print(complex(True,False))

# print(bool(0))
# print(bool(1))
# print(bool(-1))
# print(bool())
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(True))
# print(bool(False))
# print(bool(" "))
# print(bool("Om"))

# ---------------------------------------------------------------------------------------------------------------------------------

'''In python, if we assign the same value to multiple variables, they will point to the same memory location. 
This is because of the way Python handles memory management and optimizes memory usage.'''
# math = 50
# chem = 50
# print(id(math))
# print(id(chem))

# ----------------------------------------------------------------------------------------------------------------------------------

# list = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# for i in list:
#         for j in list:
#                 if i == j:
#                         sum = sum + list[i][j]
# print(sum)

# ----------------------------------------------------------------------------------------------------------------------------------

#Swapping of two numbers using a temporary variable 
# val1 = int(input("Enter value of val1: "))
# val2 = int(input("Enter value of val2: "))
# print("Before swapping: ", val1, val2)
# temp = val1
# val1 = val2
# val2 = temp
# print("After swapping: ", val1, val2)

#Swapping of two numbers without using a temporary variable
# val1 = int(input("Enter value of val1: "))
# val2 = int(input("Enter value of val2: "))
# val1 = val1 + val2
# val2 = val1 - val2
# val1 = val1 - val2
# print("After swapping: ", val1, val2)

# ------------------------------------------------------------------------------------------------------------------------------------

# WAP to accept phy,chem and math subject marks and calculate total and percentage and if percentage is greater or equal to 60 
# and gender is equal to male so he is eligible for placement else eligible for data entry job.
phy = int(input("Enter value of physics: "))
chem = int(input("Enter value of chemistry: "))
math = int(input("Enter value of mathematics: "))
total = phy + chem + math
percentage = (total/3.0)
print("Total marks: ", total)
print("Percentage: ", percentage,"%")
gender = input("Enter your gender(M/F): ")
gender = gender.upper()
if (percentage >= 60) and (gender == "M"):
    print("Eligible for placement")
else:
    print("Eligible for data entry job")


# ------------------------------------------------------------------------------------------------------------------------------------

# Write a program to calculate the simple interest.
# p_amount = int(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = int(input("Enter the duration in years: "))
# simple_interest = (p_amount * rate * time) / 100
# print("Simple Interest: Rs.",simple_interest)

# ------------------------------------------------------------------------------------------------------------------------------------

# write a program to enter height of user in feet and convert it to inch and centimeter 
# height_feet = int(input("Enter your height in feet: "))
# height_inch = height_feet * 12
# height_cm = height_inch * 2.54
# print("Height in inches: ", height_inch)
# print("Height in centimeters: ", height_cm)

# ------------------------------------------------------------------------------------------------------------------------------------

#reverse a number
# num = 12345
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = (reverse * 10) + digit
#     num = num // 10
# print("Reversed No.: ", reverse)  

# ------------------------------------------------------------------------------------------------------------------------------------

#identity operator - is, is not
# a = 10
# b = 10
# print ( a is b) #True
# print ( a is not b) #False

#membership operator - in, not in
# name = "Om"
# print("O" in name) 
# print("o" in name) 

# -------------------------------------------------------------------------------------------------------------------------------------

# wap to accept any one no. and check positive, negative or zero
# no = int(input("Enter a number: "))
# if no > 0:
#     print("Positive number")
# if no < 0:
#     print("Negative number")
# if no == 0:
#     print("Number is zero")

# -------------------------------------------------------------------------------------------------------------------------------------

# WAP to accept 5 numbers and find the largest number among them
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))
# num5 = int(input("Enter number 5: "))

# if (num1 > num2) and (num1 > num3) and (num1 > num4) and (num1 > num5):
#     print("Largest number is: ", num1)
# if (num2 > num1) and (num2 > num3) and (num2 > num4) and (num2 > num5):
#     print("Largest number is: ", num2)
# if (num3 > num1) and (num3 > num2) and (num3 > num4) and (num3 > num5):
#     print("Largest number is: ", num3)
# if (num4 > num1) and (num4 > num2) and (num4 > num3) and (num4 > num5):
#     print("Largest number is: ", num4)
# if (num5 > num1) and (num5 > num2) and (num5 > num3) and (num5 > num4):
#     print("Largest number is: ", num5)

# -------------------------------------------------------------------------------------------------------------------------------------

# WAP to check username and password are same or not. 
# If same, print "Login successful", else print "Invalid credentials"
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if (username == password):
#     print("Login successful")
# else:
#     print("Invalid credentials")

# -------------------------------------------------------------------------------------------------------------------------------------
