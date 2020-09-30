'''
set is an unordered collection of items
can't be accessed using index number,no slicing
:mutable
no duplicate values
can add immutable elements

can be created using
 -curly bracket {}
 - using set function


'''

num={1,2,3,4,5,5}
print(num,type(num))

num1= set([4,5,6])# converting the list into set
print(num1)

num.add(7)
print(num)
num.remove(7)
print(num)
print(7 in num)#checking whether 7 is in the set or not
print(7 not in num)

#some other operations

print(num | num1)#unioun  / num3=num1.union(num2)
print(num & num1)#intersection/ num3=num1.intesection(num2)
print(num - num1)#difference/ num3=num1.difference(num2)

#s3=s1.symmetric_difference(s2) it will return all the elements of s1 and s2 except the common element

num.update(num1) #union and it will uptdate num nd will not return any thing
num.intersection_update(num1)#intersection and it will uptdate num nd will not return any thing
num.difference_update(num1)#difference and it will uptdate num nd will not return any thing
print("subset")
#subset
s1={1,2,3,4,5}
s2={1,2,3}
print(s2.issubset(s1))
print(s2.issuperset(s1))

l1=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]

ss1=set(l1)
ss2=set(l2)

ss3=ss1.union(ss2)
print(ss3)

l3=list(ss3)

# remove pop discard clear del

r=ss1.pop()
print("pop",r)
ss1.remove(2)#will remove element 1, if value doesn't exist it will show an error

ss2.discard(100) #same as remove but it will not show error if value doesn't exist and will just ignore in this case

ss2.clear() # remove all element