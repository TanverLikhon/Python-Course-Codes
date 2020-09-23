i =1
while i<=100:
    print(i)
    i=i+1
print("End of the program")

num=list(range(10))# value from 0 to 4

for x in num:
    print(x)

num=int(input("Enter number :"))
sum=0
for x in range(1,num+1,1):
    sum=sum+x

print(sum)

# break-ager moto
# continue- ager moto
# enumerate
# else block for for loop


l=[10,20,30,40]
key=405
for value in l:
    if value==key:
        print("Element Found")
        break
    else:
        continue
else:
    print("Element not found")

#enumerate
for index,value in enumerate(l): #can be use like for loop
    print(index,value)


#use of pass statement: else block e ki korte hbe ami jokhon janina tokhon seta pass kore dibo nahole
#syntax error hobe

if(0):
    print("hello")
else:
    pass
    #pass er poro onno statement thakle setao execute hobe

#tanverlikhon@gmail.com