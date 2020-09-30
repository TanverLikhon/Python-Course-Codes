# difference between list and tuples is that values of the list can be
# changed which is not possible in tuples
# tuples is faster than list
# '''

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

#for counting occurance of an element  t.count()

#converting a list to tuple
l=[10,20,30]
t=tuple(l)

# tuple to list
l1=list(t)