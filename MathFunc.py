import math
from math import*

print(max(5,6,7,2,9))
print(min(2,3))
print(abs(-6))
print(floor(5.6))
print(ceil(5.5))
print(round(3.6))
print(round(3.2))
print(sqrt(99))
print(factorial(9))
print(sin(30))#values are taken in radian
print(sin(radians(30)))
#similiar cos tan

num1=45.55506
print(math.modf(num1))#will return tuple
d,i=math.modf(num1)#decimal and iteger part
print(i,d)

#random
import random
print(random.random())#random number between zero and one

l2=[1,2,3,4,5,6]
print(random.choice(l2))#random number from the list

print(random.randint(10,100))#10 to 100
print(random.randrange(10,100))#10 to 99
print(random.uniform(10,20))# floating point number from 10 to 20


# Python code to demonstrate the working of
# log(a,Base)

# Printing the log base e of 14
print ("Natural logarithm of 14 is : ", end="")
print (math.log(14))

# Printing the log base 5 of 14
print ("Logarithm base 5 of 14 is : ", end="")
print (math.log(14,5))

l=[1,2,3,4,5]
print(sum(l))
print(max(l))
print(min(l))
print(round(2.567))
print(round(2.56,2))#rounded upto two decimal point

l=[0.1]*10 # will repeat 0.1 10 times
print(l)
print(sum(l))#it has rounding issues for floating point numbers
print(math.fsum(l)) #for floating point numbers

help(math)
print(dir(math))