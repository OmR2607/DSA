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
