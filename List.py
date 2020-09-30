#list are mutable
# add update and delete
#ordered : indexing and slicing
#can store any type of data
# heterogeneous datatype


subjects=["C","C++","Java","Python",6795]
print(subjects)#prints all the elements

print(subjects[0])

print(subjects[2:])#prints elements from index 2
print(subjects[-1])#prints elements from reverse

subjects=subjects+["TOC","Algorithm"]#adding elements
print(subjects)

print(subjects*3)#prints the element 3 times

print(len(subjects))#prints the size
subjects.append("PHP")#adding elements
print(subjects)
subjects.insert(2,"OS")#insert elemlent at index 2
print(subjects)

#extend method for adding multiple element
subjects.extend(["C#","Ruby"])
print(subjects)

subjects.append(["C#","Ruby"])#this will add the list as an element
print(subjects)

l1=[10,20,30]
l2=l1

l1.append(40)#40 will be appended in bot l1 and l2 because both of the lists' memory location is same
print(id(l1),id(l2))
print(l1)
print(l2)

#but if we copy then there will be different memory location
l1=[10,20,30]
l2=l1.copy()

l1.append(40)#40 will be appended in bot l1 and l2 because both of the lists' memory location is same
print(id(l1),id(l2))
print(l1)
print(l2)

r=l1.pop()#return last element
print(r)


array=[5,8,9,2,6,3]
print(array)
#l.cear() to clear the list
del l1 #this will delete the reference of the list

array.insert(2,25)#index and value


array.remove(3)#remove element 3 not index,will remove one element at a time not all the occurence
print(array)
array.sort()#sort the list,
print(array)

l3=sorted(array)#will return a sorted list/ this function also works in tuple and dictionary


array.reverse()#reverese sort
print(array)
array.pop()#remove the last element of the list
print(array)
pos=array.index(6)##returns the index of element 6
print(pos)
print(array.count(6))#occurrence of 6
array2=array.copy()#copy the list
print(array2)

#indexing and slicing
print("reverse indexing")
print(array[-1])
l=[10,20,30,"Python","Java",[100,200,300]]
print(l[-1][1])
#slicing is similliar to string
print(l[1:3])
print(l[:-1])

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

