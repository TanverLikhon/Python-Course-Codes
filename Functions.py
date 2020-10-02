#making user defined function

def add(x,y):
    sum=x+y
    print(sum)

add(10,20)

def message():
    print("Hello World")

message()
#Python return statement
'''
A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned.

Note: Return statement can not be used outside the function.
def fun():
    statements
    .
    .
    return [expression]

'''
def sum(a,b):
    return a+b

print(sum(1,6))

def is_true(a):
    return bool(a)
print(is_true(0))
print(is_true(5))
print(is_true(2<5))

def reverse_str(value):
    if type(value)==list or type(value)==str:
      reverse=value[::-1]
      return reverse
    else:
        return value
s="TanverLikhon"

result=reverse_str(s)
print(result)

l=[1,2,3,4,5]

result=reverse_str(l)
print(result)



#Zip functions
roll =[1702027,1702028,1702065]
name=["Oishe ","Tanver ","Bari"]
print(list(zip(roll,name)))
print(list(zip(roll,name,"ABC")))#ABC will be assigned serially

#another example
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(tuple(x))

#recursion

def fact(n):
     if n==1:
         return 1
     else:
         return n*fact(n-1)


print(fact(5))

#binary_search using recursion
print("Binary Search")
def binary_serach(l,key):

    if len(l)==0:
        return False
    mid=len(l)//2 #floor

    if l[mid]==key:
        return True
    elif key<l[mid]:
        return binary_serach(l[:mid],key)
    else:
        return binary_serach(l[mid+1:],key)

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
key=7
result=binary_serach(l,key)
print(result)

key=6795
result=binary_serach(l,key)
print(result)



def linearSearch(l,key):
    for value in l:
        if key==value:
            return True;
        else:
            False

l=[1,2,3,4,5,6,7,8,88,99,]
key=7
result=linearSearch(l,key)
print(result)

#ascii value
print(ord('t'))
print(chr(97))

import random
def gen_password(length=8):
    ll=['@','#','$','&']
    upper=chr(random.randint(60,90))
    lower=chr(random.randint(97,122))
    special=random.choice(ll)
    digit=random.randint(10000,99999)
    password=upper+lower+special+str(digit)
    ll=random.sample(password,length)
    password=("").join(ll)
    return password

result=gen_password(5)
print(result)
result=gen_password()
print(result)
r=gen_password(length=6) #we can call with arguments like this, the parameters have to be same as
# it is described in the definintion, in this case sequence of the parameters need not to be maintained according to
# function definition

#print function
#help(print)

print(100,200,sep=",",end=" ")
print("tanverlikhon@gmail.com")

#functions having no fixed length of arguments

def add_value(*args): # * is compulsory , we can use like *l instead of *args
    print(args)
add_value(1,2,3,4) #pack the values as tuples
add_value(5,6)

###########
def get_details(**kwargs):#it will pack all the values in a dictionary
    print(kwargs)


get_details(name="tanverlikhon",email="tanverlikhon@gmail.com",contact=88017819495,dob="05-04-2009")
get_details(name="tanverlikhon",email="tanverlikhon@gmail.com",dob="05-04-2009")
get_details(name="tanverlikhon",email="tanverlikhon@gmail.com")