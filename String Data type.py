#string :
# s=' ' " " """ """ are valid
# strings are immutable: that means i can not modify the value of the same memory location
# string is ordered data structure: indexing and slicing

s="Python sample string"
print(type(s))

s1="Python"
print(id(s1))

s1="C++"
print(id(s1))  # here variable is same but memory location will be different

#indexing
print(s[0]) #indexing from right side
print(s[-1]) #indexing from right side
print(s[-2]) #indexing from right side

#slicing
#0-5
print(s[0:5])# this will print from index 0 to 4
print(s[7:])# this will print from index 7 to the end
print(s[:6])# this will print from index 0 to 5


# stride
print(s[::2])# it will print every second character
print(s[::-1])# it will print the string in reverse order
print(s[::-2])# it will print every second character of the string in reverse order

for value in s[::2]:
    print(value)

help(str)

#detail functions for string

# foramt

num1=100
num2=200

print("Value of num1 is {} value of num2 {}".format(num1,num2))# by default first {} index is zero
print("Value of num1 is {1} value of num2 {0}".format(num1,num2))#we can define index also
print("Value of num1 is {val2} value of num2 {val2}".format(val1=num1,val2=num2))#we can define index also
s4="tanver likhon"
s4=s.capitalize()
print(s4) #it will make first letter to uppercase

print(s4.upper())#every character will be in uppercase
s4=s4.upper()
print(s4.isupper())

print(s4.lower())#every character will be in lowercase
s4=s4.lower()
print(s4.islower())

print(s4.title())#every first letter of words will be in uppercase
s4=s4.title()
print(s4.istitle())

# but there is no is capitalize built in function

#split and join

s="HTML,CSS,PYTHON,JAVA,C++"
l=s.split(",")#it will split on the basis of comma
print(l)
sj=(" ").join(l)#there will be space between two strings
print(sj)

s1="abcd"
s2="1234"
s3="Python Sample string abcd"

# if we want to replace all abcd with 1234 a b c d will be replaced by
# 1 2 3 4 respectively
#maketrans and translate

table=str.maketrans(s1,s2)# mapping table
result=s3.translate(table)
print(result)

#index
#find
#rfind functions

s1="HTML,CSS,PYTHON,JAVA,C++"
print("PYTHON" in s)
print(s.index("PYTHON"))# will return index of P (index of first occurence of PYTHON)
print(s.find("PYTHON"))# will return index of P (index of first occurence of PYTHON)
# if not found it will return -1 this is the difference between find() and index()
print(s.rfind("PYTHON"))#index from right side

s="       Tanver Ahmed Likhon           "
s1=s.strip(" ")# will remove spaces before and after the string .
# We can pass any character in the function to be romoved
print(s1)
#lstrip(" ")to remove from left side
#rstrip(" ")to remove from right side
s="tanverlikhon"
s1=s.center(20,"*") # make fixed length adding * on both sides
print(s1)
#ljust(20,"*")
#rjust(20,"*")

s="html,css,python,html"
s1=s.replace("html","HTML5") # will replace html with HTML5
print(s1)