# iterators are much more better in terms of time and m  emory complexity in comparison to normal data type


# l=[1,2,3,4,5,6,7,8,9]
# i= iter(l)
# print(next(i))
# print(next(i))
#
# for value in i:
#     print(value)

import itertools

l1=[1000,20,300,40,5000,60,7000,80,9000]
l2=[100,200,300,400,500,600,700,800,900]
l3=[10,2000,30,4000,50,6000,70,8000,90]

i=itertools.chain(l1,l2,l3)#returns chain object
print(i)
print(next(i))
print(next(i))
print(next(i))
#for loop can be used

count=0

for value in itertools.cycle(l1):#cycle method will create infinite iterator over list l1
    if count<20:
        print(value)
        count+=1
    else:
        break
count=0;
for value in itertools.repeat(l1):#in every iteration i will get the same list
    if count<20:
        print(value)
        count+=1
    else:
        break

l=[1,2,23]
i=iter(l)
t=itertools.tee(i,5)# there will be five object which means i can iterate 5 times

# for value in i:
#     print(value)
#print(next(i))#this will be an error because iterator can be back to first element


for value in t[0]:#t[0] because it is tuple of two values by default
    print(value)
for value in t[1]:#to iterate again
    print(value)

#slicing of existing iterator
i=itertools.chain(l1,l2,l3)

for value in itertools.islice(i,0,8):# 8 is non inclusive
    print(value)

for value in itertools.count(10,5):#count(start_point,increment) can't specify the end
    if count>20:
        break
    else:
        print(value)
    count+=1 #this statement is default increment of count


l=[1,2,3,4,5,6]
print(list(itertools.permutations(l,2)))

print(list(itertools.combinations(l,2)))
