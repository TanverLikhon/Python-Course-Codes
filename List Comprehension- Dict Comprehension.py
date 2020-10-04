l=[100,200,300,400,500]
l2=[]
for value in l:
    l2.append(value*value)
print(l2)

l3=[value*value for value in l] # using list comprehension
print(l3)

l=[10,20,25,30,35,60,65,70,85]
l4=[value for value in l if value%2==0] #faster than using normal for loop
print(l4)

l=['abc','abcd','abcde','zzzzzzzz']
l2=[len(value) for value in l]
print(l2)

#nested for loo

l2=[(value1,value2)for value1 in range(1,5)for value2 in range(100,103)]
print(l2)

l=[[1,2,3],[4,5,6],[7,8,9]]
l2=[value1 for value in l for value1 in value]
print(l2)

l3=["Even" if value%2==0 else "Odd" for value in l2]
print(l3)

d={x:x**2 for x in range(1,11)}
print(d)

d2={value:key for key,value in d.items()}
print(d2)