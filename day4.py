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
