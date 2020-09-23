# DataTypes
# 1 Int
num=100
print(num)
print(type(num))

#2 float
num2=15.25
print(id(num2)) #memory locatins will be different with line 12
print(num2)
print(type(num2))
num2=15.56
print(id(num2))

# 3 string '' "" """  is valid python string
str="python"
print(str,type(str),id(str))

s="'Python' sample string "
print(s,type(s),id(s))


# s=" "Pyhton" sample string " this line will be considered as a empty strting then a varibale Pythone and another string
# sample string

#4 List : anything is enclosed in square bracket in python is list (mutable data type)
#mutable data type means add delete or uptdate operation can be done with this



subjects=["C","C++","Java","Python",6795]
print(subjects)#prints all the elements
print("Printing Location",id(subjects))
print(subjects[0])

print(subjects[2:])#prints elements from index 2
print(subjects[-1])#prints elements from reverse

subjects=subjects+["TOC","Algorithm"]#adding elements
print(subjects)

print(subjects*3)#prints the element 3 times

print(len(subjects))#prints the size
subjects.append("PHP")#adding elements / after appending the memory location will be the same
print(subjects)
subjects.insert(2,"OS")#insert elemlent at index 2
print(subjects)

array=[5,8,9,2,6,3]
print(array)
array.remove(3)#remove element 3 not index
print(array)
array.sort()#sort the list
print(array)
array.reverse()#reverese sort
print(array)
array.pop()#remove the last element of the list
print(array)
pos=array.index(6)##returns the index of element 6
print(pos)
print(array.count(6))#occurrence of 6
array2=array.copy()#copy the list
print(array2)

###taking list of integer

n= input("Enter a text of numbers")
list =n.split()
for x in list:
    print(x)

text=input("Enter a text: ")

character=0
word=0
number=0

list=text.split()
for x in list:
    x=x.lower()
    if x>='a' and x<='z':
        character=character+1
    elif x==' ':
        word=word+1

#5 Tubple: (non mutable datatype)

'''
difference between list and tuples is that values of the list can be
changed which is not possible in tuples
tuples is faster than list
'''

name=(
    "Tanver ahmed likhon",
    "Hasanul Bari",
    "Bangladesh",
    ("hello","one ","two ","three ")##tuples under tuples

)
name1 = "hello","World"
##giving first bracket is optional

print(name)
print(name[2])
print(name1)
print(name[1:])#will print values from index 1
#name[0]="5555" #it's an error as it is changing value
#name1[0]="5555" #it's an error as it is changing value


# 6 Dictionary: storing value under a key also called a hashmap

# like map in c++
studentId={
    "1702028": "Tanver Ahmed Likhon",
    "1702029": "Saroyar Ahmed",
    "1702029": "OverLap",
    1702065:"Hasanul Bari"
}

print(studentId["1702029"])
print(studentId.get("1702028"))
print(studentId.get("1702030"))#print none if not found
#print(studentId["1702030"])#will print and error if not found
print(studentId.get("1702022","Message"))#print message if not found
print(studentId[1702065])

# 7 set {}

'''
set is an unordered collection of items
can't be accessed using index number
no duplicate values

can be created using
 -curly bracket {}
 - using set function
 -mutable data type :)


'''

num={1,2,3,4,5,5}
print(num)

num1= set([4,5,6])# converting the list into set
print(num1)

num.add(7)
print(num)
num.remove(7)
print(num)
print(7 in num)#checking whether 7 is in the set or not
print(7 not in num)

#some other operations

print(num | num1)#unioun
print(num & num1)#intersection
print(num - num1)#difference

# 8 bool true and false
# 9 complex: 4+3j

help(str) # will show the methods of string as str is a string variable previously declared