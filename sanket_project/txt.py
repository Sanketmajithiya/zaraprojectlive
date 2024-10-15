# char1 = "12345"
# e = int(char1)
# print(type(e))
# print(e)


# char2 = "12345"
# e = int(char1)
# print(type(e))
# print(e)

# # mylist =



# a = input("insert value of a")
# b = input("insert value of b")


# a = int(a)
# a = int(b)
# # print(a+b)
# # print(type(a))

# # print("hello world ")

# ---------#------------------#-------------->  
# FOR LOOP
# str1 = "sanket"

# for element in str1:
#     print(element,end=" ") 
    
# ---------#------------------#-------------->    
# FOREACH LOOP
# mylist = [1,2,3,4,5,6,7,8,9,10]

# for number in range(15,51,3):
#     print(number,end=" ")
    
# for index in range(0,n):
#     print(mylist[index],end=" ")    
    
    
# ---------#------------------#-------------->      



# from copy import deepcopy 
# tup1 = deepcopy(tuple)
# tup2 = deepcopy(tup1)
# print(tup2)

# print(id(tup1))
# print(id(tup2))


# IMPORTANT******---------#------------------#----------> 

# tup1 = (2)   
# print(type(tup1)) # out: this is int not tuple 


# tup1 = (2,)
# print(type(tup1)) # out put: <class 'tuple'>

# ---------#------------------#--------------> 
 # set always store in a sorted formate 
 # eachand every Elemt by unique element (one time hi lega)
 # set always remove duplicate elment 
 
 
# mylist = [5,1,2,3,4,5,6,7,8,"a","a","ba"]

# myset = set(mylist)

# print(myset)

# print(mylist)
# myset.clear()
# myset.pop()



# ---------#------------------#--------------> 

# dict 
# key ---->   (immutable) sirf chalegi and unique honi 
# value ---->  any data type 


# mykey = [1,2,3,4,5,6]
mykey = [1,2] # Ager 2 key dunga to woh error nahi dega mujhe Tab  
myval = (100,200,300,400)

keyvalzip = zip(mykey,myval)
keyvalzip = list(keyvalzip)

print(keyvalzip)